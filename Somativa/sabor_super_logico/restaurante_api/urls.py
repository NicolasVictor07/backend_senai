from django.urls import path
from .views import (Cliente_listarCriar,Listar_Atualizar_Deletar_Cliente, Funcionario_listarCriar, Listar_Atualizar_Deletar_Funcionario,
                     Mesa_listarCriar, Listar_Atualizar_Deletar_Mesa, Fornecedor_listarCriar, Listar_Atualizar_Deletar_Fornecedor, 
                     Categoria_listarCriar, Listar_Atualizar_Deletar_Categoria, Ingrediente_listarCriar, 
                     Listar_Atualizar_Deletar_Ingrediente, Produto_listarCriar, Listar_Atualizar_Deletar_Produto, Compra_listarCriar, 
                     Listar_Atualizar_Deletar_Compra, Pedido_listarCriar, Listar_Atualizar_Deletar_Pedido, ItemPedido_listarCriar, 
                     Listar_Atualizar_Deletar_ItemPedido, Pagamento_listarCriar, Listar_Atualizar_Deletar_Pagamento)

# Define as rotas (endpoints) da sua API.
# ele funciona como um "mapa": ele diz ao Django qual função (View) deve ser executada
# quando alguém acessa um endereço específico.
urlpatterns = [
    path('clientes/', Cliente_listarCriar, name='clientes_listar_criar'),
    path('clientes/<int:id>/', Listar_Atualizar_Deletar_Cliente, name='cliente_detalhe'),

    path('funcionarios/', Funcionario_listarCriar, name='funcionarios_listar_criar'),
    path('funcionarios/<int:id>/', Listar_Atualizar_Deletar_Funcionario, name='funcionario_detalhe'),

    path('mesas/', Mesa_listarCriar, name='mesas_listar_criar'),
    path('mesas/<int:id>/', Listar_Atualizar_Deletar_Mesa, name='mesa_detalhe'),

    path('fornecedores/', Fornecedor_listarCriar, name='fornecedores_listar_criar'),
    path('fornecedores/<int:id>/', Listar_Atualizar_Deletar_Fornecedor, name='fornecedor_detalhe'),

    path('categorias/', Categoria_listarCriar, name='categorias_listar_criar'),
    path('categorias/<int:id>/', Listar_Atualizar_Deletar_Categoria, name='categoria_detalhe'),

    path('ingredientes/', Ingrediente_listarCriar, name='ingredientes_listar_criar'),
    path('ingredientes/<int:id>/', Listar_Atualizar_Deletar_Ingrediente, name='ingrediente_detalhe'),

    path('produtos/', Produto_listarCriar, name='produtos_listar_criar'),
    path('produtos/<int:id>/', Listar_Atualizar_Deletar_Produto, name='produto_detalhe'),

    path('compras/', Compra_listarCriar, name='compras_listar_criar'),
    path('compras/<int:id>/', Listar_Atualizar_Deletar_Compra, name='compra_detalhe'),

    path('pedidos/', Pedido_listarCriar, name='pedidos_listar_criar'),
    path('pedidos/<int:id>/', Listar_Atualizar_Deletar_Pedido, name='pedido_detalhe'),

    path('itens_pedido/', ItemPedido_listarCriar, name='itens_pedido_listar_criar'),
    path('itens_pedido/<int:id>/', Listar_Atualizar_Deletar_ItemPedido, name='item_pedido_detalhe'),

    path('pagamentos/', Pagamento_listarCriar, name='pagamentos_listar_criar'),
    path('pagamentos/<int:id>/', Listar_Atualizar_Deletar_Pagamento, name='pagamento_detalhe'),
]