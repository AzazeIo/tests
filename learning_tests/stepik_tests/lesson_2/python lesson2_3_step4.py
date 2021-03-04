import pyperclip as pyperclip
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    buttonAccaept = browser.find_element_by_css_selector("button.btn.btn-primary").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id("input_value")
    x = x.text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn.btn-primary").click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

finally:
    time.sleep(4)
    browser.quit()
