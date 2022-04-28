
from src.request_files.request_parameters import BASE_URL
import requests


class GistsRequests:

    def post_gists(self, request_dto):
        url = BASE_URL
        request_dto._headers["Content-Type"] = "application/json"
        response_data = requests.request(method="POST", url=url, json=request_dto._body, headers=request_dto._headers)
        return response_data

    def delete_gist(self, request_dto):
        url = BASE_URL+"/"+request_dto._parameters
        response_data = requests.request(method="DELETE", url=url, headers=request_dto._headers)
        return response_data

    def read_gist(self, request_dto):
        url = BASE_URL+"/"+request_dto._parameters
        response_data = requests.request(method="GET", url=url, headers=request_dto._headers)
        return response_data

    def update_gist(self, request_dto):
        url = BASE_URL+"/"+request_dto._parameters
        response_data = requests.request(method="PATCH", url=url, json=request_dto._body, headers=request_dto._headers)
        return response_data