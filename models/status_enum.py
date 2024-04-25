from dataclasses import dataclass
from enum import Enum
@dataclass(frozen=True)
class Status(Enum):
    Take = 1, "Взять питомца"
    GiveAway = 2, "Сдать питомца"