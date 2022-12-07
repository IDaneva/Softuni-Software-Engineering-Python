from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    def __init__(self):
        super().__init__(5, 10)

    @staticmethod
    def get_name():
        return "Plant"


