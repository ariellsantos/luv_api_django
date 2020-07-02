from luv_api.src.Domain.products.product import Product
from luv_api.src.Domain.products.iproduct_repository import IProductRepository

class ListAllProducts():

    def __init__(self, product_repository: IProductRepository):
        self._repository = product_repository

    def execute(self) -> [Product]:
        products = self._repository.list()

        return products
