# import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(
    executable_path='./geckodriver.exe'
)
driver.get("http://10.10.10.48:8000/")
time.sleep(5)
elem = driver.find_element("csrfmiddlewaretoken")
time.sleep(5)
elem.send_keys("Тензор")
assert "No results found." not in driver.page_source
elem.send_keys(Keys.RETURN)
driver.close()


#
# class PythonOrgSearch(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome(
#             executable_path='./chromedriver.exe'
#         )
#
#     def test_search_in_python_org(self):
#         driver = self.driver
#         driver.get("http://www.yandex.ru")
#         elem = driver.find_element_by_name("input input_size_search input_theme_search")
#         elem.send_keys("Тензор")
#         assert "No results found." not in driver.page_source
#         elem.send_keys(Keys.RETURN)
#
#     def tearDown(self):
#         self.driver.close()
#
# if __name__ == "__main__":
#     unittest.main()