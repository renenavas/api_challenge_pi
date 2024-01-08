import os, sys
sys.path.append('../')


from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from dotenv import load_dotenv


env_path = './.env'

# Carga las variables de entorno desde el archivo .env
load_dotenv(dotenv_path=env_path)

# Defino la tabla
TABLE = os.getenv("USER_TABLE")
#TABLE="characters"
print("TABLA", TABLE)

Base = declarative_base()

class Character(Base):
    __tablename__ = TABLE
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(255), nullable=False)
    skin_color = Column(String(255), nullable=False)
    eye_color = Column(String(255), nullable=False)
    birth_year = Column(Integer, nullable=False)

    def to_character(self):
        return Character(
            id = self.id,
            name = self.name,
            height = self.height,
            mass = self.mass,
            hair_color = self.hair_color,
            skin_color = self.skin_color,
            eye_color = self.eye_color,
            birth_year = self.birth_year
            )

    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'height':self.height,
            'mass':self.mass,
            'hair_color':self.hair_color,
            'skin_color':self.skin_color,
            'eye_color':self.eye_color,
            'birth_year':self.birth_year
        }
    
def to_orm(CharacterData):
    return Character(
        name=CharacterData.name,
        height=CharacterData.height,
        mass=CharacterData.mass,
        hair_color=CharacterData.hair_color,
        skin_color=CharacterData.skin_color,
        eye_color=CharacterData.eye_color,
        birth_year=CharacterData.birth_year
    )