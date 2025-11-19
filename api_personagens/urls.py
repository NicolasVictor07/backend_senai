from django.urls import path
from .views import lista_personagens, lista_atores_dubladores, lista_obras, lista_habilidades, lista_personagem_habilidades, lista_relacionamentos

urlpatterns = [
    path('personagens/<int:id>/', lista_personagens, name='lista_personagens'),
    path('atores_dubladores/<int:id>/', lista_atores_dubladores, name='lista_atores_dubladores'),
    path('obras/<int:id>/', lista_obras, name='lista_obras  '),
    path('habilidades/<int:id>/', lista_habilidades, name='lista_habilidades'),
    path('personagem_habilidades/<int:id>/', lista_personagem_habilidades, name='lista_personagem_habilidades'),
    path('relacionamentos/<int:id>/', lista_relacionamentos, name='lista_relacionamentos'),
]



