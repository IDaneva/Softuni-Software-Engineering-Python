from product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for pr in self.products:
            if pr.name == product_name:
                return pr

    def remove(self, product_name):
        a = self.find(product_name)
        if a is not None:
            self.products.remove(a)

    def __repr__(self):
        res = []
        for pr in self.products:
            res.append(f"{pr.name}: {pr.quantity}")

        return "\n".join(res)
