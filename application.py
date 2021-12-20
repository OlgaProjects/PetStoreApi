import pytest
from clients.pets import ApiPets
from helpers.helper import ApiHelp


class Application:
    def __init__(self):
        self.api = ApiPets()
        self.print_all = ApiHelp()
