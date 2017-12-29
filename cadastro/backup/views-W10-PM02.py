from django.shortcuts import render
from .models import colecoes,clientes,costureiras

def index(request):
    return 'cadastro'