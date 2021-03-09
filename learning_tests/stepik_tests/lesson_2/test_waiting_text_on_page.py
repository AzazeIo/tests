# Задача https://stepik.org/lesson/181384/step/8?unit=156009
import math
import pyperclip
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWaitingTextOnPage:
    def test_waiting_text_on_page(self, browser):
        browser.get("http://suninjuly.github.io/explicit_wait2.html")

        WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
        browser.find_element_by_id("book").click()

        x = browser.find_element_by_id("input_value")
        calc = lambda x: str(math.log(abs(12 * math.sin(int(x)))))
        x = x.text
        y = calc(x)
        browser.find_element_by_id("answer").send_keys(y)
        browser.find_element_by_id("solve").click()

        alert = browser.switch_to.alert
        alert_text = alert.text
        addToClipBoard = alert_text.split(': ')[-1]
        pyperclip.copy(addToClipBoard)
