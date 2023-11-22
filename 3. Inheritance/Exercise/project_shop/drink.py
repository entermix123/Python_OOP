from project_shop.product import Product


class Drink(Product):
    QUANTITY = 10       # set hard coded quantity

    def __init__(self, name: str):
        super().__init__(name, Drink.QUANTITY)      # import attributes form class Product and set the QUANTITY
