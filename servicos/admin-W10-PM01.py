from django.contrib import admin
from .models import servicos
from cadastro.models import abatimento
from django import forms

class servico(servicos):
    class Meta:
        proxy = True

class servicoForm(forms.Form):
    finalizado = forms.Charfield(widget = forms.CheckboxInput)

class lista_servicos(admin.ModelAdmin):
    fieldsets = (
    (None,{
    'fields':(
    'nome_costureira','cod_pedido','num_ordem','tipo_servico','cliente','dt_entrada','dt_saida','finalizado')
    }),
    ('Advanced options', {
    'classes':('collapse',),
    'fields':('num_ficha','quant1','valor1','total1','desconto','quantidadedesconto','valorunitariodesconto','totaldesconto','colecao','obs'),
    }),
    )
    ordering = ('-num_ordem',)
    search_fields=('cod_pedido',)

       
class lista_abatimento(admin.ModelAdmin):
    # fieldsets = (
    # (None,
    # {'fields':
    # ('nome_costureira','desconto','dt_saida','dt_entrada','quantidadedesconto')
    # }),
    # ('Advanced options',{
    # 'classes':('collapse',),
    # 'fields':('valorunitariodesconto','quantidadedesconto * valorunitariodesconto','finalizado'),
    # }),
    # )
    # ordering = ('-num_ordem',)
    search_fields = ('cod_pedido',)

admin.site.register(servico,lista_servicos)
admin.site.register(abatimento,lista_abatimento)