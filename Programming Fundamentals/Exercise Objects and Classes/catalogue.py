class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [s for s in self.products if s.startswith(first_letter)]

    def __repr__(self):
        thing_to_print = f"Items in the {self.name} catalogue:\n"
        thing_to_print += "\n".join(s for s in sorted(self.products))
        return thing_to_print


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
