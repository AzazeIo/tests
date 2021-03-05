import time
import unittest

from selenium import webdriver


class TestAbs(unittest.TestCase):
    def test_one(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group first_class']/input").send_keys("Ivan")
        browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group second_class']/input").send_keys("Petrov")
        browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group third_class']/input").send_keys("ivan_petrov@yandex.ru")
        browser.find_element_by_css_selector("button.btn").click()
        time.sleep(5)
        welcome_text_elt = browser.find_element_by_xpath("/html/body/div/h1")
        welcome_text = welcome_text_elt.text
        self.assertNotEqual(welcome_text, "Not Found Welcome text")
        browser.quit()

    def test_two(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group first_class']/input").send_keys("Ivan")
        browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group second_class']/input").send_keys("Petrov")
        browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group third_class']/input").send_keys("ivan_petrov@yandex.ru")
        browser.find_element_by_css_selector("button.btn").click()
        time.sleep(5)
        welcome_text_elt = browser.find_element_by_xpath("/html/body/div/h1")
        welcome_text = welcome_text_elt.text
        self.assertNotEqual(welcome_text, "Not Found Welcome text")
        browser.quit()

        if __name__ == "__main__":
            unittest.main()