class CharacterData:
    def __init__(self, name = None, height = None, mass = None, hair_color = None, skin_color = None, eye_color = None, birth_year = None):
        self.id = int()
        self.name = str(name)
        self.height = int(height)
        self.mass = int(mass)
        self.hair_color = str(hair_color)
        self.skin_color = str(skin_color)
        self.eye_color = str(eye_color)
        self.birth_year = int(birth_year)
    
    def to_dict(self):
        return {'id':self.id,
                'name':self.name,
                'height':self.height,
                'mass':self.mass,
                'hair_color':self.hair_color,
                'skin_color':self.skin_color,
                'eye_color':self.eye_color,
                'birth_year':self.birth_year,
                }