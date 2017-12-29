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

def index(request):
    contexto = {'vazio':'vazio'}
    templ = loader.get_template('servicos/index.html')
    return HttpResponse(templ.render(contexto,request))

def detalhesservicos(request):
    req = request.get_full_path()
    if re.search('costureira',req):
        print('resultado %s'%req)
    elif re.search('itinerario',req):
        print('resultado %s'%req)
    elif re.search('servico',req):
        print('resultado %s'%req)
    put = FirstForm(form.request)
    if form.is_valid():
        q = form.cleaned_data['qry']
        print('q')
    todos_servicos = servicos.objects.order_by('-data_saida')
    # context = {'todos_servicos':todos_servicos,}
    context = {'todos_servicos':'temporario',}
    templ = loader.get_template('servicos/detalhes-servicos.html')
    return HttpResponse(templ.render(context,request))
    
def detalhescostureiras(request):
    todos_servicos = servicos.objects.order_by('-nome')
    context = {'todos_servicos':todos_servicos,}
    templ = loader.get_template('servicos/detalhes-costureiras.html')
    return HttpResponseRedirect(reverse('servicos:detalhes'))
    # (templ.render(context,request))