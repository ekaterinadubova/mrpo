from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Food, User, Aviary, Pet

DATABASE_URL = "sqlite:///aviaries.db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Создаие экземпляров волонтёров
user1 = User(name="Zolotoeva Anna", phone="123456789")
user2 = User(name="Ramid Alina", phone="987654321")

# Создаие экземпляров животных
pet1 = Pet(kind="Cat", name="Cused", breed="Britain", gender="Male", size="Small")
pet2 = Pet(kind="Dog", name="Baloon", breed="Shepherd", gender="Female", size="Big")

# Создаие экземпляров вольеров
aviary1 = Aviary(size="Big")
aviary2 = Aviary(size="Small")

# Добавление животных в вольеры
aviary1.pets.append(pet2)
aviary2.pets.append(pet1)

# Создание экземпляров приюта
food = Food(name="Royal Canin", users=[user1], aviaries=[aviary2], pets=[pet1])

# Добавление данных в бд
session.add(food)
session.commit()

# Запрос в бд на чтение
food = session.query(Food).all()
for food in Food:
    print(food)
    for user in food.users:
        print(f"  {user}")
    for aviary in food.aviaries:
        print(f"  {aviary}")
        for pet in aviary.pets:
            print(f"    {pet}")

session.close()
