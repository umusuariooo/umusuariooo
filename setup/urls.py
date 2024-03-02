from django.contrib import admin
from django.urls import path

from cliente import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('listar', views.listar, name='listar')
]