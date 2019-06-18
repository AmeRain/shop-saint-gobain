from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from pages.CartPage import CartHelper
from pages.ComplexPage import ComplexHelper
from settings import chrome_driver


class App:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_driver)
        self.complex_helper = ComplexHelper(self)
        self.cart_helper = CartHelper(self)
        self.wait = WebDriverWait(self.driver, 3)

    def destroy(self):
        self.driver.quit()

    def wait_element(self, type_by, id_el):
        """
        Ждем появление элемента
        :param type_by: тип поиска selenium selenium.webdriver.common.by
        :param wait: фикстура ожидания елемента
        :param id_el: индентификатор элемента
        :return: инстанц элемента
        """
        wait = self.wait
        _web_el = None
        try:
            try:
                _web_el = wait.until(EC.element_to_be_clickable(
                    (type_by, id_el)))
            except:
                _web_el = wait.until(EC.presence_of_element_located(
                    (type_by, id_el)))

        except TimeoutException as e:
            raise Exception(
                "Ошибка: Элемент с '{}' => '{}' не найден.\n{}"
                    .format(type_by, id_el, e))
        wait._timeout = 3
        return _web_el

    def scroll_into_element(self, el):
        self.driver.execute_script("arguments[0].scrollIntoView();", el)