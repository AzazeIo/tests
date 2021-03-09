# Задача https://stepik.org/lesson/138920/step/8?unit=196194

class TestSearchWithXpath:
    def test_search_with_xpath(self, browser):
        browser.get("http://suninjuly.github.io/find_xpath_form")
        browser.find_element_by_tag_name("input").send_keys("Ivan")
        browser.find_element_by_name("last_name").send_keys("Petrov")
        browser.find_element_by_class_name("city").send_keys("Smolensk")
        browser.find_element_by_id("country").send_keys("Russia")
        browser.find_element_by_xpath('//form/div/button[@type="submit"]').click()