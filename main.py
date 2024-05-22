
from Class.Aviary import Aviary
from Class.Pet import Pet
from Repository.XMLrepository import XMLRepository

def save_to_xml(pet_data):
    repository = XMLRepository("base.xml")
    repository.save(pet_data)


def find_pet_by_aviary(aviary):
    pet_repository = XMLRepository("base.xml")
    query = f"//item[aviary='{aviary}']"
    pets = pet_repository.find()
    return pets

if __name__ == "__main__":
    pet_data = {
        'pet_id': 1,
        'kind': "Кот",
        'name': "Кисед",
        'breed': "Дворняжка",
        'gender': "Ж",
        'size': "М"
    }
    pet = Pet(**pet_data)
    save_to_xml(pet)
    pet_data = {
        'pet_id': 2,
        'kind': "Собака",
        'name': "Гами",
        'breed': "Дворняжка",
        'gender': "М",
        'size': "Б"
    }
    pet = Pet(**pet_data)
    save_to_xml(pet)
    pet = Pet(3, 'Собака', 'Алси', 'Овчарка', 'Ж', 'Б')
    save_to_xml(pet)

    aviary_data = {
         'aviary_id': 2,
        'size': 'Маленький',
        'pet_id': [1],
    }
    aviary = Aviary(**aviary_data)
    save_to_xml(aviary)
    aviary_data = {
         'aviary_id': 1,
        'size': 'Большой',
        'pet_id': [2, 3],
    }
    aviary = Aviary(**aviary_data)
    save_to_xml(aviary)

    print(find_pet_by_aviary('Кисед'))
