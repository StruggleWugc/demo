import sys
sys.path.append("..")
from common.driver import browser
import unittest
from common import variable


class test_web(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser(variable.Driver)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        # startUp(cls.driver, 1)   #通过获取类名来区分
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass
