import abc
from .product import Product


class IProductRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def exists(self) -> bool:
        pass

    @abc.abstractmethod
    def list(self) -> [Product]:
        pass

    @abc.abstractmethod
    def bulk(self, products: [Product]):
        pass
