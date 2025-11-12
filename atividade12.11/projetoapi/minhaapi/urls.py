from django.urls import path
from .views import item_list

urlpatterns = [
    path('itens/', item_list, name='item-list'),
]