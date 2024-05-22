from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    name: str
    phone: int


u1 = User("Дубова Екатерина Анатольевна", 88005553535)
u2 = User("Полковникова Елизавета Сергеевна", 89998889988)
u3 = User("Забелина Анастасия Игоревна", 88889998899)
