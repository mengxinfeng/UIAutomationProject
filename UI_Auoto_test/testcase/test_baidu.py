import unittest,logging
from selenium import webdriver


class BaiDuTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com/')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_baidu_title(self):
        '''验证：测试百度的标题是否正确：'''
        self.assertEqual(self.driver.title, '百度一下，你就知道')
        logging.info('ceshi')

    def test_news_url(self):
        '''验证：跳转百度新闻页面的URL是否正确：'''
        self.driver.find_element_by_link_text('新闻').click()
        current_window = self.driver.window_handles[1]
        self.driver.switch_to.window(current_window)
        self.assertEqual(self.driver.current_url, 'http://news.baidu.com/')
        logging.info('结果ceshi01')
        logging.error('dfaf')




if __name__ == '__main__':
    unittest.main(verbosity=2)
