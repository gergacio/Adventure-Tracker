class Country():
    def __init__(self, name, description, visit = False, id = None):
        self.name = name
        self.description = description
        self.cities = []
        self.visit = visit
        self.id = id