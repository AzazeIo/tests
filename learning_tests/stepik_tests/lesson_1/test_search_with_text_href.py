# Задача https://stepik.org/lesson/138920/step/5?unit=196194

class TestSearchWithTextHref:
    def test_search_with_text_href(self, browser):
        browser.get("http://suninjuly.github.io/find_link_text")
        browser.find_element_by_link_text("224592").click()
        browser.find_element_by_tag_name("input").send_keys("Ivan")
        browser.find_element_by_name("last_name").send_keys("Petrov")
        browser.find_element_by_class_name("city").send_keys("Smolensk")
        browser.find_element_by_id("country").send_keys("Russia")
        browser.find_element_by_css_selector("button.btn").click()


