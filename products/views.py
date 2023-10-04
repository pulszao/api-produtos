from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework import status

from products.models import ProductDTO
from products.serializers import AddProductsSerializer

from .services import get_all_products, create_new_product


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
