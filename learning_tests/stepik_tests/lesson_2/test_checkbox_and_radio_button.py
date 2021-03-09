# Задача https://stepik.org/lesson/165493/step/7?unit=140087
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


class TestCheckboxAndRadiobutton:
    def test_checkbox_and_radio_button(self, browser):
        link = "http://suninjuly.github.io/get_attribute.html"
        browser.get(link)

        x = browser.find_element_by_id("treasure")
        x = x.get_attribute("valuex")
        y = calc(x)

        answer = browser.find_element_by_id("answer")
        answer.send_keys(y)
        browser.find_element_by_id("robotCheckbox").click()
        browser.find_element_by_id("robotsRule").click()
        browser.find_element_by_css_selector("button.btn.btn-default").click()