from dataclasses import dataclass
from enum import Enum
from datetime import datetime


class Role(Enum):
    Client = 1, "Клиент"
    Admin = 2, "Администратор"


dataclass(frozen=True)
class User:
    def __init__(self, id: int, name: str, phone: int, role: Role):
        self.id = id
        self.name = name
        self.phone = phone
        self.role = role

    def __str__(self):
        return f'{self.id} - {self.name} -  {self.phone} - {self.role.value[1]}'

    def __repr__(self):
        return self.__str__()


class Status(Enum):
    Take = 1, "Взять питомца"
    GiveAway = 2, "Сдать питомца"


class Interaction:
    def __init__(self, id: int, KindOfPet: str, status: Status, client: User, admin: User):
        self.id = id
        self.status = status
        self.KindOfPet = KindOfPet
        self.client = client
        self.admin = admin

    def __str__(self):
        return f'{self.id} -  {self.status.value[1]} - {self.KindOfPet} -  {self.client}\n {self.admin} '

    def __repr__(self):
        return self.__str__()


class Gender(Enum):
    Female = 1, "Женский"
    Male = 2, "Мужской"


class Size(Enum):
    Big = 1, "Большой"
    Small = 2, "Маленький"


class Aviary:
    def __init__(self, id: int, size: Size, KindOfPet: str):
        self.id = id
        self.size = size
        self.KindOfPet = KindOfPet


class Pet:
    def __init__(self, id: int, KindOfPet: str, gender: Gender, name: str, size: Size):
        self.id = id
        self.KindOfPet = KindOfPet
        self.gender = gender
        self.name = name
        self.size = size


    def __str__(self):
        return f'{self.id} - {self.name} - {self.KindOfPet} - {self.gender} - {self.size}'

    def __repr__(self):
        return self.__str__()


class Food:
    def __init__(self, id: int, food: str, KindOfPet: str):
        self.id = id
        self.food = food
        self.KindOfPet = KindOfPet

    def __str__(self):
        return f'{self.id} - {self.food} -  {self.KindOfPet}'

    def __repr__(self):
        return self.__str__()


class Repository:
    __users = {}
    __interaction = {}
    __pets = {}
    __aviary = {}
    __food = {}

    @staticmethod
    def AddUser(user: User):
        Repository.__users[user.id] = user

    @staticmethod
    def GetUser(id: int):
        return Repository.__users.get(id)

    @staticmethod
    def AddInteraction(interaction: Interaction):
        Repository.__interaction[interaction.id] = interaction

    @staticmethod
    def GetInteraction(id: int):
        return Repository.__interaction.get(id)

    @staticmethod
    def AddPet(pet: Pet):
        Repository.__pets[pet.id] = pet

    @staticmethod
    def GetPet(id: int):
        return Repository.__pets.get(id)

    @staticmethod
    def AddAviary(aviary: Aviary):
        Repository.__aviary[aviary.id] = aviary

    @staticmethod
    def GetAviary(id: int):
        return Repository.__aviary.get(id)

    @staticmethod
    def AddFood(food: Food):
        Repository.__food[food.id] = food

    @staticmethod
    def GetFood(id: int):
        return Repository.__food.get(id)


user_katya = User(1,"Katya", "88888888888", Role.Client)
user_liza = User(1,"Liza", "99999999999", Role.Admin)
Repository.AddUser(user_katya)
print(Repository.GetUser(1))

Repository.AddInteraction(Interaction(1, "К", Status.GiveAway, user_katya, user_liza))
print(f'Оформление \n {Repository.GetInteraction(1)} ')

Repository.AddAviary(Aviary(1, Size.Small, "К"))
print(f'Вольер: {Repository.GetAviary(1)}')

Repository.AddFood(Food(1, "Пурина", "К"))
print(f'Еда: {Repository.GetFood(1)}')

pet1 = Pet(1, "К", Gender.Female, "Барсик", Size.Small)
Repository.AddPet(pet1)
print(f'Питомец: {Repository.GetPet(1)}')

