from dataclasses import dataclass
from enum import Enum
@dataclass(frozen=True)
class Gender(Enum):
    Female = 1, "Женский"
    Male = 2, "Мужской"
