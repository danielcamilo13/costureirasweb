# -*- coding: latin-1 -*-
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from .models import servicos
from cadastro.models import costureira
from django.conf.urls.static import static
# from django.conf.urls import reverse
from django.core.urlresolvers import reverse
import re
from django.contrib import admin

def index(request):
    templ = loader.get_template('servicos/index.html')
    req = request.get_full_path()
    if re.search('costureira',req):
        todos_servicos = costureira.objects.order_by('-nome')
        context = {'todos_servicos':todos_servicos,}
    elif re.search('itinerario',req):
        print('resultado %s'%req)
        todos_servicos = costureira.objects.order_by('-itinerario')
        context = {'todos_servicos':todos_servicos,}
    elif re.search('tipo',req):
        todos_servicos = servicos.objects.order_by('-dt_saida')
        context = {'todos_servicos':todos_servicos,}
    else:
        todos_servicos='N'
        context = {'todos_servicos':todos_servicos,}
    search_query = request.GET.get('txt_pesquisar',None)
    if search_query != None:
        todos_servicos = servicos.objects.filter(tipo_servico=search_query)
        context = {'todos_servicos':todos_servicos,}

    return HttpResponse(templ.render(context,request))
    
def detalhesservicos(request):
    req = request.get_full_path()
    if re.search('costureira',req):
        todos_servicos = costureira.objects.order_by('-nome')
    elif re.search('itinerario',req):
        print('resultado %s'%req)
    elif re.search('servico',req):
        todos_servicos = servicos.objects.order_by('-data_saida')
    context = {'todos_servicos':todos_servicos,}
    templ = loader.get_template('servicos/index.html')
    return HttpResponse(templ.render(context,request))

def detalhes(request):
    templ = loader.get_template('servicos/detalhes.html')
    req = request.get_full_path()
    todos_servicos = costureira.objects.order_by('-nome')
    # if re.search('costureira',req):
        # todos_servicos = costureira.objects.order_by('-nome')
    # elif re.search('itinerario',req):
        # print('resultado %s'%req)
    # elif re.search('servico',req):
        # todos_servicos = servicos.objects.order_by('-data_saida')
    context = {'todos_servicos':todos_servicos,}
    # return HttpResponse(templ.render(context,request))
    print('Nome de retorno %s'%request)
    return HttpResponse(templ.render(context,request))
    
def detalhescostureiras(request):
    todos_servicos = servicos.objects.order_by('-nome')
    context = {'todos_servicos':todos_servicos,}
    templ = loader.get_template('servicos/detalhes-costureira.html')
    return HttpResponseRedirect(reverse('servicos:detalhes'))
    
def pesquisar(request):
    templ = loader.get_template('servicos/pesquisa.html')
    # filter = CostureiraFiltro(request.GET,queryset=servicos.objects.all())
    if request.method=='GET':
        # search_query = request.GET.get('pesquisar_txt', None)
        search_query = request.GET.get('txt_pesquisar',None)
        print('results %s'%search_query)
        # todos_servicos = servicos.objects.filter(tipo_servico=search_query)
        todos_servicos = servicos.objects.filter(tipo_servico=search_query)
        context={'todos_servicos':todos_servicos,}
    else:
        print('Metodo NAO GET')
    return HttpResponse(templ.render(context,request))