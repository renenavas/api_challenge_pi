import sys
sys.path.append('../')

from entities.character import CharacterData
from adapters import orm_adapter as orm
import adapters.db_interface as dbc

def insert_character(name = None, height = None, mass = None, hair_color = None, skin_color = None, eye_color = None, birth_year = None):
    try:
        character_data_instance = CharacterData(name, height, mass, hair_color, skin_color, eye_color, birth_year)
        new_user = orm.to_orm(character_data_instance)
        dbc.session.add(new_user)
        dbc.session.commit()
        add_user_dict = new_user.to_dict()
        dbc.session.close()
        return 200, add_user_dict
    except Exception as error:
        print(f'Se encontro el siguiente error:\n{error}')
        return 400 , error

example = {
    'name': 'Test',
    'height': 166,
    'mass': 66,
    'hair_color': 'marron',
    'skin_color': 'moreno',
    'eye_color' : 'negros',
    'birth_year': 1995
    }




if __name__== '__main__':
    try:
        if len(sys.argv) == 1:
            char = insert_character(
                        name = example['name'],
                        height = example['height'],
                        mass = example['mass'],
                        hair_color = example['hair_color'],
                        skin_color = example['skin_color'],
                        eye_color = example['eye_color'],
                        birth_year = example['birth_year']
                        )
            print(char)
            if char[0] == 200:
                print(f'Se insertó exitosamente el personaje {char[1]}')
        elif len(sys.argv)-1 == len(example):
            char = insert_character(
                        name = sys.argv[1],
                        height = sys.argv[2],
                        mass = sys.argv[3],
                        hair_color = sys.argv[4],
                        skin_color = sys.argv[5],
                        eye_color = sys.argv[6],
                        birth_year = sys.argv[7]
                        )
            if char == 200:
                print(f'Se insertó exitosamente el personaje')
    except Exception as error:
            print(f'Se encontro el siguiente error:\n{error}')