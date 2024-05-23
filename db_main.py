from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, User, Aviary, Pet

DATABASE_URL = "sqlite:///pet.db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

user1 = User(name="Zolotoeva Anna", phone="123456789")
user2 = User(name="Ramid Alina", phone="987654321")

pet1 = Pet(kind="Cat", name="Cused", breed="Britain", gender="Male", size="Small")
pet2 = Pet(kind="Dog", name="Baloon", breed="Shepherd", gender="Female", size="Big")

aviary1 = Aviary(size="Big")
aviary2 = Aviary(size="Small")

aviary1.pets.append(pet2)
aviary2.pets.append(pet1)

session.add(user1)
session.add(user2)
session.add(pet1)
session.add(pet2)
session.add(aviary1)
session.add(aviary2)
session.commit()


session.close()
