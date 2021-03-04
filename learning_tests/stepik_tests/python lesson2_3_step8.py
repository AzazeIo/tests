import math
import time
import pyperclip
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    buttonBook = browser.find_element_by_id("book").click()

    x = browser.find_element_by_id("input_value")
    calc = lambda x: str(math.log(abs(12 * math.sin(int(x)))))
    x = x.text
    y = calc(x)
    answer = browser.find_element_by_id("answer").send_keys(y)
    submitButton = browser.find_element_by_id("solve").click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

finally:
    time.sleep(4)
    browser.quit()