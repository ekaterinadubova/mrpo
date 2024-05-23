from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

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
        return f"<User(name='{self.name}', phone='{self.phone}')>"

class Aviary(Base):
    __tablename__ = 'aviaries'

    id = Column(Integer, primary_key=True, autoincrement=True)
    size = Column(String, nullable=False)
    pets = relationship('Pet', secondary=aviary_pet_association, back_populates='aviaries')

    def __repr__(self):
        return f"<Aviary(id={self.id}, size='{self.size}')>"

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

DATABASE_URL = 'sqlite:///pet.db'

def setup_database():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    print("Database setup complete.")

if __name__ == "__main__":
    setup_database()
