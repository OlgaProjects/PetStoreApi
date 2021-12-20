from clients.pets import ApiPets


class ApiPetStore:
    def __init__(self):
        self.pets = ApiPets()

