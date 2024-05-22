from Class.Pet import Pet

class Food:

    def __init__(self, food_id, name :str, pet_id):
        self.id = food_id
        self.name = name
        self.pet = pet_id


    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f"{self.id}, Название - '{self.name}', Для кого - {self.pet_id}"

