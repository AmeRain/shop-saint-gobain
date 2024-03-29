from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

from common.js_helper import scroll_into_element
from common.locators import Xpath
from common.wait_helper import wait_element
from settings import url_multicomfort

error_msg = "Ошибка при проверке стоимости пакета." \
            "Итоговая стоимость в {} отсутствует"


def test_fixation_cost_in_calc_and_cart(wait):
    """
    Заказ товаров из раздела https://shop.saint-gobain.ru/multicomfort (любой пакет)
    с фиксированием стоимости в калькуляторе и в корзине
    """
    try:
        wait._driver.get(url_multicomfort)
        sq_flat = wait_element(wait, By.XPATH, Xpath.Multicomfort.Flats.Calculator.XPATH_FIELD_SQUARE_FLAT)
        scroll_into_element(wait._driver, sq_flat)
        sq_flat.clear()
        sq_flat.send_keys(Keys.HOME)
        sq_flat.send_keys(80)
        calc_button = wait_element(wait, By.XPATH, Xpath.Multicomfort.Flats.Calculator.XPATH_BUTTON_CALCULATE)
        calc_button.click()
        time.sleep(1)
        wait_element(wait, By.XPATH, Xpath.Multicomfort.Flats.Calculator.XPATH_BLOCK_PACKAGE.format('1'))
        cost_in_calc = wait_element(wait, By.XPATH,
                                    Xpath.Multicomfort.Flats.Calculator.XPATH_BLOCK_PACKAGE_PRICE.format('1')).text
        assert cost_in_calc not in ['', None], error_msg.format('калькуляторе')
        buy_comfort = wait_element(wait, By.XPATH,
                                   Xpath.Multicomfort.Flats.Calculator.XPATH_BLOCK_PACKAGE_BUY.format('1'))
        buy_comfort.click()
        add_to_cart = wait_element(wait, By.XPATH, Xpath.Multicomfort.Flats.DetailsPackage.XPATH_ADD_TO_CART)
        scroll_into_element(wait._driver, add_to_cart)
        add_to_cart.click()
        cost_in_cart = wait_element(wait, By.XPATH, Xpath.Cart.XPATH_FINAL_COST).text
        assert cost_in_cart not in ['', None], error_msg.format('корзине')
    except Exception as e:
        raise Exception('Не удалось произвести проверку: \n {}'.format(e))


def test_fixation_cost_in_calc_and_cart_page_object(driver_page_object):
    """Предыдущий тест с использованием паттерна PageObject"""
    try:
        complex_helper = driver_page_object.complex_helper

        complex_helper.open_complex_solution()
        complex_helper.enter_square_flat(80)
        complex_helper.click_calculate_button()
        cost_in_calc = complex_helper.get_packages_price()
        assert cost_in_calc not in ['', None], error_msg.format('калькуляторе')

        complex_helper.click_button_buy_package()
        cart_helper = driver_page_object.cart_helper
        cart_helper.click_button_add_to_cart()
        cost_in_cart = cart_helper.get_final_cost()
        assert cost_in_cart not in ['', None], error_msg.format('корзине')
    except Exception as e:
        raise Exception('Не удалось произвести проверку: \n {}'.format(e))
