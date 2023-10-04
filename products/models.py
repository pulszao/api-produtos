from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


class ProductDTO(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(verbose_name='Nome do Produto', max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço do Produto')
    description = models.TextField(verbose_name='Descrição do Produto')
    inStock = models.BooleanField()
    quantity = models.IntegerField(verbose_name='Quantidade Disponível do Produto')


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

    def save(self, *args, **kwargs):
        # save ProductDTO
        product = ProductDTO()
        product.name = self.name
        product.price = self.price
        product.description = self.description
        product.inStock = self.inStock
        product.quantity = self.quantity
        product.save()

        super().save(*args, **kwargs)


class ProductUpdateDTO(models.Model):
    product = models.ForeignKey(ProductDTO, on_delete=models.CASCADE, related_name='base_product')
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

    def save(self, *args, **kwargs):
        # update ProductDTO
        product = ProductDTO.objects.get(id=self.product.id)
        product.name = self.name
        product.price = self.price
        product.description = self.description
        product.quantity = self.quantity
        product.save()

        super().save(*args, **kwargs)

