# Задача https://stepik.org/lesson/184253/step/4?unit=158843
import pyperclip as pyperclip
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


class TestAcceptAlert:
    def test_accept_alert(self, browser):
        browser.get("http://suninjuly.github.io/alert_accept.html")

        browser.find_element_by_css_selector("button.btn.btn-primary").click()
        confirm = browser.switch_to.alert
        confirm.accept()

        x = browser.find_element_by_id("input_value")
        x = x.text
        y = calc(x)

        browser.find_element_by_id("answer").send_keys(y)
        browser.find_element_by_css_selector("button.btn.btn-primary").click()

        alert = browser.switch_to.alert
        alert_text = alert.text
        addToClipBoard = alert_text.split(': ')[-1]
        pyperclip.copy(addToClipBoard)
