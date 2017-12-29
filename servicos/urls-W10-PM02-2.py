from django.conf.urls import url
from .import views

app_name = 'servicos'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^detalhesservicos/$',views.detalhesservicos),
    url(r'^detalhescostureiras/$',views.detalhescostureiras),
    url(r'^pesquisar/$',views.pesquisar),
]
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # url(r'^detalhesservicos/$',views.detalhesservicos),
    # url(r'^$',views.servico1,name='servico1'),
    # url(r'^([a-z][A-Z][0-9]+)/detalhes/$',views.detalhes),
    # url(r'^servico1/$',views.servico1,name='servico1'),
    # url(r'^/$',views.detalhe,name='detalhe'),
    # url(r'^([a-z][A-Z][0-9]+)/$', views.detalhe, name='detalhe'),

