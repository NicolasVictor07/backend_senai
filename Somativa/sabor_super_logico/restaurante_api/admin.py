from django.contrib import admin
from .models import (Fornecedor, Categoria, Ingrediente, Funcionario, Mesa, Cliente,
                    Compra, Produto, ProdutoIngrediente, Pedido, ItemPedido, Pagamento)

# Register your models here.
admin.site.register(Fornecedor)
admin.site.register(Categoria)
admin.site.register(Ingrediente)
admin.site.register(Funcionario)
admin.site.register(Mesa)
admin.site.register(Cliente)
admin.site.register(Compra)
admin.site.register(Produto)
admin.site.register(ProdutoIngrediente)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(Pagamento)