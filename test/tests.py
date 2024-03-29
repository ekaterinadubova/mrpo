import unittest
from models.aviary import Aviary
from models.pet import Pet
from models.food import Food



class aviary_service_test:

    def test_pet_not_in_multiple_aviary(self):
        pet = Pet("Мурка", 5, "кошка")
        aviary1 = Aviary("Вольер 1")
        aviary2 = Aviary("Вольер 2")

        aviary1.add_pet(pet)
        self.assertTrue(aviary1.has_pet(pet))
        self.assertFalse(aviary2.has_pet(pet))

    def test_dog_not_in_cat_aviary(self):
        cat_aviary = Aviary("Вольер для кошек")
        dog = Pet("Шарик", 3, "собака")

        with self.assertRaises(ValueError):
            cat_aviary.add_pet(dog)


class pet_service_test:

    def test_pet_type_is_cat_or_dog(self):
        with self.assertRaises(ValueError):
            pet = Pet("Шарик", 3, "попугай")

    def test_pet_age(self):
        with self.assertRaises(ValueError):
            pet = Pet("Барсик", -2, "кошка")

    def test_food(self):
        cat_food = Food("Корм для кошек")
        dog_food = Food("Корм для собак")

        cat = Pet("Мурка", 5, "кошка")
        dog = Pet("Шарик", 3, "собака")

        with self.assertRaises(ValueError):
            dog.eat(cat_food)


if __name__ == '__main__':
    unittest.main()