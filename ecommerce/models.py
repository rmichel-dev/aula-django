from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Produto(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='produtos',
    )
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Carro(models.Model):
    placa = models.CharField(max_length=7, null=False)
    cor =  models.CharField(max_length=100, null=True)
    modelo = models.CharField(max_length=100, null=False)
    ano = models.IntegerField(null=True)
    preco = models.DecimalField(default=100, decimal_places=2, max_digits=10)
    disponivel = models.BooleanField(default=True)
    potencia = models.IntegerField(null=False)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='carro',
    )
    
    class Meta:
        ordering = ['ano']

    def __str__(self):
        return f'Placa: {self.placa} - Modelo: {self.modelo}'