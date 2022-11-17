from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    sponsors = {"Petronas": {1: 1_000_000, 2: 500_000},
                "TeamViewer": {5: 100_000, 7: 50_000}}
    expenses = 200_000

    def __init__(self, budget: int):
        self.budget = budget

    def calculate_revenue_after_race(self, race_pos: int):
        total = -MercedesTeam.expenses
        for sponsor, sponsorships in MercedesTeam.sponsors.items():
            for position, money in sponsorships.items():
                if race_pos <= position:
                    total += money
                    break

        self.budget += total
        return f"The revenue after the race is {total}$. Current budget {self.budget}$"


