from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework import status

from products.models import ProductDTO
from products.serializers import AddProductsSerializer, UpdateProductsSerializer

from .services import get_all_products, create_new_product, get_product_data, update_product_data, delete_product


class Products(APIView):

    def get(self, request):
        """
        Listar todos os produtos.
        """
        data = get_all_products()

        return JsonResponse(data, safe=False)

    def post(self, request):
        """
        Criar um novo produto.
        """

        serializer = AddProductsSerializer(data=request.data)

        if serializer.is_valid():

            create_new_product(serializer.validated_data)

            return JsonResponse({'message': 'Produto criado com sucesso', 'status': status.HTTP_201_CREATED})

        else:
            return JsonResponse({'message': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})


class ProductData(APIView):

    def get(self, request, product_id):
        """
        Obter detalhes de um produto específico.
        """
        try:
            data = get_product_data(product_id)

            return JsonResponse(data, safe=False)

        except ProductDTO.DoesNotExist:
            return JsonResponse({'message': 'Produto não encontrado', 'status': status.HTTP_404_NOT_FOUND})

    def put(self, request, product_id):
        """
        Atualizar detalhes de um produto.
        """

        serializer = UpdateProductsSerializer(data=request.data)

        if serializer.is_valid():

            try:
                update_product_data(serializer.validated_data, product_id)

                return JsonResponse({'message': 'Produto editado com sucesso', 'status': status.HTTP_201_CREATED})

            except ProductDTO.DoesNotExist:
                return JsonResponse({'message': 'Produto não encontrado', 'status': status.HTTP_404_NOT_FOUND})

        else:
            return JsonResponse({'message': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

    def delete(self, request, product_id):
        """
        Excluir um produto.
        """

        try:
            delete_product(product_id)

            return JsonResponse({'message': 'Produto excluído com sucesso', 'status': status.HTTP_204_NO_CONTENT})

        except ProductDTO.DoesNotExist:
            return JsonResponse({'message': 'Produto não encontrado', 'status': status.HTTP_404_NOT_FOUND})
