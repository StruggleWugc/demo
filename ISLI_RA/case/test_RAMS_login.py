import sys
# sys.path.append("..")
from page.RAMS_loginpage import Login_RA_MS
import unittest,time

class Rams_Login(unittest.TestCase):
	'''RA后台登陆'''
	@classmethod
	def setUpClass(cls):
		cls.driver = Login_RA_MS()
		cls.driver.open(Login_RA_MS.Ra_MS_url)
		cls.driver.select_language()

	def test_01(self):
		'''用户名为空'''
		self.driver.input_passwd("aaaaaa")
		self.driver.input_code('8888')
		self.driver.click_submit()
		self.assertEqual('请输入您的用户名',self.driver.get_error())

	def test_02(self):
		'''用户名不存在'''
		self.driver.input_usname('www')
		self.driver.click_submit()
		self.assertEqual('帐号不存在',self.driver.get_error())

	def test_03(self):
		'''密码为空'''
		# self.driver.input_passwd('')
		self.driver.input_code('8888')
		self.driver.click_submit()
		self.assertEqual('请输入密码',self.driver.get_error())

	def test_04(self):
		'''密码错误'''
		self.driver.input_usname('isli')
		self.driver.input_passwd('qqqqqq')
		self.driver.input_code('8888')
		self.driver.click_submit()
		self.assertEqual('密码错误',self.driver.get_error())

	def test_05(self):
		'''验证码为空'''
		self.driver.input_passwd('qqqqqq')
		self.driver.click_submit()
		self.assertEqual('请输入4位验证码',self.driver.get_error())

	def test_06(self):
		'''登入成功'''
		self.driver.input_passwd('aaaaaa')
		self.driver.input_code('8888')
		self.driver.click_submit()
		self.assertIn('或修改帐户密码',self.driver.get_text(('css selector','.warnTip')))


	@classmethod
	def tearDownClass(cls):
		cls.driver.close()

if __name__=="__main__":
	unittest.main()