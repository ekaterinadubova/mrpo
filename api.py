from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from unit_of_work import UnitOfWork
import json
from Repository import UserRepository, AviaryRepository, PetRepository
from db_setup import User, Aviary, Pet

def write_to_json(data, file_path):
    with open(file_path, 'a') as file:
        json.dump(data, file)
        file.write('\n')

class UserCreate(BaseModel):
    name: str
    phone: str

class UserResponse(BaseModel):
    id: int
    name: str
    phone: str

class AviaryCreate(BaseModel):
    size: str

class AviaryResponse(BaseModel):
    id: int
    size: str

class PetCreate(BaseModel):
    name: str
    kind: str
    breed: str
    gender: str
    size: str

class PetResponse(BaseModel):
    id: int
    name: str
    kind: str
    breed: str
    gender: str
    size: str

app = FastAPI()

def get_db():
    with UnitOfWork() as session:
        yield session


@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_users = User(**user.dict())
    db.add(db_users)
    db.commit()
    db.refresh(db_users)

    # Запись действия в JSON файл
    data = {"action": "create_user", "user_id": db_users.id, "user_data": user.dict()}
    write_to_json(data, "actions.json")

    return db_users


@app.post("/aviaries/", response_model=AviaryResponse)
def create_aviary(aviary: AviaryCreate, db: Session = Depends(get_db)):
    db_aviaries = Aviary(**aviary.dict())
    db.add(db_aviaries)
    db.commit()
    db.refresh(db_aviaries)

    # Запись действия в JSON файл
    data = {"action": "create_aviary", "aviary_id": db_aviaries.id, "aviary_data": aviary.dict()}
    write_to_json(data, "actions.json")

    return db_aviaries



@app.post("/pets/", response_model=PetResponse)
def create_pet(pet: PetCreate, db: Session = Depends(get_db)):
    db_pets = Pet(**pet.dict())
    db.add(db_pets)
    db.commit()
    db.refresh(db_pets)

    # Запись действия в JSON файл
    data = {"action": "create_pet", "pet_id": db_pets.id, "pet_data": pet.dict()}
    write_to_json(data, "actions.json")

    return db_pets

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/aviaries/{aviary_id}", response_model=AviaryResponse)
def get_aviary(aviary_id: int, db: Session = Depends(get_db)):
    aviary = db.query(Aviary).filter(Aviary.id == aviary_id).first()
    if aviary is None:
        raise HTTPException(status_code=404, detail="Aviary not found")
    return aviary

@app.get("/pets/{pet_id}", response_model=PetResponse)
def get_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(Pet).filter(Pet.id == pet_id).first()
    if pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

if __name__ == '__main__':
    from uvicorn import run
    run("api:app", host="127.0.0.1", port=8000, reload=True)