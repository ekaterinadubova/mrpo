import kindOfAnimal

class pet:

    def __init__(self, vaccine, name, gender, kind):
        self.vaccine = vaccine
        self.name = name
        self.gender = gender
        self.kind = kind

p1 = pet(vaccine="Привит", name="Барсик", gender="Женский", kind=[k1])
p2 = pet(vaccine="Привит", name="Доги", gender="Мужской", kind=[k2])
p3 = pet(vaccine="Не привит", name="Мурзик", gender="Мужской", kind=[k1])
p4 = pet(vaccine="Привит", name="Курсе", gender="Женский", kind=[k2])
p5 = pet(vaccine="Привит", name="Пико", gender="Мужской", kind=[k2])