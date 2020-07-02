from luv_api.src.Domain.products.iproduct_repository import IProductRepository
from django.db.models import Model
from django.core.exceptions import ObjectDoesNotExist

from luv_api.src.Domain.products.product import Product


class DjangoProductRepository(IProductRepository):

    def __init__(self, model: Model):
        self._model = model


    def exists(self, id: str) -> bool:
        if not self._model.objects.filter(pk=id).exists():
            return  False
        return True

    def list(self) -> [Product]:
        instances = self._model.objects.all()

        products = [self._factory_product(instance) for instance in instances]

        return products

    def bulk(self, products: [Product]):
        product_list = self._get_dicts_product_list(products)
        self._model.objects.bulk_create(product_list)


    def _get_dicts_product_list(self, products):
        products_list = [ self._model(**product.to_dict()) for product in products]
        return products_list



    def _factory_product(self, instance: Model) -> Product:
        return Product.factory(
            id=instance.id,
            name=instance.name,
            value=instance.value,
            discount_value=instance.discount_value,
            stock=instance.stock
        )
