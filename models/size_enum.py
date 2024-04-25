from dataclasses import dataclass
from enum import Enum
@dataclass(frozen=True)
class Size(Enum):
    Big = 1, "Большой"
    Small = 2, "Маленький"
