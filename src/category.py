from src.product import Product


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

    def __str__(self):
        total_products = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_products} шт."

    @property
    def products(self):
        return self.__products

    def add_product(self, product: Product):
        if issubclass(type(product), Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError
