from rest_framework import serializers
from .models import (Fornecedor, Categoria, Ingrediente, Funcionario, Mesa, Cliente, Compra, Produto,
                      ProdutoIngrediente, Pedido, ItemPedido, Pagamento)

# Define os Serializers, que funcionam como "tradutores" entre o banco de dados e a API.
# Eles convertem os objetos do Python (Models) para JSON 
# e também validam o JSON recebido antes de transformar em dados para salvar no banco.

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
       model = Fornecedor
       fields = '__all__'
       read_only_fields = ['id']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
       model = Categoria
       fields = '__all__'
       read_only_fields = ['id']

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
       model = Ingrediente
       fields = '__all__'
       read_only_fields = ['id']

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
       model = Funcionario
       fields = '__all__'
       read_only_fields = ['id']

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
       model = Mesa
       fields = '__all__'
       read_only_fields = ['id']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
       model = Cliente
       fields = '__all__'
       read_only_fields = ['id']   
    
class CompraSerializer(serializers.ModelSerializer):
    class Meta:
       model = Compra
       fields = '__all__'
       read_only_fields = ['id']

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
       model = Produto
       fields = '__all__'
       read_only_fields = ['id']

class ProdutoIngredienteSerializer(serializers.ModelSerializer):
    class Meta:
       model = ProdutoIngrediente
       fields = '__all__'
       read_only_fields = ['id']
    
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
       model = Pedido
       fields = '__all__'
       read_only_fields = ['id']

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
       model = ItemPedido
       fields = '__all__'
       read_only_fields = ['id']

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
       model = Pagamento
       fields = '__all__'
       read_only_fields = ['id']








