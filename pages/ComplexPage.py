import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from common.locators import Xpath
from settings import url_multicomfort


class ComplexHelper:
    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

    def open_complex_solution(self):
        self.driver.get(url_multicomfort)

    def enter_square_flat(self, sq):
        sq_flat = self.app.wait_element(By.XPATH, Xpath.Multicomfort.Flats.Calculator.XPATH_FIELD_SQUARE_FLAT)
        self.app.scroll_into_element(sq_flat)
        sq_flat.clear()
        sq_flat.send_keys(Keys.HOME)
        sq_flat.send_keys(sq)

    def click_calculate_button(self):
        calc_button = self.app.wait_element(By.XPATH, Xpath.Multicomfort.Flats.Calculator.XPATH_BUTTON_CALCULATE)
        calc_button.click()
        time.sleep(1)

    def get_packages_price(self):
        self.app.wait_element(By.XPATH, Xpath.Multicomfort.Flats.Calculator.XPATH_BLOCK_PACKAGE.format('1'))
        return self.app.wait_element(By.XPATH,
                                     Xpath.Multicomfort.Flats.Calculator.XPATH_BLOCK_PACKAGE_PRICE.format('1')).text

    def click_button_buy_package(self):
        buy_comfort = self.app.wait_element(By.XPATH,
                                            Xpath.Multicomfort.Flats.Calculator.XPATH_BLOCK_PACKAGE_BUY.format('1'))
        buy_comfort.click()

