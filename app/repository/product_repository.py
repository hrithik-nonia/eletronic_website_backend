import json
import os

PRODUCT_FILE = "app/data/product_data.json"


def read_products() -> list:
    if not os.path.exists(PRODUCT_FILE):
        return []
    with open(PRODUCT_FILE, "r") as f:
        content = f.read().strip()
        if not content:
            return []
        return json.loads(content)


def write_products(products: list):
    with open(PRODUCT_FILE, "w") as f:
        json.dump(products, f, indent=2)


def add_product(product: dict) -> dict:
    products = read_products()
    products.append(product)
    write_products(products)
    return product


# get all peoduct to show
def get_all_products() -> list:
    return read_products()