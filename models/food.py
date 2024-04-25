from dataclasses import dataclass


@dataclass(frozen=True)
class Food:
        id: int
        cat_food: str
        dog_food: str
        food: str
        KindOfPet: str