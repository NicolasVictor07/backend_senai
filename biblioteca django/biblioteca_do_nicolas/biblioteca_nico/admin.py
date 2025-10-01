from django.contrib import admin
from .models import Autor, Categoria, Livro, Livro_Autor, Livro_Categoria,Associacao,Emprestimo,Usuario
# Register your models here.

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Livro)
admin.site.register(Livro_Autor)
admin.site.register(Livro_Categoria)
admin.site.register(Associacao)
admin.site.register(Emprestimo)
admin.site.register(Usuario)