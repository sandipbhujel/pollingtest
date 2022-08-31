from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('vote/<poll_id>', views.vote, name='vote'),
    path('results/<poll_id>', views.results, name='results'),

]
