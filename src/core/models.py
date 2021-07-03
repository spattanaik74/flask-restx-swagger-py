class Users:
    def __init__(self, name, place):
        self.name = name
        self.place = place

    def __repr__(self):
        return f'{"name":{self.name}, "place":{self.place}}'
