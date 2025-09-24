from django.shortcuts import render
from django.http import HttpResponse

def saudacao(request):
    return HttpResponse("<h1>Olá, seja bem-vindo ao site Soluções Web!</h1>")