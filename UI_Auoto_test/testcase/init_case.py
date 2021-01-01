import unittest
from selenium import webdriver


class InitCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.hao123.com/')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

