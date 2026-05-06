"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from ecommerce.views import (
    categoria_cadastro,
    categoria_excluir,
    home,
    produto_cadastro,
    produto_excluir,
    carro_cadastro,
    carro_excluir
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('', home, name='home'),
    path('produtos/cadastrar/', produto_cadastro, name='produto_cadastro'),
    path('produtos/<int:produto_id>/excluir/', produto_excluir, name='produto_excluir'),
    path('categorias/cadastrar/', categoria_cadastro, name='categoria_cadastro'),
    path('categorias/<int:categoria_id>/excluir/', categoria_excluir, name='categoria_excluir'),
    path('carro/cadastrar/', carro_cadastro, name='carro_cadastro'),
    path('carro/<int:carro_id>/excluir/', carro_excluir, name='carro_excluir'),
]
