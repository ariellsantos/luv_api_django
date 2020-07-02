class Product():

    errors = list()

    def __init__(
            self,
            id: str,
            name: str,
            value: float,
            discount_value: float,
            stock: int
    ):
        self._id = id
        self._name = name
        self._value = value
        self._discount_value = discount_value
        self._stock = stock

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:

        return self._name
    @property
    def value(self) -> float:
        return self._value

    @property
    def discount_value(self) -> float:

        return self._discount_value

    @property
    def stock(self) -> int:
        return self._stock




    @classmethod
    def factory(
            cls,
            id:str,
            name:str,
            value:float,
            discount_value:float,
            stock:int
    ):
        return cls(
            id=id,
            name=name,
            value=value,
            discount_value=discount_value,
            stock=stock
        )

    def to_dict(self):
        return {
            'id': self._id,
            'name': self._name,
            'value': self._value,
            'discount_value': self._discount_value,
            'stock': self._stock
        }
