from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('p1/', views.p1),
]