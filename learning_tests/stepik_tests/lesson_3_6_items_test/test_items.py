import time


class TestItems:
    def test_items(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(30)
        assert browser.find_element_by_class_name("btn-add-to-basket"),\
            "Кнопка добавления товара в корзину отсутсвует"


