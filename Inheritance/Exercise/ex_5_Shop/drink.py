from ex_5_Shop.product import Product


class Drink(Product):

    def __init__(self, name: str, quantity=10):
        super().__init__(name, quantity)