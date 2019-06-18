import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from application.App import App
from settings import chrome_driver


@pytest.fixture(scope='session')
def driver(request):
    browser = webdriver.Chrome(chrome_driver)

    def fin():
        browser.quit()

    request.addfinalizer(fin)
    return browser


@pytest.fixture(scope='session')
def wait(driver):
    waits = WebDriverWait(driver, 3)
    return waits


@pytest.fixture(scope='session')
def driver_page_object(request):
    app = App()

    def fin():
        app.destroy()

    request.addfinalizer(fin)
    return app
