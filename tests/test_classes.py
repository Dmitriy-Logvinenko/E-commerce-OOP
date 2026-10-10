from src.classes import Product, Category


def test_classes_init(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_name_products(product1, product2, product3, product4):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product2.name == "Iphone 15"
    assert product3.name == "Xiaomi Redmi Note 11"
    assert product4.name == "55\" QLED 4K"


def test_description_products(product1, product2, product3, product4):
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product2.description == "512GB, Gray space"
    assert product3.description == "1024GB, Синий"
    assert product4.description == "Фоновая подсветка"


def test_price_products(product1, product2, product3, product4):
    assert product1.price == 180000.0
    assert product2.price == 210000.0
    assert product3.price == 31000.0
    assert product4.price == 123000.0


def test_quantity_products(product1, product2, product3, product4):
    assert product1.quantity == 5
    assert product2.quantity == 8
    assert product3.quantity == 14
    assert product4.quantity == 7


def test_category_init(category1):
    assert category1.name == "Смартфоны"
    assert category1.description == ("Смартфоны, как средство не только коммуникации, "
                                     "но и получения дополнительных функций для удобства жизни")
    assert category1.category_count == 1
    assert category1.product_count == 3


def test_new_product():
    new_product = Product("Samsung Galaxy S24", "512GB, Серый цвет, +100500MP", 100000.0, 2)
    new_product.name = "Samsung Galaxy S24 Ultra"
    new_product.description = "512GB, Серый цвет, +100500MP"
    new_product.price = 100000.0
    new_product.quantity = 2


def test_product_count():
    assert Category.product_count == 3
