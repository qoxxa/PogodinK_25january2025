from PogodinK_25january2025.test_api.BoardApi import SibdarApi
import allure


api = SibdarApi()


@allure.title("Добавить товар в корзину")
@allure.id(1)
@allure.severity("Blocker")
def test_add_to_cart(test_data):
    id = test_data.get("query_prod")
    type_prod = test_data.get("type_prod")
    type = type_prod['add']
    product = id | type
    add = api.cart(product)

    assert add.status_code == 200


@allure.title("Изменить количество товара +1")
@allure.id(2)
@allure.severity("Critical")
def test_change_the_quantity(test_data):
    id = test_data.get("query_prod")
    type_prod = test_data.get("type_prod")
    type = type_prod['plus']
    product = id | type
    add = api.cart(product)

    assert add.status_code == 200


@allure.title("Удалить товар из корзины")
@allure.id(3)
@allure.severity("Critical")
def test_delete(test_data):
    id = test_data.get("query_prod")
    type_prod = test_data.get("type_prod")
    type = type_prod['delete']
    product = id | type
    add = api.cart(product)

    assert add.status_code == 200
