from Class.Pet import Pet

class Aviary:
    def __init__(self, aviary_id, size, pet_id):
        self.id = aviary_id
        self.size = size
        self.pet_id = pet_id


    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f"ID {self.id}, Размер: {self.size}, Содержит питомцев:{self.pet_id}"
