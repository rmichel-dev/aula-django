from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CarroForm, CategoriaForm, ProdutoForm
from .models import Carro, Categoria, Produto


# Create your views here.
def home(request):
    return render(request, 'ecommerce/home.html')


# Autenticacao: login_required exige apenas que o usuario esteja logado.
@login_required(login_url='/admin/login/')
# Autorizacao: permission_required verifica se o usuario tem a permissao marcada no admin.
# raise_exception=True mostra erro 403 quando o usuario esta logado, mas nao tem permissao.
@permission_required('ecommerce.add_produto', raise_exception=True)
def produto_cadastro(request):
    # Quando o formulario e enviado, o navegador faz uma requisicao POST.
    if request.method == 'POST':
        # request.POST contem os dados digitados pelo usuario no formulario.
        form = ProdutoForm(request.POST)

        # is_valid() verifica se os dados seguem as regras do ModelForm e da model.
        if form.is_valid():
            # save() cria e grava um novo produto no banco de dados.
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso.')

            # Redireciona para evitar reenviar o formulario ao atualizar a pagina.
            return redirect('produto_cadastro')
    else:
        # Quando a pagina e aberta pela primeira vez, criamos um formulario vazio.
        form = ProdutoForm()

    # Busca todos os produtos cadastrados para mostrar na tabela do template.
    produtos = Produto.objects.all()

    # Envia o formulario e a lista de produtos para o arquivo HTML.
    return render(request, 'ecommerce/produto_cadastro.html', {'form': form, 'produtos': produtos})


# Autorizacao: somente usuarios com a permissao "Can delete produto" podem excluir.
@login_required(login_url='/admin/login/')
# raise_exception=True mostra erro 403 quando o usuario esta logado, mas nao tem permissao.
@permission_required('ecommerce.delete_produto', raise_exception=True)
def produto_excluir(request, produto_id):
    # Busca o produto pelo id. Se nao existir, o Django retorna erro 404.
    produto = get_object_or_404(Produto, id=produto_id)

    # Por seguranca, a exclusao deve acontecer apenas via POST.
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto excluido com sucesso.')

    return redirect('produto_cadastro')


# Autenticacao: login_required exige apenas que o usuario esteja logado.
@login_required(login_url='/admin/login/')
# Autorizacao: permission_required verifica se o usuario tem a permissao marcada no admin.
# raise_exception=True mostra erro 403 quando o usuario esta logado, mas nao tem permissao.
@permission_required('ecommerce.add_categoria', raise_exception=True)
def categoria_cadastro(request):
    # Quando o formulario e enviado, o navegador faz uma requisicao POST.
    if request.method == 'POST':
        # request.POST contem os dados digitados pelo usuario no formulario.
        form = CategoriaForm(request.POST)

        # is_valid() verifica se os dados seguem as regras do ModelForm e da model.
        if form.is_valid():
            # save() cria e grava uma nova categoria no banco de dados.
            form.save()
            messages.success(request, 'Categoria cadastrada com sucesso.')

            # Redireciona para evitar reenviar o formulario ao atualizar a pagina.
            return redirect('categoria_cadastro')
    else:
        # Quando a pagina e aberta pela primeira vez, criamos um formulario vazio.
        form = CategoriaForm()

    # Busca todas as categorias cadastradas para mostrar na tabela do template.
    categorias = Categoria.objects.all()

    # Envia o formulario e a lista de categorias para o arquivo HTML.
    return render(request, 'ecommerce/categoria_cadastro.html', {'form': form, 'categorias': categorias})


# Autorizacao: somente usuarios com a permissao "Can delete categoria" podem excluir.
@login_required(login_url='/admin/login/')
# raise_exception=True mostra erro 403 quando o usuario esta logado, mas nao tem permissao.
@permission_required('ecommerce.delete_categoria', raise_exception=True)
def categoria_excluir(request, categoria_id):
    # Busca a categoria pelo id. Se nao existir, o Django retorna erro 404.
    categoria = get_object_or_404(Categoria, id=categoria_id)

    # Por seguranca, a exclusao deve acontecer apenas via POST.
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoria excluida com sucesso.')

    return redirect('categoria_cadastro')




def carro_cadastro(request):
    # Quando o formulario e enviado, o navegador faz uma requisicao POST.
    if request.method == 'POST':
        # request.POST contem os dados digitados pelo usuario no formulario.
        form = CarroForm(request.POST)

        # is_valid() verifica se os dados seguem as regras do ModelForm e da model.
        if form.is_valid():
            # save() cria e grava uma nova categoria no banco de dados.
            form.save()
            messages.success(request, 'Carro cadastrado com sucesso.')

            # Redireciona para evitar reenviar o formulario ao atualizar a pagina.
            return redirect('carro_cadastro')
    else:
        # Quando a pagina e aberta pela primeira vez, criamos um formulario vazio.
        form = CarroForm()

    # Busca todas as carros cadastradas para mostrar na tabela do template.
    carros = Carro.objects.all()

    # Envia o formulario e a lista de carros para o arquivo HTML.
    return render(request, 'ecommerce/carro_cadastro.html', {'form': form, 'carros': carros})


def carro_excluir(request, carro_id):
    return redirect('home')