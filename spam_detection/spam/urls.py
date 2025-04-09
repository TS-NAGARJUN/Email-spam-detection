from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This maps /index/ to the index view
    path('index/',views.index,name='index'),
    path('check',views.checkSpam,name = 'CheckSpam'),
]
