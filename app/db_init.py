from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
from dotenv import load_dotenv
import os

# Ruta del archivo .env de la base de datos
env_path = '../.env'

# Carga las variables de entorno desde el archivo .env
load_dotenv(dotenv_path=env_path)

# Defino las credenciales de la db como variables
MYSQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
MYSQL_ROOT_USER = os.getenv("MYSQL_ROOT_USER")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
HOST = os.getenv("HOST")

# Define el string del conector mysqlconnector
connection_string = f"mysql+mysqlconnector://{MYSQL_ROOT_USER}:{MYSQL_ROOT_PASSWORD}@{HOST}/{MYSQL_DATABASE}"

# Crea el engine de SQLAlchemy
engine = create_engine(connection_string)

# Especifica las variables de entorno o los valores directos
MYSQL_ROOT_USER = MYSQL_ROOT_USER
MYSQL_ROOT_PASSWORD = MYSQL_ROOT_PASSWORD
MYSQL_DATABASE = MYSQL_DATABASE
MYSQL_USER = MYSQL_USER
MYSQL_USER_PASSWORD = MYSQL_PASSWORD

# Crea el engine de SQLAlchemy
engine = create_engine(f"mysql+mysqlconnector://{MYSQL_ROOT_USER}:{MYSQL_ROOT_PASSWORD}@localhost/{MYSQL_DATABASE}")

# Conecta al motor
connection = engine.connect()

# Ejecuta comandos SQL para crear la base de datos y la tabla
connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DATABASE};"))
connection.execute(text(f"CREATE USER IF NOT EXISTS '{MYSQL_USER}'@'localhost' IDENTIFIED BY '{MYSQL_USER_PASSWORD}';"))
connection.execute(text(f"GRANT ALL PRIVILEGES ON {MYSQL_DATABASE}.* TO '{MYSQL_USER}'@'localhost';"))
connection.execute(text("FLUSH PRIVILEGES;"))

# Cierra la conexión
connection.close()

# Define el modelo de la tabla 'characters'
Base = declarative_base()

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(255), nullable=False)
    skin_color = Column(String(255), nullable=False)
    eye_color = Column(String(255), nullable=False)
    birth_year = Column(Integer, nullable=False)

# Crea la tabla 'characters'
metadata = MetaData()
Base.metadata.create_all(engine)