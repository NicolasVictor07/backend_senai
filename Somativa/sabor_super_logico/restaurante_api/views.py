from rest_framework.response import Response
from .models import Fornecedor, Categoria, Ingrediente, Funcionario, Mesa, Cliente, Compra, Produto, ProdutoIngrediente, Pedido, ItemPedido, Pagamento
from .serializers import FornecedorSerializer, CategoriaSerializer, IngredienteSerializer, FuncionarioSerializer, MesaSerializer, ClienteSerializer, CompraSerializer, ProdutoSerializer, ProdutoIngredienteSerializer, PedidoSerializer, ItemPedidoSerializer, PagamentoSerializer
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET', 'POST'])
def Cliente_listarCriar(request):
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return (serializer.data)

    elif request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Cliente criado!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE','PATCH'])
def Listar_Atualizar_Deletar_Cliente(request, id):
    try:
        cliente = Cliente.objects.get(pk=id)
    except Cliente.DoesNotExist:
        return Response({"erro":"cliente não encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Cliente Atualizado!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = ClienteSerializer(cliente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Cliente Atualizado!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cliente.delete()
        return Response({"Cliente Deletado!"},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def Funcionario_listarCriar(request):
    if request.method == 'GET':
        funcionarios = Funcionario.objects.all()
        serializer = FuncionarioSerializer(funcionarios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FuncionarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Funcionario criado!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE','PATCH'])
def Listar_Atualizar_Deletar_Funcionario(request, id):
    try:
        funcionario = Funcionario.objects.get(pk=id)
    except Funcionario.DoesNotExist:
        return Response({"erro":"funcionario não encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FuncionarioSerializer(funcionario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FuncionarioSerializer(funcionario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Funcionario Atualizado!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = FuncionarioSerializer(funcionario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Funcionario Atualizado!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        funcionario.delete()
        return Response({"Funcionario Deletado!"},status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def Categoria_listarCriar(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Categoria criada!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE','PATCH'])
def Listar_Atualizar_Deletar_Categoria(request, id):
    try:
        categoria = Categoria.objects.get(pk=id)
    except Categoria.DoesNotExist:
        return Response({"erro":"categoria não encontrada"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Categoria Atualizada!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = CategoriaSerializer(categoria, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Categoria Atualizada!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        categoria.delete()
        return Response({"Categoria Deletada!"},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def Produto_listarCriar(request):
    if request.method == 'GET':
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Produto criado!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE','PATCH'])
def Listar_Atualizar_Deletar_Produto(request, id):
    try:
        produto = Produto.objects.get(pk=id)
    except Produto.DoesNotExist:
        return Response({"erro":"produto não encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Produto Atualizado!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = ProdutoSerializer(produto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Produto Atualizado!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        produto.delete()
        return Response({"Produto Deletado!"},status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def Ingrediente_listarCriar(request):
    if request.method == 'GET':
        ingredientes = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingredientes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Ingrediente criado!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE','PATCH'])
def Listar_Atualizar_Deletar_Ingrediente(request, id):
    try:
        ingrediente = Ingrediente.objects.get(pk=id)
    except Ingrediente.DoesNotExist:
        return Response({"erro":"ingrediente não encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IngredienteSerializer(ingrediente)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = IngredienteSerializer(ingrediente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Ingrediente Atualizado!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = IngredienteSerializer(ingrediente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Ingrediente Atualizado!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ingrediente.delete()
        return Response({"Ingrediente Deletado!"},status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def Mesa_listarCriar(request):
    if request.method == 'GET':
        mesas = Mesa.objects.all()
        serializer = MesaSerializer(mesas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MesaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Mesa criada!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE','PATCH'])
def Listar_Atualizar_Deletar_Mesa(request, id):
    try:
        mesa = Mesa.objects.get(pk=id)
    except Mesa.DoesNotExist:
        return Response({"erro":"mesa não encontrada"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MesaSerializer(mesa)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MesaSerializer(mesa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mesa Atualizada!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = MesaSerializer(mesa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mesa Atualizada!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        mesa.delete()
        return Response({"Mesa Deletada!"},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def Pedido_listarCriar(request):
    if request.method == 'GET':
        pedidos = Pedido.objects.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Pedido criado!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE','PATCH'])
def Listar_Atualizar_Deletar_Pedido(request, id):
    try:
        pedido = Pedido.objects.get(pk=id)
    except Pedido.DoesNotExist:
        return Response({"erro":"pedido não encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PedidoSerializer(pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Pedido Atualizado!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = PedidoSerializer(pedido, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Pedido Atualizado!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pedido.delete()
        return Response({"Pedido Deletado!"},status=status.HTTP_204_NO_CONTENT)
        
    
@api_view(['GET', 'POST'])
def ItemPedido_listarCriar(request):
    if request.method == 'GET':
        itens_pedido = ItemPedido.objects.all()
        serializer = ItemPedidoSerializer(itens_pedido, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ItemPedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Item do Pedido criado!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE','PATCH'])
def Listar_Atualizar_Deletar_ItemPedido(request, id):
    try:
        item_pedido = ItemPedido.objects.get(pk=id)
    except ItemPedido.DoesNotExist:
        return Response({"erro":"item do pedido não encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemPedidoSerializer(item_pedido)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ItemPedidoSerializer(item_pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Item do Pedido Atualizado!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = ItemPedidoSerializer(item_pedido, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Item do Pedido Atualizado!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item_pedido.delete()
        return Response({"Item do Pedido Deletado!"},status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def Pagamento_listarCriar(request):
    if request.method == 'GET':
        pagamentos = Pagamento.objects.all()
        serializer = PagamentoSerializer(pagamentos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PagamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Pagamento criado!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE','PATCH'])
def Listar_Atualizar_Deletar_Pagamento(request, id):
    try:
        pagamento = Pagamento.objects.get(pk=id)
    except Pagamento.DoesNotExist:
        return Response({"erro":"pagamento não encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PagamentoSerializer(pagamento)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PagamentoSerializer(pagamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Pagamento Atualizado!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = PagamentoSerializer(pagamento, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Pagamento Atualizado!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pagamento.delete()
        return Response({"Pagamento Deletado!"},status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def Fornecedor_listarCriar(request):
    if request.method == 'GET':
        fornecedores = Fornecedor.objects.all()
        serializer = FornecedorSerializer(fornecedores, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FornecedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Fornecedor criado!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE','PATCH'])
def Listar_Atualizar_Deletar_Fornecedor(request, id):
    try:
        fornecedor = Fornecedor.objects.get(pk=id)
    except Fornecedor.DoesNotExist:
        return Response({"erro":"fornecedor não encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FornecedorSerializer(fornecedor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FornecedorSerializer(fornecedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Fornecedor Atualizado!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = FornecedorSerializer(fornecedor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Fornecedor Atualizado!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        fornecedor.delete()
        return Response({"Fornecedor Deletado!"},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def Compra_listarCriar(request):
    if request.method == 'GET':
        compras = Compra.objects.all()
        serializer = CompraSerializer(compras, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CompraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Compra criada!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE','PATCH'])
def Listar_Atualizar_Deletar_Compra(request, id):
    try:
        compra = Compra.objects.get(pk=id)
    except Compra.DoesNotExist:
        return Response({"erro":"compra não encontrada"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompraSerializer(compra)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompraSerializer(compra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Compra Atualizada!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = CompraSerializer(compra, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Compra Atualizada!"},serializer.data)
        return Response({"formato invalido"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        compra.delete()
        return Response({"Compra Deletada!"},status=status.HTTP_204_NO_CONTENT)

#FIM DO CODIGO 