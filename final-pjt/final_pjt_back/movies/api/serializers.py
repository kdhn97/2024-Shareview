from django.contrib.auth import get_user_model
from rest_framework import serializers
from ..models import *

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        
class ActorNameSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Actor
        fields = ('actor', )
        
class ProducerNameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Producer
        fields = ('producer', )
    

class MovieSerializer(serializers.ModelSerializer):
    
    actor = ActorNameSerializer(many=True, read_only=True)
    producer = ProducerNameSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('genre', 'country', 'actor', 'producer', 'title', )

class MovieListSerializer(serializers.ModelSerializer):
    
    
    actor = ActorNameSerializer(many=True, read_only=True)    
      
    class Meta:
        model = Movie
        fields = '__all__'
        
class ObjectCountSerializer(serializers.Serializer):
    movie_count = serializers.SerializerMethodField()
    genre_count = serializers.SerializerMethodField()
    producer_count = serializers.SerializerMethodField()
    actor_count = serializers.SerializerMethodField()
    country_count = serializers.SerializerMethodField()

    def get_movie_count(self, obj):
        return Movie.objects.count()
    
    def get_genre_count(self, obj):
        return Genre.objects.count()
    
    def get_producer_count(self, obj):
        return Producer.objects.count()
    
    def get_actor_count(self, obj):
        return Actor.objects.count()
    
    def get_country_count(self, obj):
        return Country.objects.count()
    

class MovieListSummarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('movie_id', 'title', 'poster', 'popularity', )
        
        
class MovieDetailSerializer(serializers.ModelSerializer):
    
    class MovieSnapshotSerializer(serializers.ModelSerializer):
        class Meta:
            model = Snapshot
            fields = ('snapshot',)
            
    class MovieActorListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = '__all__'
            
    class MovieProducerListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Producer
            fields = '__all__'
            
    actor = MovieActorListSerializer(many=True, read_only=True)
    snapshots = MovieSnapshotSerializer(many=True, read_only=True)
    producer = MovieProducerListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'

class MovieNestedSerializer(serializers.ModelSerializer):
    
    actor = ActorSerializer(many=True)
    producer = ProducerSerializer(many=True)
    
    class Meta:
        model = Movie
        fields = ('actor', 'genre', 'country', 'producer', 'title',)

class ChoiceSerializer(serializers.Serializer):
    movies = MovieNestedSerializer(many=True)
    genres = GenreSerializer(many=True)
    countries = CountrySerializer(many=True)
    actors = ActorSerializer(many=True)
    producers = ProducerSerializer(many=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'id', 'email', 'nickname', )


class ReviewListSerializer(serializers.ModelSerializer):
         
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = MovieReview
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MovieReview
        fields = '__all__'
        read_only_fields = ('user', 'movie',)


class UserLikedMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'poster', 'movie_id')


class UserProfileSerializer(serializers.ModelSerializer):
    like_movies = UserLikedMovieSerializer(many=True, read_only=True)
    review_movies = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'like_movies', 'review_movies', 'nickname', 'profile_image',)
        
    def get_review_movies(self, obj):
        movies = obj.review_movies.all()
        return UserLikedMovieSerializer(movies, many=True).data


class MovieLikeSerializer(serializers.Serializer):
    is_liked = serializers.SerializerMethodField()
    
    def get_is_liked(self, obj):
        user = self.context['request'].user
        movie = obj
        
        return user in movie.like_users.all()
    
class MovieChatSerialzier(serializers.ModelSerializer):
    
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = MovieChat
        fields = '__all__'
        read_only_fields = ('user', 'movie',)
        
        
class MovieResultSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('movie_id', 'title', 'opening_date', 'review_score', 'poster')