from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from products.models import ProductDTO


class ProductsTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_all_products(self):
        response = self.client.get(reverse('products:products'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        # Teste sucesso
        data = {
            'name': 'Calça Jeans',
            'price': '10.99',
            'description': 'Descrição do produto.',
            'inStock': True,
            'quantity': 50,
        }
        response = self.client.post(reverse('products:products'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Teste dados inválidos
        data = {
            'price': '10.99',
            'description': 'Descrição do produto.',
            'quantity': 50,
        }
        response = self.client.post(reverse('products:products'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ProductDataTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = ProductDTO.objects.create(
            id=1,
            name='Calça Jeans',
            price=250.99,
            description='Descrição da calça jeans',
            inStock=True,
            quantity=30,
        )

    def test_get_product_data(self):
        # Teste sucesso
        response = self.client.get(reverse('products:product_data', args=[self.product.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Teste ID inválido
        response = self.client.get(reverse('products:product_data', args=[3]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_product_data(self):
        # Teste sucesso
        data = {
            'name': 'Calça Jeans Branca',
            'price': 299.13,
            'description': 'Descrição da calça Jeans Branca',
            'quantity': 50,
        }
        response = self.client.put(reverse('products:product_data', args=[self.product.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verificar se o produto atualizado é retornado em test_list_all_products
        list_response = self.client.get(reverse('products:products'))
        self.assertEqual(list_response.status_code, status.HTTP_200_OK)
        products = list_response.json()
        self.assertEqual(products[0]['name'], 'Calça Jeans Branca')

        # Teste ID inválido
        response = self.client.put(reverse('products:product_data', args=[10]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Teste informações faltando
        data = {
            'name': 'Calça Jeans Branca',
            'price': 299.13,
            'quantity': 50,
        }
        response = self.client.put(reverse('products:product_data', args=[self.product.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_product(self):
        # Teste sucesso
        response = self.client.delete(reverse('products:product_data', args=[self.product.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Teste ID inválido
        response = self.client.delete(reverse('products:product_data', args=[10]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
