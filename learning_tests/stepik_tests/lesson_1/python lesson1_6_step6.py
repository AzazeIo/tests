from selenium import webdriver
import time
import math

link = "https://fake-shop.com/book1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    add_button = browser.find_element_by_css_selector(".add")
    add_button.click()

    browser.get("https://fake-shop.com/book2.html")
    add_button = browser.find_element_by_css_selector(".add")
    add_button.click()
    browser.get("https://fake-shop.com/basket.html")
    goods = browser.find_elements_by_css_selector(".good")
    assert len(goods) == 2

finally:
    time.sleep(5)
    browser.quit()

