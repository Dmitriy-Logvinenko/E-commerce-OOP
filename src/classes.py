class Product:
    """Класс для предоставления информации о продукте"""
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса продуктов"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product: dict):
        new_pr.name = product["name"]
        new_pr.description = product["description"]
        new_pr.price = product["price"]
        new_pr.quantity = product["quantity"]

        return new_pr

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


class Category:
    """Класс для предоставления информации о категориях продуктов"""
    name: str
    description: str
    __products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса категорий"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price}. Остаток: {product.quantity} шт.\n"
        return self.__products

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1
