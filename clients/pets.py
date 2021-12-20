import requests
import copy
from config import Config
import json


class ApiPets:
    def __init__(self):
        self.url = Config.url
        self.default_headers = {"accept": "application/json"}

    def create_pet(self, name, photoUrls, status):
        api_method = Config.api_method_add_pets
        url = self.url + api_method

        headers = copy.deepcopy(self.default_headers)
        headers["content-type"] = "application/json"

        req_dict = {
            "id": id,
            "category": {
                "id": id,
                "name": name
            },
            "name": name,
            "photoUrls": [
                photoUrls
            ],
            "tags": [
                {
                    "id": id,
                    "name": name
                }
            ],
            "status": status
        }

        response = requests.post(url, headers=headers, json=req_dict)
        return response

    def delete_pet(self, id):
        api_method = Config.api_method_dell_pets + id
        url = self.url + api_method
        header = {'accept': 'application/json'}

        response = requests.delete(url, headers=header)

    def get_pets_by_status(self, status):
        api_method = Config.api_method_find_by_status + status
        url = self.url + api_method
        headers = {'accept': 'application/json'}

        response = requests.get(url, headers=headers)

        return response
