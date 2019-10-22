from django.urls import path
from . import views


urlpatterns = [
    path('', views.random_user, name='random_user'),
    path('five_new_users/', views.five_new_users, name='five_new_users'),
    path('all_users/', views.all_users, name='all_users'),
    path('users_deleted/', views.users_deleted, name='users_deleted'),
]
