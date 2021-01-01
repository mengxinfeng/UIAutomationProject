import unittest,logging
from selenium import webdriver


class Sina(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://mail.sina.com.cn/')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_login_null(self):
        '''验证新浪登录为空的情况：'''
        self.driver.find_element_by_id('freename').send_keys('')
        self.driver.find_element_by_id('freepassword').send_keys('')
        self.driver.find_element_by_class_name('loginBtn').click()
        null_err = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]').text

        self.assertEqual(null_err, '请输入邮箱名',msg='邮箱验证名为空提示信息不一致')


if __name__ == '__main__':
    unittest.main(verbosity=2)


