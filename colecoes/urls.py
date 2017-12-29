from django.conf.urls import url
from .import views

app_name='colecoes'
urlpatterns = [
url(r'^$',views.index,name='index'),
]