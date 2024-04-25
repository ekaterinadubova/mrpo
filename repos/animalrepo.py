
from models import pet


class PetRepository:

    def __init__(self):
        self.pet = []

    def add_pet(self, pet: pet):
        self.pet.append(pet)

    def del_pet(self, pet: pet):
        self.pet.remove(pet)

    def find_pet(self, pet_id):
        for o in self.pet:
            if o.id == pet_id:
                return o

    def show_pet(self):
        for o in self.pet:
            print(f"{o.id}; {o.food_id}; "
                  f"{o.product_id}; {o.product_count}; "
                  f"{o.delivery_date}")