from django.urls import path
from . import views

urlpatterns = [
    path('saudacao/', views.saudacao,name='saudacao'),
]