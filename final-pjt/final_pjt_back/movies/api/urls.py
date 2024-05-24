from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('v1/current_movies/', views.current_movies),
    path('v1/search/', views.search),
    path('v1/upcoming_movies/', views.upcoming_movies),
    path('v1/main/', views.main_view),
    path('v1/top_rated/', views.movie_sort_popularity),
    path('v1/movie/<str:movie_id>/', views.movie_detail),
    path('v1/choice/', views.choice),
    path('v1/choice/result/', views.choice_result),
    path('v1/<str:movie_id>/reviews/', views.review),
    path('v1/current_user/', views.current_user),
    path('v1/<str:movie_id>/like/', views.movie_like),
    path('v1/<str:movie_id>/associate/', views.movie_associate),
    path('v1/<str:movie_id>/chat/', views.movie_chat),
    path('v1/profile/', views.profile),
    path('v1/profile/reviews/', views.profile_review),
    path('v1/profile/member_leave/', views.member_leave),
    path('v1/profile/change_nickname/', views.nickname_change),
]
