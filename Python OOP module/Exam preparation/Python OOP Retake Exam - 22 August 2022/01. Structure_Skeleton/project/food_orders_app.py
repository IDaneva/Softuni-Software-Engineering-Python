from project.client import Client
from project.meals.meal import Meal
# from project.meals.starter import Starter
# from project.meals.dessert import Dessert
# from project.meals.main_dish import MainDish


class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 0

    def register_client(self, client_phone_number: str):
        try:
            cmr = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        except StopIteration:
            cmr = Client(client_phone_number)
            self.clients_list.append(cmr)
            return f"Client {client_phone_number} registered successfully."

        raise Exception("The client has already been registered!")

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ not in ["Starter", "MainDish", "Dessert"]:
                continue
            self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        result = [food.details() for food in self.menu]
        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        try:
            cmr = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        except StopIteration:
            self.register_client(client_phone_number)
            cmr = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        cart_for_current_spree = {}
        bill_for_shopping = 0

        for meal_name, quantities in meal_names_and_quantities.items():
            try:
                meal = next(filter(lambda m: m.name == meal_name, self.menu))
            except StopIteration:
                raise Exception(f"{meal_name} is not on the menu!")

            if meal.quantity < quantities:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal.name}!")

            cart_for_current_spree[meal] = quantities
            bill_for_shopping += meal.price * quantities

        cmr.shopping_cart.extend([x for x in cart_for_current_spree])
        cmr.bill += bill_for_shopping
        for k, v in cart_for_current_spree.items():
            needed_index = self.menu.index(k)
            self.menu[needed_index].quantity -= v
            if self.menu[needed_index].quantity == 0:
                self.menu.remove(k)

        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join([x.name for x in cmr.shopping_cart])} for {cmr.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        cmr = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        if not cmr.shopping_cart:
            raise Exception("There are no ordered meals!")
        for thing in cmr.shopping_cart:
            if thing not in self.menu:
                self.menu.append(thing)
            idx = self.menu.index(thing)
            self.menu[idx].quantity += thing.quantity

        cmr.shopping_cart = []
        cmr.bill = 0.0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        cmr = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        if not cmr.shopping_cart:
            raise Exception("There are no ordered meals!")

        self.receipt_id += 1
        paid = cmr.bill
        cmr.bill = 0.0
        cmr.shopping_cart = []
        return f"Receipt #{self.receipt_id} with total amount of " \
               f"{paid:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."


# toast = Starter("toast", 2.5, 2)
# soup = Starter("tomato", 5, 10)
# a = Dessert("sweets", 5, 10)
# b = MainDish("cucumber", 5, 10)
# c = Dessert("tomato", 5, 10)
#
# restaurant = FoodOrdersApp()
# restaurant.add_meals_to_menu(toast, soup, a, b, c)
# print(restaurant.show_menu())
