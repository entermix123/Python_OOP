from typing import List                 # import List
from project_shop.product import Product     # import Product


class ProductRepository(Product):               # define ProductRepository class

    def __init__(self):
        self.products: List[Product] = []       # set empty list as a collection of objects of type Product

    def add(self, product: Product) -> None:    # define add method with object input type Product
        self.products.append(product)           # add to collection

    def find(self, product_name: str) -> [Product, None]:   # define find method with name of product
        for product in self.products:                       # iterate through collection
            if product.name == product_name:                # check if product exists in collection
                return product                              # return product if exists

    def remove(self, product_name: str) -> None:            # define remove method with name of product
        product = self.find(product_name)                   # find product in collection
        if product:                                         # if product exists
            self.products.remove(product)                   # remove product from collection

    def __repr__(self):                                     # define __repr__ method
        return '\n'.join([f"{k}: {k.quantity}" for k in self.products])     # return string representation of collection
