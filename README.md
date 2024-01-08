#TODO
En el root del repo generar un entorno virtual
> python -m venv venv

Activarlo
  En linux:
    > source venv/bin/activate
  En windows:
    > venv\Scripts\activate

Luego hay que instalar las depenencias:
> pip install -r requirements.txt	

Ahora Se puede levantar la base de datos:
En el path donde se encuenta el docker-compose:
> docker compose up -d

Inicializo la tabla y la coneccion:
db_init.py

Ahora se puede levantar la api con sus endpoints:
uvicorn main:app --reload  

En http://localhost:8000/docs se puede ecnontrar la documentación
