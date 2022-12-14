from django.contrib import admin
from django.urls import path
from field_form_app import views

urlpatterns = [
    path('', views.index),
    path('main', views.main)
]
