
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inclui as URLs da sua API
    path('api/', include('minhaapi.urls')),
]