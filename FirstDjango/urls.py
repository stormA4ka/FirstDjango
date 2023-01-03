"""FirstDjango URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from MainApp import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('items/', views.items),
    path('item/<int:id>', views.item_details),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
