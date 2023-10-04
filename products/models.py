from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


class ProductInputDTO(models.Model):
    name = models.CharField(verbose_name='Nome do Produto', max_length=120, validators=[
        MinLengthValidator(5, 'Nome deve conter no minimo 5 caracteres.')
    ])
    price = models.DecimalField(decimal_places=2, verbose_name='Preço do Produto', max_digits=10, validators=[
        MinValueValidator(0.01, 'Preço minimo do produto deve ser 0,01.')
    ])
    description = models.TextField(verbose_name='Descrição do Produto', validators=[
        MinLengthValidator(10, 'Descrição deve conter no minimo 10 caracteres.')
    ])
    inStock = models.BooleanField()
    quantity = models.IntegerField(verbose_name='Quantidade Disponível do Produto', validators=[
        MinValueValidator(0, 'Quantidade deve ser de no minimo 0.')
    ])


class ProductUpdateDTO(models.Model):
    name = models.CharField(verbose_name='Nome do Produto', max_length=120, validators=[
        MinLengthValidator(5, 'Nome deve conter no minimo 5 caracteres.')
    ])
    price = models.DecimalField(decimal_places=2, verbose_name='Preço do Produto', max_digits=10, validators=[
        MinValueValidator(0.01, 'Preço minimo do produto deve ser 0,01.')
    ])
    description = models.TextField(verbose_name='Descrição do Produto', validators=[
        MinLengthValidator(10, 'Descrição deve conter no minimo 10 caracteres.')
    ])
    quantity = models.IntegerField(verbose_name='Quantidade Disponível do Produto', validators=[
        MinValueValidator(0, 'Quantidade deve ser de no minimo 0.')
    ])


class ProductDTO(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(verbose_name='Nome do Produto', max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço do Produto')
    description = models.TextField(verbose_name='Descrição do Produto')
    inStock = models.BooleanField()
    quantity = models.IntegerField(verbose_name='Quantidade Disponível do Produto')

