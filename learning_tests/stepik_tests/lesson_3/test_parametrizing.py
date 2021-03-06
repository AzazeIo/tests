# Задача https://stepik.org/lesson/237240/step/3?thread=solutions&unit=209628
import math
import time
import pytest


class TestParametrizing:
    @pytest.mark.parametrize(
        "link",
        [
            ("https://stepik.org/lesson/236895/step/1"),
            ("https://stepik.org/lesson/236896/step/1"),
            ("https://stepik.org/lesson/236897/step/1"),
            ("https://stepik.org/lesson/236898/step/1"),
            ("https://stepik.org/lesson/236899/step/1"),
            ("https://stepik.org/lesson/236903/step/1"),
            ("https://stepik.org/lesson/236904/step/1"),
            ("https://stepik.org/lesson/236905/step/1"),
        ],
    )
    def test_parametrizing(self, browser, link):
        browser.get(link)
        browser.implicitly_wait(5)
        answer = math.log(int(time.time()))
        browser.find_element_by_xpath('//textarea[@placeholder="Напишите ваш ответ здесь..."]').send_keys(f"{answer}")
        browser.find_element_by_css_selector("button.submit-submission").click()
        time.sleep(4)
        correct_text = browser.find_element_by_tag_name("pre").text

        assert correct_text == "Correct!"
