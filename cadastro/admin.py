from django.contrib import admin
from .models import colecao,cliente,costureira,itinerario,tipo_servico,cidade,estado,tipo_desconto

class lista_cliente(admin.ModelAdmin):
    lista_display = ('cliente','email','bairro','cidade','estado')
    ordering = ('cliente',)
    search_fields = ('cliente','email')
    
class lista_costureira(admin.ModelAdmin):
    lista_display = ('nome','bairro','fone1')
    ordering = ('nome',)
    search_fields = ('nome',)

class lista_colecao(admin.ModelAdmin):
    lista_display = ('colecao','descricao')
    ordering = ('colecao',)
    search_fields = ('colecao',)
    
class lista_itinerario(admin.ModelAdmin):
    lista_display = ('nr_itinerario,ds_itinerario')
    ordering = ('nr_itinerario',)
    search_fields = ('ds_itinerario',)

class lista_tipo_servico(admin.ModelAdmin):
    lista_display = ('id','tipo_servico')
    ordering = ('tipo_servico',)
    search_fields = ('tipo_servico',)
    
class lista_cidade(admin.ModelAdmin):
    lista_display = ('id','nm_cidade')
    ordering = ('nm_cidade',)
    search_fields = ('nm_cidade',)

class lista_estado(admin.ModelAdmin):
    lista_display = ('id','nm_estado')
    ordering = ('nm_estado',)
    
admin.site.register(colecao,lista_colecao)
admin.site.register(cliente,lista_cliente)
admin.site.register(costureira,lista_costureira)
admin.site.register(itinerario,lista_itinerario)
admin.site.register(tipo_servico,lista_tipo_servico)
admin.site.register(cidade,lista_cidade)
admin.site.register(estado,lista_estado)
admin.site.register(tipo_desconto)
