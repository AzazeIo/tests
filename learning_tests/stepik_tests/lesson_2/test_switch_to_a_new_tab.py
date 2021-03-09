# Задача https://stepik.org/lesson/184253/step/6?unit=158843
import pyperclip
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


class TestSwitchToANewTab:
    def test_switch_to_a_new_tab(self, browser):
        browser.get("http://suninjuly.github.io/redirect_accept.html")

        TrollButton = browser.find_element_by_css_selector("button.trollface.btn.btn-primary")
        window_before = browser.window_handles[0]
        TrollButton.click()
        window_after = browser.window_handles[1]
        time.sleep(10)
        browser.switch_to_window(window_after)

        x = browser.find_element_by_id("input_value")
        x = x.text
        y = calc(x)
        browser.find_element_by_id("answer").send_keys(y)
        browser.find_element_by_css_selector("button.btn.btn-primary").click()

        alert = browser.switch_to.alert
        alert_text = alert.text
        addToClipBoard = alert_text.split(': ')[-1]
        pyperclip.copy(addToClipBoard)



