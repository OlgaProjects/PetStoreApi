from config import Config
import pytest


@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_get_pets_positive(base_fixture, status):
    response = base_fixture.api.get_pets_by_status(status)
    resp_dict = response.json()
    print(resp_dict[0]['status'])
    base_fixture.print_all.print_all.request(response)


    assert resp_dict[0][
               'status'] == status, f'Поле status не соответствует ожидаемому {status}, ожидаемое - {resp_dict[0]["status"]}'
    return response
