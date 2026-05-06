from django import forms

from .models import Categoria, Produto


# ModelForm cria um formulario automaticamente com base em uma model.
class CategoriaForm(forms.ModelForm):
    # A classe Meta informa ao Django qual model sera usada no formulario.
    class Meta:
        # Model que sera usada para criar e salvar os dados do formulario.
        model = Categoria

        # Campos da model que vao aparecer na tela de cadastro.
        fields = ['nome', 'descricao', 'ativo']

        # Textos exibidos como rotulos dos campos no template.
        labels = {
            'nome': 'Nome',
            'descricao': 'Descricao',
            'ativo': 'Ativo',
        }

        # Widgets permitem configurar como cada campo sera exibido no HTML.
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome da categoria'}),
            'descricao': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descricao da categoria'}),
        }


# ModelForm cria um formulario automaticamente com base em uma model.
class ProdutoForm(forms.ModelForm):
    # A classe Meta informa ao Django qual model sera usada no formulario.
    class Meta:
        # Model que sera usada para criar e salvar os dados do formulario.
        model = Produto

        # Campos da model que vao aparecer na tela de cadastro.
        fields = ['categoria', 'nome', 'descricao', 'preco', 'estoque', 'ativo']

        # Textos exibidos como rotulos dos campos no template.
        labels = {
            'categoria': 'Categoria',
            'nome': 'Nome',
            'descricao': 'Descricao',
            'preco': 'Preco',
            'estoque': 'Estoque',
            'ativo': 'Ativo',
        }

        # Widgets permitem configurar como cada campo sera exibido no HTML.
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do produto'}),
            'descricao': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descricao do produto'}),
            'preco': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'estoque': forms.NumberInput(attrs={'min': '0'}),
        }
