from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class clientes(models.Model):
    codcliente = models.IntegerField(primary_key=True)
    cliente = models.CharField(max_length=90)
    def __str__(self):
        return self.cliente
        
@python_2_unicode_compatible
class costureiras(models.Model):
    cod_costureira = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=90)
    cpf = models.CharField(max_length=90)
    endereco = models.CharField(max_length=90)
    num = models.CharField(max_length=90)
    complemento = models.CharField(max_length=90)
    bairro = models.CharField(max_length=90)
    cep = models.CharField(max_length=90)
    cidade = models.CharField(max_length=90)
    uf = models.CharField(max_length=90)
    itinerario = models.CharField(max_length=90)
    ddd1 = models.CharField(max_length=90)
    fone1 = models.CharField(max_length=90)
    ddd2 = models.CharField(max_length=90)
    fone2 = models.CharField(max_length=90)
    contato = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    banco = models.CharField(max_length=90)
    tipoconta = models.CharField(max_length=90)
    agencia = models.CharField(max_length=90)
    numeroconta = models.CharField(max_length=90)
    obs = models.CharField(max_length=90)
    def __str__(self):
        return 'Nome: ' + self.nome +' CEP: ' +self.cep + ' Bairro: ' + self.bairro + ' Cidade: ' + self.cidade
    
@python_2_unicode_compatible
class colecao(models.Model):
    colecao = models.CharField(max_length=90,primary_key=True)
    def __str__(self):
        return self.colecao
