from  rest_framework.response import Response
from rest_framework import  status
from rest_framework.generics import CreateAPIView
from luv_api.src.Infraestructure.products.persistence.django_product_repository import DjangoProductRepository
from luv_api.src.Infraestructure.products.models  import Product
from luv_api.src.Application.products.bulk_list_products.bulk_list_products import  BulkListProducts
from ..serializers.list_products_serializer import ListProductsSerializer

class BulkProductsPostView(CreateAPIView):
    serializer_class = ListProductsSerializer

    def create(self, request):
        products = request.data.get('products', [])
        serializers = self.get_serializer(data=products, many=True)
        serializers.is_valid(raise_exception=True)
        usecase = self._factory_bulk_list_porducts(products)

        usecase.execute()
        return Response({"status":"ok"}, status=status.HTTP_200_OK)

    def _factory_bulk_list_porducts(self, products:list) -> BulkListProducts:
        repository = DjangoProductRepository(Product)

        usecase = BulkListProducts(repository, products=products)

        return  usecase


