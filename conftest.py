import platform

import os
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

if 'Linux'.__eq__(platform.system()):
    chrome_driver = os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)), 'drivers', 'chromedriver')
else:
    chrome_driver = os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)), 'drivers', 'chromedriver.exe')


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
