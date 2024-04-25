
from models import user


class UserRepository:

    def __init__(self):
        self.user = []

    def add_user(self, user: user):
        self.clients.append(user)

    def del_user(self, user: user):
        self.clients.remove(user)

    def find_user(self, user_id):
        for c in self.user:
            if c.id == user_id:
                return c

    def show_user(self):
        for c in self.user:
            print(f"{c.id}; {c.name}; {c.phone}; ")
