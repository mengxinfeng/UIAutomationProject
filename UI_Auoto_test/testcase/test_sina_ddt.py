import unittest,logging
from selenium import webdriver
from ddt import ddt, data, unpack


@ddt
class SinaLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://mail.sina.com.cn/')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    @data(('', '', u'请输入邮箱名'), ('', 'admin', u'请输入邮箱名'), ('admin', '', u'您输入的邮箱名格式不正确'))
    @unpack
    def test_login(self, username, password, result):
        '''验证新浪邮箱新浪的多种情况（一条用例对应多个测试点）'''
        self.driver.find_element_by_id('freename').send_keys(username)
        self.driver.find_element_by_id('freepassword').send_keys(password)
        # 点击登录
        self.driver.find_element_by_link_text('登录').click()
        # 获取异常信息
        div_text = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]').text
        res = self.assertEqual(div_text, result,msg='%s--不通过'%result)
        logging.info(msg=res)


if __name__ == '__main__':
    unittest.main(verbosity=2)
