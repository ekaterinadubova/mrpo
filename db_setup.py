from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base, sessionmaker, backref

Base = declarative_base()

# Таблица связей для определения соотношения "многие ко многим" между вольером и домашним животным
aviary_pet_association = Table('aviary_pet', Base.metadata,
    Column('aviary_id', Integer, ForeignKey('aviaries.id')),
    Column('pet_id', Integer, ForeignKey('pets.id'))
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    def __repr__(self):
        return f"<User(name='{self.fio}', phone='{self.phone}')>"

class Aviary(Base):
    __tablename__ = 'aviaries'

    id = Column(Integer, primary_key=True, autoincrement=True)
    size = Column(String, nullable=False)
    pets = relationship('Pet', secondary=aviary_pet_association, back_populates='aviaries')

    def __repr__(self):
        return f"<Aviary(id={self.id}, size='{self.size})>"

class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    kind = Column(String, nullable=False)
    breed = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    size = Column(String, nullable=False)
    aviaries = relationship('Aviary', secondary=aviary_pet_association, back_populates='pets')

    def __repr__(self):
        return f"<Pet(id={self.id}, name='{self.name}', kind='{self.kind}', breed='{self.breed}', gender='{self.gender}', size='{self.size}')>"

class Food(Base):
    __tablename__ = 'foods'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    pets = relationship('Pets', secondary=aviary_pet_association, back_populates='aviaries')
    # установка отношений
    users = relationship('User', back_populates='foods')
    aviaries = relationship('Aviary', back_populates='pets')

    def __repr__(self):
        return f"<Food(id={self.id}, name='{self.name}')>"

User.food_id = Column(Integer, ForeignKey('foods.id'))
User.food = relationship('Food', back_populates='users')

Aviary.pet_id = Column(Integer, ForeignKey('pets.id'))
Aviary.pet = relationship('Pet', back_populates='aviaries')

DATABASE_URL = 'sqlite:///aviaries.db'  # or any other database URL

def setup_database():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()


    print("Database setup complete.")

if __name__ == "__main__":
    setup_database()

