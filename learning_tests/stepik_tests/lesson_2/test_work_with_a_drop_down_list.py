# Задача https://stepik.org/lesson/228249/step/3?unit=200781
from selenium.webdriver.support.ui import Select


class TestWorkWithADropDownList:
    def test_work_with_a_drop_down_list(self, browser):
        link = "http://suninjuly.github.io/selects1.html"
        browser.get(link)

        x = browser.find_element_by_id("num1")
        x = x.text
        y = browser.find_element_by_id("num2")
        y = y.text
        s = (int(x) + int(y))

        select = Select(browser.find_element_by_id("dropdown"))
        select.select_by_value(f'{s}')
        browser.find_element_by_css_selector("button.btn.btn-default").click()
