from application import Application
import pytest
from config import Config
from clients.api_helpers import ApiPetStore

fixture = Application()

@pytest.fixture(scope="session")
def base_fixture():
    return fixture

@pytest.fixture(scope="session")
def pet(request):
    def fin():
        fixture.api.delete_pet(Config.id)

    req = fixture.api.create_pet(Config.name, Config.photoUrls, Config.status_for_pet)
    Config.id = req.json()['id']

    request.addfinalizer(fin)
    return fixture
