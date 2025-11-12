from .models import Item
from .serializers import ItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status # Para códigos de status HTTP

@api_view(['GET', 'POST'])
def item_list(request):
    """
    Lista todos os itens (GET) ou cria um novo item (POST).
    """
    if request.method == 'GET':
        # GET: Lista todos os itens
        itens = Item.objects.all()
        serializer = ItemSerializer(itens, many=True) # many=True para serializar uma lista
        return Response(serializer.data)

    elif request.method == 'POST':
        # POST: Cria um novo item
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Retorna o item criado com status 201 (Created)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Retorna erros com status 400 (Bad Request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)