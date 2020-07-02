from luv_api.src.Domain.products.product import Product
from luv_api.src.Domain.products.iproduct_repository import IProductRepository


class BulkListProducts():

    def __init__(
            self,
            product_repository: IProductRepository,
            products: list
    ):
        self._repository = product_repository
        self._products = products

    def execute(self):
        products = self._factory_products(self._products)
        self._repository.bulk(products)

    def _factory_products(self, products: Product) -> [Product]:
        products_created = []
        for product in products:
            product_created = Product.factory(**product)
            products_created.append(product_created)

        return  products_created
