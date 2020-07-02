from  rest_framework.response import Response
from rest_framework import  status
from rest_framework.generics import ListAPIView
from luv_api.src.Infraestructure.products.persistence.django_product_repository import DjangoProductRepository
from luv_api.src.Infraestructure.products.models  import Product
from  luv_api.src.Application.products.list_products.list_all_products import ListAllProducts
from ..renderers.product_list_get_renderer import ProductListGetRenderer
from ..serializers.list_products_serializer import ListProductsSerializer

class ListProductsGetView(ListAPIView):
    serializer_class = ListProductsSerializer
    renderer_classes = (ProductListGetRenderer,)

    def list(self, request):
        usecase = self._factory_list_products()
        products = usecase.execute()
        serializer = self.get_serializer(products, many=True)
        return  Response(serializer.data, status=status.HTTP_200_OK)


    def _factory_list_products(self):
        repository = DjangoProductRepository(Product)
        return ListAllProducts(repository)
