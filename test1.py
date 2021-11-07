import time
import unittest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver




class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='./chromedriver.exe'
        )

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.yandex.ru")
        elem = driver.find_element(By.NAME, "text")
        elem.send_keys("Тензор")
        time.sleep(3)
        try:
            elem2 = driver.find_element(By.CSS_SELECTOR, '.mini-suggest__item')
        except TimeoutException:  # проверяем есть ли таблица с подсказками
            print('Нет таблицы с подсказками')

        elem.send_keys(Keys.ENTER)
        time.sleep(5)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()