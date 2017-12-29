from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import datetime,tzinfo,timedelta

from django.utils import timezone

@python_2_unicode_compatible
class servicos(models.Model):
    id = models.IntegerField(default=0,unique=True,primary_key=True)
    cod_pedido = models.IntegerField(default=0,unique=False)
    nome_costureira = models.CharField(max_length=90)
    num_ordem = models.CharField(max_length=90)
    tipo_servico = models.CharField(max_length=90)
    quant1 = models.CharField(max_length=90)
    data_saida = models.DateTimeField('Data Saida')
    data_entrada = models.DateTimeField('Data Entrada')
    cliente = models.CharField(max_length=90)
    num_ficha = models.CharField(max_length=90)
    valor1 = models.CharField(max_length=90)
    total1 = models.CharField(max_length=90)
    obs = models.CharField(max_length=90)
    finalizado = models.CharField(max_length=90)
    colecao = models.CharField(max_length=90)
    desconto = models.CharField(max_length=90)
    quantidadedesconto = models.CharField(max_length=90)
    valorunitariodesconto = models.CharField(max_length=90)
    totaldesconto = models.CharField(max_length=90)
    def __str__(self):
        return 'Codigo: ' +str(self.id) + ' Tipo de Serviço: ' + str(self.tipo_servico)+' Data de Entrada: '+ str(self.data_entrada) + ' Data de Saida: ' + str(self.data_saida)
    def was_published_recently(self):
        return self.data_saida >= timezone.now() - datetime.timedelta(days=1)
