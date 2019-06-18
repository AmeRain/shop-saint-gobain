class Xpath:
    class Multicomfort:
        class Flats:
            class Calculator:
                XPATH_FIELD_SQUARE_FLAT = '//div[@class="control__field"]/input[@class="field_text js-calc__fld"]'
                XPATH_BUTTON_CALCULATE = '//div[@class="btn btn_main" and text()="рассчитать"]'
                XPATH_BLOCK_PACKAGE = '//div[@class="b-tarif c{}"]'
                XPATH_BLOCK_PACKAGE_PRICE = '//div[@class="b-tarif c{}"]/div[@class="b-tarif__price"]/span'
                XPATH_BLOCK_PACKAGE_BUY = '//div[@class="b-tarif c{}"]//div[@class="btn btn_block btn_main" and text()="купить"]'
            class DetailsPackage:
                XPATH_ADD_TO_CART = '//a[@class="btn btn_main sz_l" and text()="Добавить в корзину"]'
    class Cart:
        XPATH_FINAL_COST = '//div[@class="label" and contains(text(), "итого")]/following-sibling::div[@class="value"]/div'