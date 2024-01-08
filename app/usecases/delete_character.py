import sys
sys.path.append('../')

from adapters.orm_adapter import Character
import adapters.db_interface as dbc

def get_character_by_id(character_id):
    try:
        character = dbc.session.get(Character, character_id)
        dbc.session.close()
        return character
    except Exception as error:
        raise Exception(f'Se encontro el siguiente error:\n{error}\nError al obtener el personaje')
        
def delete_character(id):
    character_to_delete = get_character_by_id(id)
    if character_to_delete:
        try:    
            dbc.session.delete(character_to_delete)
            dbc.session.commit()
            char_dict = character_to_delete.to_dict()
            #print(f'Se eliminó el siguiente personaje:\n{char_dict}')
            dbc.session.close()
            return 200, char_dict
        except Exception as error:
            print(f'Se encontro el siguiente error:\n{error}')
            return 400, str(error)
    else:
        e = Exception(f'Error al obtener el personaje con id:{id}')
        print(e)
        return 400, str(e)
    

if __name__ == '__main__':
    id = sys.argv[1]
    delete_character(id)

