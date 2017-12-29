from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class clientes(models.Model):
    codcliente = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=90,blank=True)
    email = models.CharField(max_length=90,blank=True)
    bairro = models.CharField(max_length=90,blank=True)
    cidade = models.CharField(max_length=90,blank=True)
    estado = models.CharField(max_length=90,blank=True)
    def __str__(self):
        return self.cliente
        
@python_2_unicode_compatible
class costureiras(models.Model):
    cod_costureira = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=90,blank=True)
    cpf = models.CharField(max_length=90,blank=True)
    endereco = models.CharField(max_length=90,blank=True)
    num = models.CharField(max_length=90,blank=True)
    complemento = models.CharField(max_length=90,blank=True)
    bairro = models.CharField(max_length=90,blank=True)
    cep = models.CharField(max_length=90,blank=True)
    cidade = models.CharField(max_length=90,blank=True)
    uf = models.CharField(max_length=90,blank=True)
    itinerario = models.CharField(max_length=90,blank=True)
    ddd1 = models.CharField(max_length=4,blank=True)
    fone1 = models.CharField(max_length=15,blank=True)
    ddd2 = models.CharField(max_length=4,blank=True)
    fone2 = models.CharField(max_length=15,blank=True)
    contato = models.CharField(max_length=90,blank=True)
    email = models.CharField(max_length=90,blank=True)
    banco = models.CharField(max_length=90,blank=True)
    tipoconta = models.CharField(max_length=90,blank=True)
    agencia = models.CharField(max_length=90,blank=True)
    numeroconta = models.CharField(max_length=90,blank=True)
    obs = models.CharField(max_length=90,blank=True)
    def __str__(self):
        return 'Nome: ' + self.nome +' CEP: ' +self.cep + ' Bairro: ' + self.bairro + ' Cidade: ' + self.cidade
    
@python_2_unicode_compatible
class colecao(models.Model):
    id = models.AutoField(primary_key=True,default=0)
    colecao = models.CharField(max_length=90)
    def __str__(self):
        return self.colecao 
