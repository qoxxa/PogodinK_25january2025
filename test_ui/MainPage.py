from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from kinopoisk.DataProvider import DataProvider


class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = DataProvider().get('url')
        self.__driver = driver

    @allure.step("Перейти на сайт")
    def go(self) -> None:
        self.__driver.get(self.__url)

    @allure.step("Добавить товар в корзину")
    def add_to_cart(self):
        button = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, """div[id='bx_3218110189_204'] button[type='button']""")))
        button.click()

        self.__driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        button = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, """a[class='bask_btn_right'] div[class='bask_icon']""")))
        button.click()

    @allure.step("Изменить количество +1")
    def product_plus(self):
        button = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".plus_prod")))
        button.click()

    @allure.step("Удалить товар из корзины")
    def delete(self):
        button = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "img[src='/local/templates/sibdar_cust/img/close.png']")))
        button.click()

    @allure.step("Вернуть название продукта")
    def prod_title(self):
        txt = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#name_product_item_204")))
        return txt.text

    @allure.step("Вернуть сумму продукта")
    def prod_count(self):
        txt = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#total_price_product_item")))
        return txt.text

    @allure.step("Вернуть количество продукта")
    def prod_value(self):
        form_all_item = self.__driver.find_element(By.CLASS_NAME, "formAllItem")

        self.__driver.execute_script("arguments[0].style.display = 'block';", form_all_item)

        WebDriverWait(self.__driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, "//div[@id='total_price_product_item']"),
                                             "3840")
        )

        text_content = self.__driver.execute_script("""
            var element = document.querySelector('.formAllItem');
            return element.innerText;  // Или element.textContent
        """)

        return text_content

    @allure.step("Вернуть сообщение корзины")
    def cart_notification(self):
        price = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div[id='order-list'] h2")))
        return price.text

    @allure.step("Вернуть общую сумму корзины")
    def cart_all_count(self):
        WebDriverWait(self.__driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, "//div[@class='total_price_block']"), "Итого: 0 руб")
        )
        all_count = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".total_price_block")))
        return all_count.text
