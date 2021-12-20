import requests
from pprint import pprint


class ApiPrintall:

    @staticmethod
    def request(response):
        req_resp_data = f"""
           REQUEST
           url: {response.url}
           method: {response.request.method}
           headers: {response.request.headers}
           body: {response.request.body}

           RESPONSE
           headers: {response.headers}
           code: {response.status_code}
           body: {response.text}
           """

        pprint(req_resp_data)

        return response
