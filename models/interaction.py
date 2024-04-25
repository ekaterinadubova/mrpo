
from models.status_enum import Status
from models.user import User

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

    def __eq__(self, other):
        if isinstance(other, Interaction):
            return (
                    self.id == other.id and
                    self.KindOfPet == other.KindOfPet and
                    self.status == other.status and
                    self.client == other.client and
                    self.admin == other.admin
            )
        return False