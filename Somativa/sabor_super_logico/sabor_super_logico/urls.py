
from django.contrib import admin
from django.urls import path, include

# Configuração principal de URLs do projeto .
# recebe todas as requisições primeiro e decide para onde encaminhar:
# 1. Se for para 'admin/', manda para o painel administrativo do Django.
# 2. Se for para qualquer outra coisa (path vazio ''), ele usa o 'include' para repassar a responsabilidade
# para o arquivo 'urls.py' que está dentro da pasta 'restaurante_api'.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurante_api.urls')),
]
