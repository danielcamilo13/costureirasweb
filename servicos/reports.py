from .models import servicos
from cadastro.models import costureiras,colecao
# import django_filters

# class CostureiraFiltro(django_filters.FilterSet):

    # class Meta:
        # model = Servicos
        # fields = ['id','cod_pedido','nome_costureira','num_ordem','tipo_servico','quant1','data_saida']

    # def __init__(self, *args, **kwargs):
        # super(CostureiraFiltro, self).__init__(*args, **kwargs)
        # self.filters['tipo_servico'].extra.update(
            # {'empty_label': 'All products'})
            
    # data_entrada = models.DateField('Data Entrada',blank=True)
    # cliente = models.CharField(max_length=90,blank=True)
    # num_ficha = models.CharField(max_length=90,blank=True)
    # valor1 = models.CharField(max_length=90,blank=True)
    # total1 = models.CharField(max_length=90,blank=True)
    # obs = models.CharField(max_length=90,blank=True)
    # finalizado = models.CharField(max_length=90,blank=True)
    # colecao = models.CharField(max_length=90,blank=True)
    # desconto = models.CharField(max_length=90,blank=True)
    # quantidadedesconto = models.CharField(max_length=90,blank=True)
    # valorunitariodesconto = models.CharField(max_length=90,blank=True)
    # totaldesconto = models.CharField(max_length=90,blank=True)
            