from models.pet import Pet
from models.size_enum import Size
from models.aviary import Aviary
from models.gender_enum import Gender
from models.KindOfPet import KindOfPet
from typing import List


def check_cat(aviaries: List[Aviary], pets: List[Pet]) -> List[Aviary]:
        dog_aviary = None
        cat_aviary = None

        for aviary in aviaries:
            if aviary.KindOfPet == "С":
                dog_aviary = aviary
            elif aviary.KindOfPet == "К":
                cat_aviary = aviary

        for pet in pets:
            if pet.KindOfPet == "С":
                if dog_aviary is not None:
                    dog_aviary = dog_aviary._replace(pets=dog_aviary.pets + [pet])
            elif pet.KindOfPet == "К":
                if cat_aviary is not None:
                    if any(cat_pet.id == pet.id for cat_pet in cat_aviary.pets):
                        print(f"Ошибка! '{pet.name}' уже в другом вольере")
                    else:
                        cat_aviary = cat_aviary._replace(pets=cat_aviary.pets + [pet])

        return [dog_aviary, cat_aviary]

