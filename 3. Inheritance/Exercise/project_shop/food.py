from project_shop.product import Product


class Food(Product):
    QUANTITY = 15   # set hard coded quantity

    def __init__(self, name):
        super().__init__(name, Food.QUANTITY)   # import attributes form class Product and set the QUANTITY
