import os
import requests as req
from django.shortcuts import render, redirect
from datetime import datetime
from django.db import transaction
from .models import *

# Create your views here.

MV_API_KEY = os.environ.get('MV_API_KEY')
TMDB_API_KEY = os.environ.get('TMDB_API_KEY')

def index(request):
    
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }

    return render(request, 'movies/index.html', context)

def actor(request):
    actors = Actor.objects.all()
    context = {
        'actors': actors
    }
    
    return render(request, 'movies/actor.html', context)


def download_movie(request):
    
    MV_URL = f'http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?'
    TMDB_URL = f'https://api.themoviedb.org/3/search/movie?'
    
    for i in range(800, 850):
        print(i)
        MV_params = {
            'key': 'd45082b888da87c39065fcb53e176f8e',
            'curPage': i,
            'itemPerPage': 50,
        }
        
        data = req.get(MV_URL, params=MV_params).json().get('movieListResult').get('movieList')
        
        for movie in data:
            title = movie.get('movieNm')
            movie_code = movie.get('movieCd')
            
            TMDB_params = {
                'api_key': TMDB_API_KEY,
                'query': title,
                'language': 'ko-KR',
                'page': 1,
            }
            
            try:
                TMDB = req.get(TMDB_URL, params=TMDB_params).json().get('results')[0]
            except Exception as e:
                print(f'Error: {e}')
                continue
            
            try:
                movie_data = req.get(f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={MV_API_KEY}&movieCd={movie_code}').json().get('movieInfoResult').get('movieInfo')
            except Exception as e:
                print(f'Error: {e}')
                continue
            
            countries = download_country(movie_data.get('nations'))
            if countries != []:
                country = countries[0]
            else:
                country = '기타'

            genres = download_genres(movie_data.get('genres'))
            actors = download_actor(movie_data.get('actors'), title)
            directors = download_producers(movie_data.get('directors'), title)
            
            overview = TMDB.get('overview')
            review_score = TMDB.get('vote_average')
            poster = TMDB.get('poster_path')
            show_status_raw = movie.get('prdtStatNm')
            
            if show_status_raw == '개봉':
                show_status = 0
            elif show_status_raw == '개봉예정':
                show_status = 1
            else:
                show_status = 2
            
            if poster == '' or poster is None:
                poster = None
            else:
                poster = f'https://image.tmdb.org/t/p/original{poster}'
            
            try:
                opening_date = datetime.strptime(movie_data.get('openDt'), '%Y%m%d').date()
            except:
                opening_date = None
            
            
            running_time = movie_data.get('showTm')
            if running_time == '':
                running_time = None
            
            
            movie = Movie(
                movie_id=movie_code,
                title=title,
                overview=overview,
                poster=poster,
                opening_date=opening_date,
                running_time=running_time,
                review_score=review_score,
                show_status=show_status,
                country=country
            )
            movie.save()
            print('movie saved')
            
            try:
                download_snapshot(TMDB.get('id'), movie)
            except Exception as e:
                print(f'snapshot error :{e}')
            
            for genre in genres:
                movie.genre.add(genre)
            
            for actor in actors:
                movie.actor.add(actor)
            
            for director in directors:
                movie.producer.add(director)
            
            
    print('done')
    return redirect('index')


def download_genres(genres):
    new_genres = []
    
    if not genres:
        return list()
    
    for genre in genres:
        new_genre, created = Genre.objects.get_or_create(genre=genre.get('genreNm'))
        new_genres.append(new_genre)
        
    return new_genres


def download_actor(actors, movie_name):
    new_actors = []
    try:
        for idx in range(5):
            actor_name = actors[idx].get('peopleNm')
            URL = 'http://kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?'
            params = {
                'key': MV_API_KEY,
                'peopleNm': actor_name,
                'filmoNames': movie_name,
            }
            actor_data = req.get(URL, params=params).json().get('peopleListResult').get('peopleList')[0]
            actor_name = actor_data.get('peopleNm')
            actor_code = actor_data.get('peopleCd')
            
            TMDB_URL = 'https://api.themoviedb.org/3/search/person?'
            TMDB_params = {
                'api_key': TMDB_API_KEY,
                'query': actor_name,
                'language': 'ko-KR',
            }
            try:
                response = req.get(TMDB_URL, params=TMDB_params).json().get('results')
            except:
                continue
            
            if response:
                profile_image_url = f'https://image.tmdb.org/t/p/original{response[0].get("profile_path")}'
            else:
                continue
                
            new_actor, created = Actor.objects.get_or_create(actor_code=actor_code, actor=actor_name, profile_image=profile_image_url)
            new_actors.append(new_actor)
            
    except IndexError:
        return new_actors
    
    return new_actors


def download_country(countries):
    new_countries = []
    
    if countries is None or countries == []:
        return list()
    
    for country in countries:
        country_name = country.get('nationNm')
        new_country = Country(country=country_name)
        new_country.save()
        new_countries.append(new_country)
    
    return new_countries


def download_producers(producers, movie_name):
    new_producers = []
    
    if not producers:
        return list()
    
    for producer in producers:
        URL = 'http://kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?'
        params = {
            'key': MV_API_KEY,
            'peopleNm': producer.get('peopleNm'),
            'filmoNames': movie_name,
        }
        try:
            producer_data = req.get(URL, params=params).json().get('peopleListResult').get('peopleList')[0]
        except:
            continue
        
        producer_name = producer_data.get('peopleNm')
        producer_code = producer_data.get('peopleCd')
        
        TMDB_URL = 'https://api.themoviedb.org/3/search/person?'
        TMDB_params = {
            'api_key': TMDB_API_KEY,
            'query': producer_name,
            'language': 'ko-KR',
        }
        try:
            TMDB_data = req.get(TMDB_URL, params=TMDB_params).json().get('results')
        except:
            continue
    
        if not TMDB_data:
            continue
        
        try:
            producer_image_url = 'https://image.tmdb.org/t/p/original' + TMDB_data[0].get('profile_path')
        except:
            continue
        
        new_producer, created = Producer.objects.get_or_create(producer_id=producer_code, producer=producer_name, profile_image=producer_image_url)
        new_producers.append(new_producer)
        
    return new_producers

def download_snapshot(movie_id, movie_cd):
    URL = f'https://api.themoviedb.org/3/movie/{movie_id}/images?'
    params = {
        'api_key': TMDB_API_KEY,
    }
    data = req.get(URL, params=params).json().get('backdrops')
    
    for i in range(5):
        try:
            snapshot_url = data[i].get('file_path')
            
        except IndexError:
            break
        
        if snapshot_url != '' and snapshot_url is not None:
            snapshot = f'https://image.tmdb.org/t/p/original{snapshot_url}'
            new_snapshot = Snapshot(snapshot=snapshot, movie=movie_cd)
            new_snapshot.save()
            
def delete(request):
    movies = Movie.objects.filter(running_time__lt=30)
    for movie in movies:
        print(f'{movie.title} :삭제완료')
        movie.delete()
        
    return redirect('index')