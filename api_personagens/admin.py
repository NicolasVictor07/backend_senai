from django.contrib import admin
from .models import Personagem, AtorDublador, Obra, Habilidade, PersonagemHabilidades, Relacionamento
# Register your models here.

admin.site.register(Personagem)
admin.site.register(AtorDublador)   
admin.site.register(Obra)
admin.site.register(Habilidade)
admin.site.register(PersonagemHabilidades)
admin.site.register(Relacionamento)