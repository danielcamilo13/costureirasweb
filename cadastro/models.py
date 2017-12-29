from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import format_html
from django.contrib import admin
from datetime import datetime,timezone

@python_2_unicode_compatible
class itinerario(models.Model):
    id = models.AutoField(primary_key=True)
    nr_itinerario = models.IntegerField(unique=False)
    ds_itinerario = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return str(self.nr_itinerario) + ' Descrição: ' +self.ds_itinerario

@python_2_unicode_compatible
class cidade(models.Model):
    id = models.AutoField(primary_key=True)
    nm_cidade = models.CharField(max_length=50,blank=True,verbose_name="Cidade")
    def __str__(self):
        return self.nm_cidade

@python_2_unicode_compatible
class estado(models.Model):
    id = models.AutoField(primary_key=True)
    nm_estado = models.CharField(max_length=50,blank=True,verbose_name="Estado")
    def __str__(self):
        return self.nm_estado

@python_2_unicode_compatible
class colecao(models.Model):
    id = models.AutoField(primary_key=True)
    colecao = models.CharField(max_length=90)
    descricao = models.CharField(max_length=30,blank=True)
    def __str__(self):
        return self.colecao +' '+ self.descricao

@python_2_unicode_compatible
class tipo_servico(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_servico = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.tipo_servico
        
@python_2_unicode_compatible
class tipo_desconto(models.Model):
    id = models.AutoField(primary_key=True)
    ds_desconto = models.CharField(max_length=50)
    def __str__(self):
        return self.ds_desconto
    
@python_2_unicode_compatible
class cliente(models.Model):
    codcliente = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=90,blank=True)
    email = models.EmailField(max_length=90,blank=True)
    bairro = models.CharField(max_length=90,blank=True)
    cidade = models.CharField(max_length=90,blank=True)
    estado = models.CharField(max_length=90,blank=True)
    def __str__(self):
        return self.cliente +' Email: ' +self.email
        
@python_2_unicode_compatible
class costureira(models.Model):
    cod_costureira = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=90,blank=True)
    cpf = models.CharField(max_length=90,blank=True)
    endereco = models.CharField(max_length=90,blank=True)
    num = models.CharField(max_length=90,blank=True)
    complemento = models.CharField(max_length=90,blank=True)
    bairro = models.CharField(max_length=90,blank=True)
    cep = models.CharField(max_length=90,blank=True)
    cidade = models.ForeignKey(cidade,on_delete=models.CASCADE,max_length=30,blank=True)
    estado = models.ForeignKey(estado,on_delete=models.CASCADE,max_length=30,blank=True,default=0)
    rota = models.ForeignKey(itinerario,on_delete=models.CASCADE,max_length=20,blank=True)
    ddd1 = models.CharField(max_length=4,blank=True,verbose_name="DDD")
    fone1 = models.CharField(max_length=15,blank=True, verbose_name="Telefone Principal")
    ddd2 = models.CharField(max_length=4,blank=True, verbose_name="DDD")
    fone2 = models.CharField(max_length=15,blank=True,verbose_name="Tefone de apoio")
    contato = models.CharField(max_length=90,blank=True)
    email = models.EmailField(max_length=90,blank=True)
    banco = models.CharField(max_length=90,blank=True)
    tipoconta = models.CharField(max_length=90,blank=True)
    agencia = models.CharField(max_length=90,blank=True)
    numeroconta = models.CharField(max_length=90,blank=True,verbose_name="Número da conta")
    status=models.CharField(max_length=25,blank=True)
    obs = models.CharField(max_length=90,blank=True)
    def __str__(self):
        return self.nome +' Telefone: ' + self.fone1 

@python_2_unicode_compatible
class abatimento(models.Model):
    id = models.AutoField(primary_key=True)
    nm_costureira = models.ForeignKey(costureira,on_delete=models.CASCADE,max_length=40,blank=True)
    desconto = models.ForeignKey(tipo_desconto,on_delete=models.CASCADE,max_length=40)
    ds_desconto = models.CharField(max_length=90,blank=True)
    dt_entrada = models.DateField(blank=True)
    dt_saida = models.DateField(blank=True)
    qte_desconto = models.IntegerField(default=0,blank=True)
    vr_unitario_desconto = models.DecimalField(max_digits=5,decimal_places=2,blank=True)
    total_desconto = models.DecimalField(max_digits=5,decimal_places=2,blank=True)
    finalizado = models.BooleanField(blank=True)
    faturado = models.BooleanField(blank=True)
    dt_faturado = models.DateField(blank=True)
    def __str__(self):
        return 'Costureira: '+str(self.nm_costureira)+ ' - Desconto: ' + str(self.desconto) + ' Data de Entrada: ' + str(self.dt_entrada)
    def sumDesconto(self):
        return self.qte_desconto * self.vr_unitario_desconto
    total_desconto = property(sumDesconto)
    
