from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import datetime,tzinfo,timedelta
from django import forms
from cadastro.models import costureira,cliente,tipo_servico
from django.forms.widgets import CheckboxSelectMultiple
from django.forms.models import ModelForm

from django.utils import timezone

@python_2_unicode_compatible
class servicos(models.Model):
    id = models.AutoField(primary_key=True)
    cod_pedido = models.IntegerField(default=0,unique=False)
    nome_costureira = models.ForeignKey(costureira,on_delete=models.CASCADE,blank=True)
    num_ordem = models.CharField(max_length=90,blank=True)
    tipo_servico = models.ForeignKey(tipo_servico,on_delete=models.CASCADE,max_length=40,blank=True,default=0)
    quant1 = models.CharField(max_length=90,blank=True)
    dt_saida = models.DateField(blank=True)
    dt_entrada = models.DateField(blank=True)
    cliente = models.ForeignKey(cliente,on_delete=models.CASCADE,max_length=90,blank=True)
    num_ficha = models.IntegerField(blank=True)
    valor1 = models.DecimalField(max_digits=5,decimal_places=2,blank=True)
    total1 = models.DecimalField(max_digits=5,decimal_places=2,blank=True)
    obs = models.CharField(max_length=90,blank=True)
    finalizado = models.CharField(max_length=90,blank=True)
    colecao = models.CharField(max_length=90,blank=True)
    desconto = models.DecimalField(max_digits=5,decimal_places=2,blank=True)
    quantidadedesconto = models.DecimalField(max_digits=5,decimal_places=2,blank=True)
    valorunitariodesconto = models.DecimalField(max_digits=5,decimal_places=2,blank=True)
    totaldesconto = models.DecimalField(max_digits=5,decimal_places=2,blank=True)
        
    def __str__(self):
        return 'Código do Pedido: ' +str(self.cod_pedido) + ' Costureira: ' + str(self.nome_costureira) +' Data Entrada: '+ str(self.dt_entrada) + ' Data Saida: ' + str(self.dt_saida) + ' Total de Desconto' + str(self.totaldesconto)
    def sumDesconto(self):
        return self.quantidadedesconto * self.valorunitariodesconto
    
    descontocalculado = property(sumDesconto)
    # def was_published_recently(self):
        # return self.dt_saida >= timezone.now() - datetime.timedelta(days=1)

