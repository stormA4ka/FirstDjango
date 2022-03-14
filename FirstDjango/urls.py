"""FirstDjango URL Configuration"""
from django.contrib import admin
from django.urls import path
from MainApp import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('items/', views.items),
    path('item/<int:id>', views.item_details),
]
