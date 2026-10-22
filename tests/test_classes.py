import pytest
from src.classes import Category, Product


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


def test_new_price(capsys, product1):
    product1.price = 0
    massage = capsys.readouterr()
    assert massage.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_product_str(product1, product2, product3, product4):
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(product2) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert str(product3) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    assert str(product4) == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.'


def test_category_str(category1, category2):
    assert str(category1) == "Смартфоны, количество продуктов: 27 шт."
    assert str(category2) == "Телевизоры, количество продуктов: 7 шт."


def test_add(product1, product2, product3):
    assert product1 + product2 == 2580000.0
    assert product1 + product3 == 1334000.0
    assert product2 + product3 == 2114000.0


def test_iteration(product1, product2, product3, product4):
    assert product1.name == "Samsung Galaxy S23 Ultra"


def test_product_iteration(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Iphone 15"
    assert next(product_iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_smartphone(smartphone1):
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_grass(grass1):
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_add_is_false(smartphone1, grass1):
    assert smartphone1.price + smartphone1.price == 360000
    with pytest.raises(TypeError):
        smartphone1 + grass1


def test_add_new_product(smartphone1, category1):
    with pytest.raises(TypeError):
        category1.add_product("Not a product")
