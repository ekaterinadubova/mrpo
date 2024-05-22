import sys

sys.path.append('/Users/katyadubova/PycharmProjects/new4lab')
from Class.Food import Food


class Food:

    def __init__(self):
        self.foods = []

    def add_food(self, food: Food):
        self.foods.append(food)

    def del_food(self, food: Food):
        self.foods.remove(food)

    def find_food(self, foodie_id):
        for a in self.foods:
            if (a.food_id == foodie_id):
                return a

    def show_food(self):
        for a in self.foods:
            print(a)