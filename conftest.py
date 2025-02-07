import pytest
import allure
from selenium import webdriver
from PogodinK_25january2025.DataProvider import DataProvider


@pytest.fixture()
def browser():
    with allure.step("Открыть и настроить браузер"):
        timeout = DataProvider().getint('timeout')
        browser_name = DataProvider().get('browser_name')

        if browser_name == 'chrome':
            browser = webdriver.Chrome()
        else:
            browser_name == 'firefox'
            browser = webdriver.Firefox()

        browser.implicitly_wait(timeout)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture()
def test_data():
    return DataProvider()
