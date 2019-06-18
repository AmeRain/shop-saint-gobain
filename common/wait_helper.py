from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


def wait_element(wait, type_by, id_el):
    """
    Ждем появление элемента
    :param type_by: тип поиска selenium selenium.webdriver.common.by
    :param wait: фикстура ожидания елемента
    :param id_el: индентификатор элемента
    :return: инстанц элемента
    """
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
