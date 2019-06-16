# from common.function import *
# from common.variable import *
from page.loginModular import loginModular
import unittest,time

class web_LoginTest(unittest.TestCase):
    '''web登入测试'''
    # variable.CurrentTest.append('web_LoginTest')
    @classmethod
    def setUpClass(cls):
        cls.t_login = loginModular()
        # cls.driver.open =(r'http://172.16.3.52:8080/irap/web/navigation/toLogin')
        cls.t_login.open(loginModular.url)

    @classmethod
    def tearDownClass(cls):
        cls.t_login.quit()

    def stest_01(self):
        '''成功登入'''
        print(variable.CurrentTest)
        # self.t_login = loginModular(self.driver)
        self.t_login.user_login_verify(username='sunsz@mpreader.com',password='aaaaaa', codecon='8888')
        self.assertEqual(self.t_login.login_success(),0)
        # self.assertEqual(self.driver.current_url,loginModular.url)
        # function.insert_img(self.driver,'pawd_empty.jpg')
        
    def test_02(self):
        '''全都不输入'''
        # t_login = loginModular(self.driver)
        self.t_login.user_login_verify()
        time.sleep(0.5)
        self.assertEqual(self.t_login.error_hint(),'请输入您的用户名/邮箱/ID')

    def test_03(self):
        '''不输入密码'''
        # t_login = loginModular(self.driver)
        self.t_login.user_login_verify(username='sunsz@mpreader.com',password='', codecon='8888')
        self.assertEqual(self.t_login.error_hint(),'请输入密码')
    
    def test_04(self):
        '''不输入验证码'''
        # t_login = loginModular(self.driver)
        self.t_login.user_login_verify(username='sunsz@mpreader.com', password='aaaaaa')
        self.assertEqual(self.t_login.error_hint(), '请输入4位验证码')
        
    def test_05(self):
        '''帐号不存在'''
        # t_login = loginModular(self.driver)
        self.t_login.user_login_verify(username='sunsz', password='aaaaaa', codecon='8888')
        self.assertEqual(self.t_login.error_hint(), '帐号不存在')
        
    def test_06(self):
        '''密码错误'''
        # t_login = loginModular(self.driver)
        self.t_login.user_login_verify(username='sunsz@mpreader.com', password='aaaaa', codecon='8888')
        self.assertEqual(self.t_login.error_hint(), '密码错误')
        
    def test_07(self):
        '''验证码不正确'''
        # t_login = loginModular(self.driver)
        self.t_login.user_login_verify(username='sunsz@mpreader.com', password='aaaaaa', codecon='888')
        self.assertEqual(self.t_login.error_hint(), '验证码不正确')
    
    def test_08(self):
        '''输入以前的密码'''
        # t_login = loginModular(self.driver)
        self.t_login.user_login_verify(username='sunsz@mpreader.com',password='a123456', codecon='8888')
        self.assertEqual(self.t_login.error_hint(),'密码错误')
    
    def test_09(self):
        '''用已经冻结的账号登入'''
        # t_login = loginModular(self.driver)
        self.t_login.user_login_verify(username='sunsz@mpreader',password='aaaaaa', codecon='8888')
        self.assertEqual(self.t_login.error_hint(),'帐号不存在')
        
    def test_10(self):
        '''用审核中的账号登入'''
        # t_login = loginModular(self.driver)
        self.t_login.user_login_verify(username='sunsz1@mpreader.com',password='aaaaaa', codecon='8888')
        self.assertEqual(self.t_login.error_hint(),'帐号不存在')
        
    def test_11(self):
        #验证码输入为空
        # t_login = loginModular(self.driver)
        self.t_login.user_login_verify(username='sunsz1@mpreader.com',password='aaaaaa', codecon='')
        self.assertEqual(self.t_login.error_hint(),'请输入4位验证码')

if __name__=="__main__":
    pass