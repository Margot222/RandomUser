from django.urls import path
from . import views


urlpatterns = [
    path('', views.random_user, name='random_user'),
]