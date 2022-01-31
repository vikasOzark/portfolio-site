from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # home/
    path('',  views.index, name = 'home'),
    # home/contact/
    path('contact/', views.contact, name='contact'),
    path('project/', views.project, name='project'),
    path('login/', views.view_login, name='login'),
    path('register/', views.register, name = 'register'),
    path('logout/', views.view_logout, name = 'logout')
]
