import sys
sys.path.append('../')

from adapters.orm_adapter import Character
import adapters.db_interface as dbc

def get_character_by_id(character_id):
    try:
        character = dbc.session.get(Character, character_id)
        dbc.session.close()
        if character:
            return 200, character.to_dict()
        else:
             print('No se encontró personaje')
             return 400, 'No se encontró personaje'
    except Exception as error:
            print(f'Se encontro el siguiente error:\n{error}')
            return 400, error

if __name__ == '__main__':
    if len(sys.argv) > 1:
        id = sys.argv[1]
    else:
        id = 1
    print(get_character_by_id(id))