from pip._internal.utils import models

from models.user_role_enum import Role

class User:
    def __init__(self, id: int, name: str, phone: int, role: models):
        self.id = id
        self.name = name
        self.phone = phone
        self.role = role

    def __str__(self):
        return f'{self.id} - {self.name} -  {self.phone} - {self.role.value[1]}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, User):
            return (
                self.id == other.id and
                self.name == other.name and
                self.phone == other.phone and
                self.role == other.role
            )
        return False
user = User(1,"alice",3333, Role.Client)
print(user)