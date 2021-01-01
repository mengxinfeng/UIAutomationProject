import unittest
import time, os, logging
import HTMLTestRunner


def get_log():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename='./log/all.log',
                        filemode='a',)

    # 往屏幕上输出
    sh = logging.StreamHandler()
    logger = logging.getLogger()
    logger.addHandler(sh)


def run_testcase():
    '''获取所有的测试用例模块'''
    suit = unittest.TestLoader().discover(
        start_dir=os.path.dirname(__file__),
        pattern='test_*.py',
        top_level_dir=None
    )
    return suit


def get_now_time():
    '''获取当前时间'''
    return time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))


def run():
    filename = os.path.join(os.path.dirname(__file__), 'report', get_now_time() + 'report.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='UI自动化测试报告',
        description='UI自动化测试报告详情')
    runner.run(run_testcase())
    fp.close()


if __name__ == '__main__':
    # unittest.TextTestRunner(verbosity=2).run(run_testcase())
    # log = Logger('test-all.log',level='info')
    get_log()
    run()
