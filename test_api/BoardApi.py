import requests
from PogodinK_25january2025.DataProvider import DataProvider
import allure


class SibdarApi:
    @allure.step('Запрос test_api')
    def __init__(self) -> None:
        self.url = DataProvider().get('url')

    @allure.step('Добавление в корзину')
    def cart(self, my_params: dict):
        resp = requests.post(self.url + 'ajax/basketOrder.php', params=my_params, cookies= DataProvider().get("cookie"))
        return resp
