from models import user
from models import pet
from repos.xmlrepo import XMLRepository


def save_to_xml(user_data):
    repository = XMLRepository("base.xml")
    repository.save(user_data)


def find_user_by_name(name):
    user_repository = XMLRepository("base.xml")
    query = f"//item[name='{name}']"
    user = user_repository.find()
    return user


if __name__ == "__main__":
    user_data = {
        'id': 1,
        'name': "Катя",
        'age': 21

    }
    user = user(**user_data)
    save_to_xml(user)
    user_data = {
        'id': 2,
        'name': "Лиза",
        'age': 20

    }
    user = user(**user_data)
    save_to_xml(user)
    user = user(3, 'Соня', 20)
    save_to_xml(user)

    pet_data = {
        'id': 2,
        'name': 'Барсик',
        'kind': 'Кошка'

    }
    pet = pet(**pet_data)
    save_to_xml(pet)
    product_data = {
        'id': 1,
        'name': 'Шарик',
        'kind': 'Собака'
    }
    pet = pet(**pet_data)
    save_to_xml(pet)

    print(find_user_by_name('Катя'))

