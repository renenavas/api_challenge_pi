from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Ruta del archivo .env de la base de datos
env_path = '../.env'

# Carga las variables de entorno desde el archivo .env
load_dotenv(dotenv_path=env_path)

# Defino las credenciales de la db como variables
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
HOST = os.getenv("HOST")
TABLE = os.getenv("USER_TABLE")

# Define el string del conector mysqlconnector
connection_string = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{HOST}/{MYSQL_DATABASE}"

# Crea el engine de SQLAlchemy
engine = create_engine(connection_string)

# Define la clase Base para la declaración de modelos
Base = declarative_base()

# Crea las tablas en la base de datos
Base.metadata.create_all(engine)

# Crea una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()