import sys

sys.path.append('/Users/katyadubova/PycharmProjects/6laba')
from Class.User import User


class UserRepository:

    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)

    def del_user(self, user: User):
        self.users.remove(user)

    def find_user(self, user_id):
        for a in self.users:
            if (a.id == user_id):
                return a

    def show_users(self):
        for a in self.users:
            print(a)