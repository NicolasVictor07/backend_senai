from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Personagem, AtorDublador, Obra, Habilidade, PersonagemHabilidades, Relacionamento
from .serializers import (PersonagemSerializer, AtorDubladorSerializer, ObraSerializer, 
                          HabilidadeSerializer, PersonagemHabilidadesSerializer, RelacionamentoSerializer)
from rest_framework import status

@api_view(['GET'])
def lista_personagens(request,id):
    try:
        personagens = Personagem.objects.get(pk=id)
    except Personagem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = PersonagemSerializer(personagens, many=True)
    


@api_view(['GET'])
def lista_atores_dubladores(request,id):
    atores_dubladores = AtorDublador.objects.get(pk=id)
    serializer = AtorDubladorSerializer(atores_dubladores, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def lista_obras(request,id):
    obras = Obra.objects.get(pk=id)
    serializer = ObraSerializer(obras, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def lista_habilidades(request,id):
    habilidades = Habilidade.objects.get(pk=id)
    serializer = HabilidadeSerializer(habilidades, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def lista_personagem_habilidades(request,id):   
    personagem_habilidades = PersonagemHabilidades.objects.get(pk=id)
    serializer = PersonagemHabilidadesSerializer(personagem_habilidades, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def lista_relacionamentos(request,id):
    relacionamentos = Relacionamento.objects.get(pk=id)
    serializer = RelacionamentoSerializer(relacionamentos, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])
def deletar_obra(request, id):
    try:
       obra = Obra.objects.get(pk=id)
    except Obra.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        obra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = ObraSerializer(obra)
        return Response(serializer.data)

@api_view(['GET', 'DELETE'])
def deletar_ator_dublador(request, id):
    try:
       ator_dublador = AtorDublador.objects.get(pk=id)
    except AtorDublador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        ator_dublador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = AtorDubladorSerializer(ator_dublador)
        return Response(serializer.data)

@api_view(['GET', 'DELETE'])
def deletar_personagem(request, id):
    try:
       personagem = Personagem.objects.get(pk=id)
    except Personagem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        personagem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = PersonagemSerializer(personagem)
        return Response(serializer.data)

@api_view(['GET', 'DELETE'])
def deletar_habilidade(request, id):
    try:
       habilidade = Habilidade.objects.get(pk=id)
    except Habilidade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        habilidade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = HabilidadeSerializer(habilidade)
        return Response(serializer.data)
    
@api_view(['GET', 'DELETE'])
def deletar_personagem_habilidades(request, id):
    try:
       personagem_habilidades = PersonagemHabilidades.objects.get(pk=id)
    except PersonagemHabilidades.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        personagem_habilidades.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = PersonagemHabilidadesSerializer(personagem_habilidades)
        return Response(serializer.data)
    
@api_view(['GET', 'DELETE'])
def deletar_relacionamento(request, id):
    try:
       relacionamento = Relacionamento.objects.get(pk=id)
    except Relacionamento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        relacionamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = RelacionamentoSerializer(relacionamento)
        return Response(serializer.data)

