# Задача https://stepik.org/lesson/36285/step/13?unit=162401
import time
import pytest


class TestMarkers:
    @pytest.mark.smoke
    def test_markers_one(self, browser):
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group first_class']/input").send_keys("Ivan")
        browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group second_class']/input").send_keys("Petrov")
        browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group third_class']/input").send_keys("ivan_petrov@yandex.ru")
        browser.find_element_by_css_selector("button.btn").click()
        time.sleep(2)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text

    @pytest.mark.xfail
    def test_markers_two(self, browser):
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group first_class']/input").send_keys("Ivan")
        browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group second_class']/input").send_keys("Petrov")
        browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group third_class']/input").send_keys("ivan_petrov@yandex.ru")
        browser.find_element_by_css_selector("button.btn").click()
        time.sleep(2)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text
