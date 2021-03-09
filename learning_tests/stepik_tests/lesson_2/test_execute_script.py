# Задача https://stepik.org/lesson/228249/step/6?unit=200781
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


class TestExecuteScript:
    def test_execute_script(self, browser):
        browser.get("http://SunInJuly.github.io/execute_script.html")
        x = browser.find_element_by_id("input_value")
        x = x.text
        y = calc(x)

        answer = browser.find_element_by_id("answer")
        answer.send_keys(y)
        checkbox = browser.find_element_by_id("robotCheckbox")
        checkbox.click()
        radiobutton = browser.find_element_by_id("robotsRule")
        browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
        radiobutton.click()
        button = browser.find_element_by_css_selector("button.btn.btn-primary")
        button.click()
