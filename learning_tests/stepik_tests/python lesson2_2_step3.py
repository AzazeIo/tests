from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser: WebDriver = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("num1")
    x = x.text
    y = browser.find_element_by_id("num2")
    y = y.text
    s = (int(x) + int(y))

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(f'{s}')
    button = browser.find_element_by_css_selector("button.btn.btn-default").click()

finally:
    time.sleep(4)
    browser.quit()
