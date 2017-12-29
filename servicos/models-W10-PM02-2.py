from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import datetime,tzinfo,timedelta

from django.utils import timezone

@python_2_unicode_compatible
class servicos(models.Model):
    id = models.AutoField(primary_key=True)
    cod_pedido = models.IntegerField(default=0,unique=False)
    nome_costureira = models.CharField(max_length=90,blank=True)
    num_ordem = models.CharField(max_length=90,blank=True)
    tipo_servico = models.CharField(max_length=90,blank=True)
    quant1 = models.CharField(max_length=90,blank=True)
    data_saida = models.DateField('Data Saida',blank=True)
    data_entrada = models.DateField('Data Entrada',blank=True)
    cliente = models.CharField(max_length=90,blank=True)
    num_ficha = models.CharField(max_length=90,blank=True)
    valor1 = models.CharField(max_length=90,blank=True)
    total1 = models.CharField(max_length=90,blank=True)
    obs = models.CharField(max_length=90,blank=True)
    finalizado = models.CharField(max_length=90,blank=True)
    colecao = models.CharField(max_length=90,blank=True)
    desconto = models.CharField(max_length=90,blank=True)
    quantidadedesconto = models.CharField(max_length=90,blank=True)
    valorunitariodesconto = models.CharField(max_length=90,blank=True)
    totaldesconto = models.CharField(max_length=90,blank=True)
    def __str__(self):
        return 'Codigo: ' +str(self.id) + ' Tipo de Serviço: ' + str(self.tipo_servico)+' Data de Entrada: '+ str(self.data_entrada) + ' Data de Saida: ' + str(self.data_saida)
    def was_published_recently(self):
        return self.data_saida >= timezone.now() - datetime.timedelta(days=1)
