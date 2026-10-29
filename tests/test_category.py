from src.category import Category


def test_category_init(category1):
    assert category1.name == "Смартфоны"
    assert category1.description == ("Смартфоны, как средство не только коммуникации, "
                                     "но и получения дополнительных функций для удобства жизни")
    assert category1.category_count == 1
    assert category1.product_count == 3


def test_product_count():
    assert Category.product_count == 3


def test_category_str(category1, category2):
    assert str(category1) == "Смартфоны, количество продуктов: 27 шт."
    assert str(category2) == "Телевизоры, количество продуктов: 7 шт."


def test_empty_category(empty_category):
    assert empty_category.middle_price() == 0
