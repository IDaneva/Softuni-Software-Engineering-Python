from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    sponsors = {"Oracle": {1: 1_500_000, 2: 800_000},
                "Honda": {8: 20_000, 10: 10_000}}
    expenses = 250_000

    def __init__(self, budget: int):
        self.budget = budget

    def calculate_revenue_after_race(self, race_pos: int):
        total = -RedBullTeam.expenses
        for sponsor, sponsorships in RedBullTeam.sponsors.items():
            for position, money in sponsorships.items():
                if race_pos <= position:
                    total += money
                    break

        self.budget += total
        return f"The revenue after the race is {total}$. Current budget {self.budget}$"


