import allure
from src.transaction_base import TransactionBase


class TestCreateTransaction(object):

    @allure.title("Marqeta API Test")
    def test_create_transaction(self):
        tb = TransactionBase()
        tb.create_user() \
            .retrive_user() \
            .get_card_product() \
            .create_card() \
            .retrieve_card() \
            .create_transaction()
