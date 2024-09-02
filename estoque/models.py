from django.db import models


class Produto(models.Model):
    codigo = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome


class Lote(models.Model):
    class TipoUnidade(models.TextChoices):
        unidade = "und", "Unidade"
        gramas = "g", "Gramas"
        kilo = "kg", "Kilos"
        ml = "ml", "Mililitros"
        litro = "l", "Litros"
        caixa = "cx", "Caixa"

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    validade = models.DateField()
    quantidade = models.IntegerField()
    tipo_unidade = models.CharField(
        max_length=100, choices=TipoUnidade.choices, default=TipoUnidade.unidade)
    def __str__(self):
        return f'{self.produto.nome} - {self.quantidade}'
