# Задача https://stepik.org/lesson/228249/step/8?unit=200781
import os


class TestUploadFiles:
    def test_upload_files(self, browser):
        browser.get("http://suninjuly.github.io/file_input.html")

        browser.find_element_by_xpath("//div[@class='form-group']/input[1][@class='form-control']").send_keys("Ivan")
        browser.find_element_by_xpath("//div[@class='form-group']/input[2][@class='form-control']").send_keys("Petrov")
        browser.find_element_by_xpath("//div[@class='form-group']/input[3][@class='form-control']").send_keys("i.petrov@mail.ru")
        current_dir = os.path.abspath(os.path.dirname("/Users/Justy/Documents/file.txt"))
        file_path = os.path.join(current_dir, 'file.txt')
        browser.find_element_by_id("file").send_keys(file_path)
        browser.find_element_by_css_selector("button.btn.btn-primary").click()

