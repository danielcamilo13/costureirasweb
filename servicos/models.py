from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from datetime import datetime,tzinfo,timedelta,timezone
from django import forms
from cadastro.models import costureira,cliente,tipo_servico

from django.utils import timezone

@python_2_unicode_compatible
class servicos(models.Model):
    id = models.AutoField(primary_key=True)
    cod_pedido = models.IntegerField(default=0,unique=False,blank=True)
    nome_costureira = models.ForeignKey(costureira,on_delete=models.CASCADE,blank=True)
    num_ordem = models.CharField(max_length=90,blank=True,verbose_name='Ordem')
    tipo_servico = models.ForeignKey(tipo_servico,on_delete=models.CASCADE,max_length=40,blank=True)
    quant1 = models.CharField(max_length=90,blank=True)
    dt_saida = models.DateField(blank=True,verbose_name='Data de Saída')
    dt_entrada = models.DateField(blank=True,verbose_name='Data de Entrada')
    cliente = models.ForeignKey(cliente,on_delete=models.CASCADE,max_length=90,blank=True)
    num_ficha = models.IntegerField(blank=True,default=0)
    valor1 = models.DecimalField(max_digits=5,decimal_places=2,blank=True)
    total1 = models.DecimalField(max_digits=5,decimal_places=2,blank=True)
    obs = models.CharField(max_length=90,blank=True)
    finalizado = models.BooleanField(blank=True)
    colecao = models.CharField(max_length=90,blank=True)
    faturado = models.BooleanField(blank=True)
    dt_faturado = models.DateField(blank=True,verbose_name='Faturado Mês')
    def __str__(self):
        return 'Código do Pedido: ' +str(self.cod_pedido) +' Data Entrada: '+ str(self.dt_entrada) + ' Data Saida: ' + str(self.dt_saida)
    def faturadoreview(self):
        return self.faturado
    def entrada(self):
        self.dt_entrada = datetime.now()

class servico(servicos):
    class Meta:
        proxy = True
        
class servicosReview(servicos):
    class Meta:
        proxy=True
    def save(self,*args,**kwargs):
        self.servicos = servicos.objects.get(cod_pedido='1')
        super(servicosReview,self).save(*args,**kwargs)
        
class faturamento(servicos):
    class Meta:
        proxy=True