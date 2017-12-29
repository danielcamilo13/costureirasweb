from django.contrib import admin
from .models import servico,servicos, servicosReview,faturamento
from cadastro.models import abatimento,costureira
from django import forms

class faturamentoReview(admin.ModelAdmin):
    # list_display=('dt_saida','nome_costureira','faturado','dt_faturado','faturadoreview')
    list_display=('dt_saida','num_ordem','faturado','dt_faturado','faturadoreview')
    ordering = ('dt_faturado','num_ordem')
    search_fields = ('dt_faturado',)
    list_filter = ('dt_faturado',)
    
class servicosAdmin(admin.ModelAdmin):
    fieldsets = (
    (None,{
    'fields':(
    'tipo_servico','nome_costureira','cod_pedido','num_ordem','cliente','dt_entrada','dt_saida','finalizado')
    }),
    ('Advanced options', {
    'classes':('collapse',),
    'fields':('num_ficha','quant1','valor1','total1','colecao','obs','faturado','dt_faturado'),
    }),
    )
    ordering = ('-num_ordem',)
    search_fields=('cod_pedido','num_ordem','dt_entrada')

class servicosReviewList(admin.ModelAdmin):
    lista_display=('nome_costureira','cod_pedido','num_ordem','tipo_servico','cliente','dt_entrada','dt_saida','finalizado')
    
    ordering=('cod_pedido',)
    # pass
    # def queryset(self,request):
        # return self.model.objects.filter(servicos__cod_pedido='1')
        
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

admin.site.register(servico,servicosAdmin)
admin.site.register(faturamento,faturamentoReview)
admin.site.register(servicosReview,servicosReviewList)
admin.site.register(abatimento)
