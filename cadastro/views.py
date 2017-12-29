from django.shortcuts import render
from .models import colecao,cliente,costureira

def index(request):
    return 'cadastro'