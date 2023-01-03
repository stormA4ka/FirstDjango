"""FirstDjango URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from MainApp import views


urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('items/', views.items, name="items-list"),
    path('item-page/<int:id>', views.item_details, name="item-page"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
