class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        monthly_expenses = 0
        for x in args:
            for appliance in x:
                monthly_expenses += appliance.get_monthly_expense()

        self.__expenses += monthly_expenses

    def __str__(self):
        return f"{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$, Expenses: {self.__expenses:.2f}$"

