
from models import food


class FoodRepository:

    def __init__(self):
        self.food = []

    def add_food(self, food: food):
        if not food in self.food:
            self.food.append(food)

    def del_food(self, food: food):
        self.food.remove(food)

    def find_food(self, food_id):
        for f in self.food:
            if f.id == food_id:
                return f

    def show_food(self):
        for p in self.food:
            print(f"{p.name}; {p.category.name}; "
                  f"{p.price}")

