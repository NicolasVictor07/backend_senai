from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=255)

    def __str__(self):
        return self.nome

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    quantidade_estoque = models.DecimalField(max_digits=10, decimal_places=2)
    unidade_medida = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome
    
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    senha = models.CharField(max_length=255)
    

    def __str__(self):
        return self.nome
    
class Mesa(models.Model):

    STATUS_MESA_CHOICES = [
        ('disponivel', 'Disponível'),
        ('ocupada', 'Ocupada'),
        ('reservada', 'Reservada'),
    ]
    
    numero = models.IntegerField()
    capacidade = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_MESA_CHOICES, default='disponivel')

    def __str__(self):
        return f"Mesa {self.numero}"
    

class Cliente(models.Model):
    TIPO_CLIENTE_CHOICES = [
        ('regular', 'Regular'),
        ('vip', 'VIP'),
    ]
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    tipo_cliente = models.CharField(max_length=20, choices=TIPO_CLIENTE_CHOICES, default='regular')

    def __str__(self):
        return self.nome
    
class Compra(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    data_compra = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Compra {self.id} - {self.fornecedor.nome}"
    
class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()

    def __str__(self):
        return self.nome
    
class ProdutoIngrediente(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    quantidade_usada = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade} de {self.ingrediente.nome} para {self.produto.nome}"

class Pedido(models.Model):
    STATUS_PEDIDO_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_preparo', 'Em Preparo'),
        ('pronto', 'Pronto'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_PEDIDO_CHOICES, default='pendente')
    observacoes = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nome}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} para Pedido {self.pedido.id}"
    
class Pagamento(models.Model):
    TIPO_PAGAMENTO_CHOICES = [
        ('dinheiro', 'Dinheiro'),
        ('cartao_credito', 'Cartão de Crédito'),
        ('cartao_debito', 'Cartão de Débito'),
        ('pix', 'PIX'),
    ]
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    tipo_pagamento = models.CharField(max_length=20, choices=TIPO_PAGAMENTO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pagamento {self.id} para Pedido {self.pedido.id}"