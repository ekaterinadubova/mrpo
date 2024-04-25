from dataclasses import dataclass
from size_enum import Size

@dataclass(frozen=True)
class Aviary:
        id: int
        size: Size
        KindOfPet: str