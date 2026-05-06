from django.contrib import admin

from .models import Carro, Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ativo']
    list_filter = ['ativo']
    search_fields = ['nome', 'descricao']


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'preco', 'estoque', 'ativo', 'criado_em']
    list_filter = ['categoria', 'ativo', 'criado_em']
    search_fields = ['nome', 'descricao']

admin.site.register(Carro)