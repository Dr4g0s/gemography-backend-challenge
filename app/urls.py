from django.urls import path
from app import views


urlpatterns = [
    path('repos-list/', views.github_repos_list_api_view, name='pure_repos_list'),
    path('language-list/', views.language_list_api_view, name='language_list'),
]