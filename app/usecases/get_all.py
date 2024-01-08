import sys
sys.path.append('../')

from adapters.orm_adapter import Character
import adapters.db_interface as dbc

def get_all():
    char_list = list()
    try:
        all_characters = dbc.session.query(Character).all()
        if len(all_characters) > 0:
            for character in all_characters:
                char_list.append(character.to_dict())
            return 200, char_list
        else:
            print(Exception(f'No se encontraron personajes'))
            return 400, 'No se encontraron personajes'
    except Exception as error:
        print(f'Se encontro el siguiente error:\n{error}')
        return 400, error

if __name__ == '__main__':
        char_list = get_all()
        print(char_list)