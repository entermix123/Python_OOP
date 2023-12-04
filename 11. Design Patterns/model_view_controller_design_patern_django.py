from typing import List


class Product:      # base class for Product

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class StoreModel:       # base class StoreModel

    def __init__(self):
        self.products = []      # list of products

    def add_product(self, product: Product):        # add product to store
        self.products.append(product)

    def get_products(self) -> List[Product]:        # represents products in store
        return self.products


class StoreView:            # base class StoreView

    def display_products(self, products: List[Product]):    # display products in store
        print("Available products:")
        for product in products:                                # iterate true products in store
            print(f"{product.name} - ${product.price:.2f}")     # display product name and price

    def get_user_input(self) -> str:                            # get user input
        return input("Enter product name to purchase or 'exit' to quit: ")

    def display_error(self, message: str):                      # display error if user input is invalid
        print(f"Error: {message}")


class StoreController:        # base class Controller, used to manage the store activities

    def __init__(self, model: StoreModel, view: StoreView):     # initialize with model and view
        self.model = model
        self.view = view

    def add_product(self, product: Product):    # add product to store
        self.model.add_product(product)

    def get_products(self) -> List[Product]:    # display products in store
        return self.model.get_products()

    def run(self):                              # run user interface
        while True:
            products = self.get_products()              # create instance of products
            self.view.display_products(products)        # display products in store
            user_input = self.view.get_user_input()     # get user input
            if user_input == "exit":                    # exit program if user enter 'exit'
                break
            else:
                product_names = [product.name for product in products]  # get product names
                if user_input in product_names:                         # search user input in product names
                    product = products[product_names.index(user_input)]     # if product name is found
                    print(f'You purchased {product.name} for ${product.price:.2f}.')    # display message that product is purchased
                else:
                    self.view.display_error(f"Invalid product name")    # display error message for user invalid input


def main():                     # main program
    model = StoreModel()                                # create store model
    view = StoreView()                                  # create view model
    controller = StoreController(model, view)           # create controller
    controller.add_product(Product('Shirt', 20.0))      # add shirt to store
    controller.add_product(Product('Pants', 30.0))      # add pants to store
    controller.add_product(Product('Shoes', 40.0))      # add shoes to store
    controller.run()                                    # run user interface


if __name__ == '__main__':      # main program condition
    main()


