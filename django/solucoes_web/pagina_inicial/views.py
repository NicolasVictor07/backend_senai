from django.shortcuts import render
from django.http import HttpResponse

def saudacao(request):
    return HttpResponse("<h1>Olá, seja bem-vindo ao site Soluções Web!</h1>")


def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')
