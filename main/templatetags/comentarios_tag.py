from django import template
from core import models

#Carrega o registro de template tags
register = template.Library()

#Registra o metodo a seguir como uma inclusion_tag indicando o template a ser renderizad
@register.inclusion_tag('comentarios_n_liberados.html')
def comentarios_n_liberados():
    comentarios = 'teste'
    # comentarios = models.comentario.objects.filter(liberado=False).order_by('data')[0:5]
    return { 'comentarios' : comentarios }