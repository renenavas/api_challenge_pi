import sys
sys.path.append('../')

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from usecases.delete_character import delete_character
from usecases.get_all import get_all
from usecases.get_character import get_character_by_id
from usecases.insert_character import insert_character
from pydantic import BaseModel
from typing import List


class CharacterCreate(BaseModel):
    name: str
    height: int
    mass: int
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: int


desc = """
### API con integracón en MariaDB

```
Endpoints:
    /character/getAll
        - Retorna todos los personaje de la base de datos

    /character/get/{id}
        - Retorna un personaje solo por id

    /character/add/
        - Agrega un personaje a la base de datos

    /character/delete/{id}
        - Elimina un personaje por id
```
"""

app = FastAPI(
    title="Challenge Pi Consulting",
    description= desc,
    version= "0.1.0"
    )

@app.get('/character/getAll')
def api_get_all() -> List[CharacterCreate]:
    """
    Busca todos los personajes en la DB 
    ```
    args: None
    return: Json con los atributos de todos los personajes de la DB
    ```
    """
    data = get_all()
    if data[0] == 400:
        raise HTTPException(status_code=400, detail=data[1])
    if data[0] == 200:
        response = {'Detail' : 'Personajes encontrados', 'Characters': data[1]}
    return JSONResponse(content=response, status_code=data[0])

@app.get('/character/get/{id}')
def api_get_character(id: int) -> CharacterCreate:
    """ 
    Busca un personaje por id en la DB
    ```
    args: id del personaje

    return: Json con los atributos del personaje encontrado
    ```
    """
    data = get_character_by_id(id)
    if data[0] == 400:
        raise HTTPException(status_code=400, detail=data[1])
    if data[0] == 200:
        response = {'Detail' : 'Personaje encontrado', 'Character': data[1]}
    return JSONResponse(content=response, status_code=data[0])

@app.post('/character/add')
def api_insert_character(character:CharacterCreate) -> CharacterCreate:
    """
    Agrega un personaje a la DB
    ``` 
    args: Diccionario con los atributos del personaje 
    (el id es autoincremental en la base de datos,es retornado al escribir con éxito)

    return: Json con los atributos del personaje agregado
    ```
    """
    print(character)
    try:
        data = insert_character(name = str(character.name),
                                height = int(character.height),
                                mass = int(character.mass),
                                hair_color = str(character.hair_color),
                                skin_color = str(character.skin_color),
                                eye_color = str(character.eye_color),
                                birth_year = int(character.birth_year)
                                )
    except:
        return JSONResponse(content="Error al parsear el body", status_code=400)    
    if data[0] == 400:
        raise HTTPException(status_code=400, detail=data[1])
    if data[0] == 200:
        response = {'Detail' : 'Personaje agregado', 'Character': data[1]}
    return JSONResponse(content=response, status_code=data[0])

@app.delete('/character/delete/{id}')
def api_delete_character(id: int) -> CharacterCreate:
    """ 
    Elimina un personaje por id
    ```
    args: id de personaje como int

    return: Json con los atributos del personaje eliminado
    ```
    """
    data = delete_character(id)
    if data[0] == 400:
        raise HTTPException(status_code=400, detail=data[1])
    if data[0] == 200:
        response = {'Detail' : 'Personaje eliminado', 'Character': data[1]}
    return JSONResponse(content=response, status_code=data[0])