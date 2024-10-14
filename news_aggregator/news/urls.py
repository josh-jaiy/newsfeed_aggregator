from django.urls import path
from . import views  # Import the views module correctly

urlpatterns = [
    path('', views.news, name='news'),  # Use views.news correctly here
    path('articles/', views.article_list, name='article_list'),  # Articles page
]
