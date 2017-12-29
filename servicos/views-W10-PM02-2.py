# -*- coding: latin-1 -*-
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from .models import servicos
from cadastro.models import costureiras
from django.conf.urls.static import static
# from django.urls import reverse
from django.core.urlresolvers import reverse
import re
from django.contrib import admin

def index(request):
    admin.site.site_title="Costureiras WEB"
    admin.site.site_header="Costureiras WEB"
    contexto = {'vazio':'vazio'}
    templ = loader.get_template('servicos/index.html')
    return HttpResponse(templ.render(contexto,request))

def detalhesservicos(request):
    req = request.get_full_path()
    if re.search('costureira',req):
        todos_servicos = costureiras.objects.order_by('-nome')
    elif re.search('itinerario',req):
        print('resultado %s'%req)
    elif re.search('servico',req):
        todos_servicos = servicos.objects.order_by('-data_saida')
    context = {'todos_servicos':todos_servicos,}
    templ = loader.get_template('servicos/detalhes-servicos.html')
    return HttpResponse(templ.render(context,request))
    
def detalhescostureiras(request):
    todos_servicos = servicos.objects.order_by('-nome')
    context = {'todos_servicos':todos_servicos,}
    templ = loader.get_template('servicos/detalhes-costureiras.html')
    return HttpResponseRedirect(reverse('servicos:detalhes'))
    # (templ.render(context,request))
    
def pesquisar(request):
    templ = loader.get_template('servicos/pesquisa.html')
    if request.method=='GET':
        search_query = request.GET.get('pesquisar_txt', None)
    return HttpResponse(templ.render(request))