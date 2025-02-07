import allure
from PogodinK_25january2025.test_ui.MainPage import MainPage
from time import sleep


@allure.title("Добавление товара в корзину")
@allure.id(1)
@allure.severity("Blocker")
def test_add_to_cart(browser, test_data):
    prod_title = test_data.get("prod_title")
    ui = MainPage(browser)
    ui.go()
    ui.add_to_cart()
    ui.go_to_cart()
    title = ui.prod_title()

    with allure.step("Сравнение наименования заказываемого продукта, с продуктом в корзине"):
        assert prod_title == title
    sleep(5)


@allure.title("Изменение количества товара")
@allure.id(1)
@allure.severity("Critical")
def test_value(browser, test_data):
    prod_value = test_data.get("prod_value")
    ui = MainPage(browser)
    ui.go()
    ui.add_to_cart()
    ui.go_to_cart()
    ui.prod_title()
    ui.product_plus()
    value = ui.prod_value()
    value = value.strip().replace("\n", " ")

    print(value)
    with allure.step("Проверка наименования, количества, суммы и итоговой суммы заказываемого продукта"):
         assert prod_value == value
    sleep(5)


@allure.title("Удаление товара из корзины")
@allure.id(1)
@allure.severity("Blocker")
def test_delete(browser, test_data):
    cart = test_data.get("empty_cart_notification")
    count = test_data.get("all_count")
    ui = MainPage(browser)
    ui.go()
    ui.add_to_cart()
    ui.go_to_cart()
    ui.delete()

    notification = ui.cart_notification()
    all_count = ui.cart_all_count()

    assert 'Корзина пуста, необходимо это исправить' == cart
    with allure.step("Проверка сообщения, что корзина пуста"):
        assert cart == notification

    with allure.step("Проверка, что общая сумма равна 0"):
        assert count == all_count

    sleep(5)
