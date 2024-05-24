from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
# Create your models here.

class Movie(models.Model):
    movie_id = models.CharField(primary_key=True, max_length=50)
    title = models.CharField(max_length=150)
    overview = models.TextField(max_length=300)
    poster = models.TextField(null=True)
    opening_date = models.DateField(null=True)
    running_time = models.IntegerField(null=True)
    review_score = models.FloatField()
    
    # 영화 개봉 상태
    STATUS_CHOICES = [
        (0, '개봉'),
        (1, '개봉 예정'),
        (2, '기타'),
    ]
    STATUS_SECTION = [MaxValueValidator(2), MinValueValidator(0)]
    show_status = models.IntegerField(validators=STATUS_SECTION, choices=STATUS_CHOICES)
    
    # 1:N
    country = models.ForeignKey("Country", on_delete=models.CASCADE)
    
    # N:M
    producer = models.ManyToManyField("Producer", verbose_name="producer_movie")
    actor = models.ManyToManyField("Actor", verbose_name="actor_movie")
    genre = models.ManyToManyField("Genre", verbose_name="genre_movie")
    
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    review_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='review_movies', through='MovieReview')
    chat_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='chat_movies', through='MovieChat')

    def __str__(self):
        return self.title
    
class Producer(models.Model):
    producer_id = models.CharField(primary_key=True, max_length=50)
    producer = models.CharField(max_length=150)
    profile_image = models.TextField(null=True)
    
    def __str__(self):
        return self.producer
    
class Actor(models.Model):
    actor_code = models.CharField(primary_key=True, max_length=50)
    actor = models.CharField(max_length=50)
    profile_image = models.TextField(null=True)

    def __str__(self):
        return self.actor
    
class Country(models.Model):
    country = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.country
    
class Genre(models.Model):
    genre = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.genre
    
def snapshot_upload_to(instance, filename):
    return f'{instance.movie.title}/snapshot/{filename}'

class Snapshot(models.Model):
    snapshot = models.TextField(blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='snapshots')
    
    def __str__(self):
        return f'Snapshot for {self.movie.title}'
    
    
class MovieReview(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class MovieChat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)