import requests
from requests.auth import HTTPBasicAuth
import json

class TransactionBase(object):
    def __init__(self):
        self.user_token = None
        self.card_product_token = None
        self.card_token = None

    def create_user(self):
        data = '{"first_name": "Abhishek","last_name": "Krishna","active": true}'
        user = "18da7496-be57-4d36-abb5-00f53dd8bb17"
        password = "acda937f-6b95-4789-a1c8-613be4117c2b"
        response = requests.post("https://sandbox-api.marqeta.com/v3/users",
                                 headers={
                                     'content-type': 'application/json',
                                 },
                                 auth=HTTPBasicAuth(user, password),
                                 data=data)
        assert response.status_code == 201
        self.user_token = response.json()['token']
        return self

    def retrive_user(self):
        user = "18da7496-be57-4d36-abb5-00f53dd8bb17"
        password = "acda937f-6b95-4789-a1c8-613be4117c2b"
        response = requests.get("https://sandbox-api.marqeta.com/v3/users/"+self.user_token,
                                 headers={
                                     'content-type': 'application/json',
                                 },
                                 auth=HTTPBasicAuth(user, password))
        assert response.status_code == 200
        # print(json.dumps(response.json(), indent=4))
        return self

    def get_card_product(self):
        data = '{}'
        response = requests.get("https://sandbox-api.marqeta.com/v3/cardproducts",
                                headers={
                                    'content-type': 'application/json',
                                    'accept': 'application/json',
                                    'Authorization': 'Basic MThkYTc0OTYtYmU1Ny00ZDM2LWFiYjUtMDBmNTNkZDhiYjE3OmFjZGE5MzdmLTZiOTUtNDc4OS1hMWM4LTYxM2JlNDExN2MyYg=='
                                },
                                data=data)
        assert response.status_code == 200
        self.card_product_token = response.json()['data'][0]['token']
        return self

    def create_card(self):
        data = '{"user_token": "' + self.user_token + '" ,"card_product_token": "' + self.card_product_token + '"} '
        response = requests.post("https://sandbox-api.marqeta.com/v3/cards",
                                 headers={
                                     'content-type': 'application/json',
                                     'accept': 'application/json',
                                     'Authorization': 'Basic MThkYTc0OTYtYmU1Ny00ZDM2LWFiYjUtMDBmNTNkZDhiYjE3OmFjZGE5MzdmLTZiOTUtNDc4OS1hMWM4LTYxM2JlNDExN2MyYg=='
                                 },
                                 data=data)
        assert response.status_code == 201
        self.card_token = response.json()['token']
        return self

    def retrieve_card(self):
        response = requests.get("https://sandbox-api.marqeta.com/v3/cards/"+self.card_token,
                                 headers={
                                     'content-type': 'application/json',
                                     'accept': 'application/json',
                                     'Authorization': 'Basic MThkYTc0OTYtYmU1Ny00ZDM2LWFiYjUtMDBmNTNkZDhiYjE3OmFjZGE5MzdmLTZiOTUtNDc4OS1hMWM4LTYxM2JlNDExN2MyYg=='
                                 })
        assert response.status_code == 200
        return self

    def create_transaction(self):
        data = '{"amount": "10", "mid": "123456890","card_token": "' + self.card_token + '"} '
        response = requests.post("https://sandbox-api.marqeta.com/v3/simulate/authorization",
                                 headers={
                                     'content-type': 'application/json',
                                     'accept': 'application/json',
                                     'Authorization': 'Basic MThkYTc0OTYtYmU1Ny00ZDM2LWFiYjUtMDBmNTNkZDhiYjE3OmFjZGE5MzdmLTZiOTUtNDc4OS1hMWM4LTYxM2JlNDExN2MyYg=='
                                 },
                                 data=data)
        assert response.status_code == 201
        return self
