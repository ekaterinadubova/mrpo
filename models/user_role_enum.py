from dataclasses import dataclass
from enum import Enum

@dataclass(frozen=True)
class Role(Enum):
    Client = 1, "Клиент"
    Admin = 2, "Администратор"