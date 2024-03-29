from dataclasses import dataclass
from models.gender_enum import Gender
from models.size_enum import Size

@dataclass(frozen=True)
class Pet:
        id: int
        KindOfPet: str
        gender: Gender
        name: str
        size: Size