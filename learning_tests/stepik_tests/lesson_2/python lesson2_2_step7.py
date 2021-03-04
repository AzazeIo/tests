from selenium import webdriver
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstName = browser.find_element_by_xpath("//div[@class='form-group']/input[1][@class='form-control']").send_keys("Ivan")
    lastName = browser.find_element_by_xpath("//div[@class='form-group']/input[2][@class='form-control']").send_keys("Petrov")
    eMail = browser.find_element_by_xpath("//div[@class='form-group']/input[3][@class='form-control']").send_keys("i.petrov@mail.ru")
    current_dir = os.path.abspath(os.path.dirname("/Users/Justy/Documents/file.txt"))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element_by_id("file").send_keys(file_path)
    submit = browser.find_element_by_css_selector("button.btn.btn-primary").click()

finally:
    time.sleep(4)
    browser.quit()
