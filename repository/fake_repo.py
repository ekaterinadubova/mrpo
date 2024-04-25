from models.aviary import Aviary
from models.pet import Pet
from models.food import Food
from models.interaction import Interaction
from models.user import User
from repository import repo


class FakeRepository(repo):
    __users = {}
    __interaction = {}
    __pets = {}
    __aviary = {}
    __food = {}
    @staticmethod
    def AddUser(self, user: User):
        repo.__users[user.id] = user

    @staticmethod
    def GetUser(self, id: int):
        return repo.__users.get(id)

    @staticmethod
    def AddInteraction(self, interaction: Interaction):
        repo.__interaction[interaction.id] = interaction

    @staticmethod
    def GetInteraction(self, id: int):
        return repo.__interaction.get(id)

    @staticmethod
    def AddPets(self, pet: Pet):
        repo.__pets[pet.id] = pet

    @staticmethod
    def GetPet(self, id: int):
        return repo.__pets.get(id)

    @staticmethod
    def AddAviary(self, aviary: Aviary):
        repo.__aviary[aviary.id] = aviary

    @staticmethod
    def GetAviary(self, id: int):
        return repo.__aviary.get(id)

    @staticmethod
    def AddFood(self, food: Food):
        repo.__food[food.id] = food

    @staticmethod
    def GetFood(self, id: int):
        return repo.__food.get(id)