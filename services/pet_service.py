from models.pet import Pet


def __init__(self, name, age, pet_type):
    self.name = name
    if not isinstance(age, int) or age <= 0:
        raise ValueError("Возраст питомца должен быть положительным целым числом.")
    self.age = age
    if pet_type not in ['кошка', 'собака']:
        raise ValueError("Питомец может быть только кошкой или собакой.")
    self.pet_type = pet_type
