from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CarroForm, CategoriaForm, DispositivoForm, ProdutoForm
from .models import Carro, Categoria, Dispositivo, Produto

from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



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
        form = CarroForm(request.POST, request.FILES)

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


class DispositivoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Dispositivo  # Especifica o modelo usado pela view de lista
    template_name = 'ecommerce/dispositivo/lista.html'  # Nome do template HTML usado para renderizar a lista
    context_object_name = 'dispositivos'  # Nome da variável no contexto do template que contém a lista de objetos
    login_url = '/admin/login/'  # URL para redirecionar se o usuário não estiver logado
    permission_required = 'ecommerce.view_dispositivo'  # Permissão necessária para acessar a view
    raise_exception = True  # Levantar exceção se o usuário não tiver permissão, em vez de redirecionar


class DispositivoCadastroView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Dispositivo
    form_class = DispositivoForm
    template_name = 'ecommerce/dispositivo/form.html'
    success_url = reverse_lazy('dispositivo_lista')
    login_url = '/admin/login/'
    permission_required = 'ecommerce.add_dispositivo'
    raise_exception = True

    def form_valid(self, form):  # Método chamado quando o formulário é válido
        # Exibe mensagem de sucesso ao usuário
        messages.success(self.request, 'Dispositivo cadastrado com sucesso.')
        # Chama o método pai para salvar o formulário no banco de dados
        return super().form_valid(form)


class DispositivoDetalheView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Dispositivo
    template_name = 'ecommerce/dispositivo/detalhe.html'
    context_object_name = 'dispositivo'
    login_url = '/admin/login/'
    permission_required = 'ecommerce.view_dispositivo'
    raise_exception = True


class DispositivoAtualizarView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Dispositivo
    form_class = DispositivoForm
    template_name = 'ecommerce/dispositivo/form.html'
    success_url = reverse_lazy('dispositivo_lista')
    login_url = '/admin/login/'
    permission_required = 'ecommerce.change_dispositivo'
    raise_exception = True

    def form_valid(self, form):  # Método chamado quando o formulário é válido
        # Exibe mensagem de sucesso ao usuário
        messages.success(self.request, 'Dispositivo atualizado com sucesso.')
        # Chama o método pai para salvar as alterações no banco de dados
        return super().form_valid(form)


class DispositivoExcluirView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Dispositivo
    template_name = 'ecommerce/dispositivo/confirmar_exclusao.html'
    success_url = reverse_lazy('dispositivo_lista')
    login_url = '/admin/login/'
    permission_required = 'ecommerce.delete_dispositivo'
    raise_exception = True

    def form_valid(self, form):  # Método chamado quando o formulário é válido
        # Exibe mensagem de sucesso ao usuário
        messages.success(self.request, 'Dispositivo excluido com sucesso.')
        # Chama o método pai para confirmar e executar a exclusão
        return super().form_valid(form)
