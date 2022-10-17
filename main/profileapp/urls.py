from typing import ValuesView
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('profile/', views.profile, name = 'profile'),
    path('login/', views.login_person, name = 'login'),
    path('register/', views.registration, name = 'register'),
    path('logout/', views.logout_user, name = 'logout'),
]
