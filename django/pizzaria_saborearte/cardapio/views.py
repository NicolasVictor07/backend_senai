from django.shortcuts import render
from django.http import HttpResponse

def pizza_do_dia(request):
    return HttpResponse(" A pizza do dia é: Calabresa com queijo extra!")

def promocoes(request):
    return HttpResponse(" Promoção de hoje: Compre 2, leve 3!")
