import json
import os

from src.classes import Category, Product


def read_json(path: str) -> dict:
    directory_path = os.path.dirname(os.path.dirname(__file__))
    full_path = os.path.join(directory_path, path)
    with open(full_path, 'r', encoding="UTF-8") as file:
        return json.load(file)


def create_json(data: dict) -> list[Category]:
    categories = []
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product(**product))
        categories.append(Category(**category))
    return categories
