
class Pet:
    def __init__(self, pet_id, name, kind, breed, gender, size):
        self.id = pet_id
        self.name = name
        self.kind = kind
        self.breed = breed
        self.gender = gender
        self.size = size


    def __eq__(self, other):
        return self.id == other.id
    def __str__(self):
        return f"""Питомец: {self.kind}, 
            Имя: {self.name}, 
            Порода: {self.breed}
            Пол: {self.gender},
            Размер: {self.size}"""

p1 = Pet(pet_id=1, name="Кити", kind="Кот", breed="Британец", gender="Ж", size="М")
p2 = Pet(pet_id=2, name="Кисед", kind="Кот", breed="Дворняжка", gender="Ж", size="М")
p3 = Pet(pet_id=3, name="Гамми", kind="Собака", breed="Дворняжка", gender="М", size="Б")
p4 = Pet(pet_id=4, name="Зюля", kind="Кот", breed="Сфинкс", gender="М", size="М")
p5 = Pet(pet_id=5, name="Пупси", kind="Собака", breed="Шпиц", gender="Ж", size="М")
p6 = Pet(pet_id=6, name="Доро", kind="Собака", breed="Бульдог", gender="М", size="Б")

# print(p1==p3, p3==p6)
