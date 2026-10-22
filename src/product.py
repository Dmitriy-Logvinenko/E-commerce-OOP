from abc import ABC, abstractmethod
from src.print_mixin import MixinProduct


class BaseProduct(ABC):
    """Абстрактный класс для создания общего шаблона"""

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Product(BaseProduct, MixinProduct):
    """Класс для предоставления информации о продукте"""
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса продуктов"""
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) == self.__class__:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product: dict):
        new_product = cls(name=product["name"],
                          description=product["description"],
                          price=product["price"],
                          quantity=product["quantity"])

        return new_product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price
        return


class Smartphone(Product):
    """Класс-наследник для предоставления информации о смартфонах"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс-наследник для предоставления информации о газоне"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
