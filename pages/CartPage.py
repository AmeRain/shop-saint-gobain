from selenium.webdriver.common.by import By

from common.locators import Xpath


class CartHelper:
    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

    def click_button_add_to_cart(self):
        add_to_cart = self.app.wait_element(By.XPATH, Xpath.Multicomfort.Flats.DetailsPackage.XPATH_ADD_TO_CART)
        self.app.scroll_into_element(add_to_cart)
        add_to_cart.click()

    def get_final_cost(self):
        return self.app.wait_element(By.XPATH, Xpath.Cart.XPATH_FINAL_COST).text
