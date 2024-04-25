import abc
from abc import ABC


class Repository(ABC):

    @abc.abstractmethod
    def AddUser(self):
        pass

    @abc.abstractmethod
    def GetUser(self):
        pass

    @abc.abstractmethod
    def AddInteraction(self):
        pass

    @abc.abstractmethod
    def GetInteraction(self):
        pass

    @abc.abstractmethod
    def AddPets(self):
        pass

    @abc.abstractmethod
    def GetPets(self):
        pass

    @abc.abstractmethod
    def AddAviary(self):
        pass

    @abc.abstractmethod
    def GetAviary(self):
        pass

    @abc.abstractmethod
    def AddFood(self):
        pass

    @abc.abstractmethod
    def GetFood(self):
        pass
