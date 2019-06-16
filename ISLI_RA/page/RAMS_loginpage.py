import sys,time
# sys.path.append("..")
from common import base

class Login_RA_MS(base.BasePage):
	Ra_MS_url = r"https://172.16.3.53:8443/isli/irms/manage-manager/base/login"
	usernam_loc = ('id','username')
	passwd_loc = ('id','password')
	valicode_loc= ('id','validCode')
	submit_loc = ("css selector",'[type="submit"]')
	error_loc=("css selector",'#error')
	language =('id','languageList')

	def select_language(self):
		'''语种选择'''
		self.select_by_value(self.language,'ZH_CN')
		time.sleep(0.5)


	def input_usname(self,usname):
		'''输入账号'''
		self.send_keys(self.usernam_loc,usname)

	def input_passwd(self,pw):
		'''输入密码'''
		self.send_keys(self.passwd_loc,pw)

	def input_code(self,code):
		'''输入验证码'''
		self.send_keys(self.valicode_loc,code)

	def click_submit(self):
		'''点击提交'''
		self.click(self.submit_loc)

	def get_error(self):
		'''获取错误信息'''
		return self.get_text(self.error_loc)

	def login_success(self,name='isli',pw='aaaaaa',code ='8888'):
		self.open(Login_RA_MS.Ra_MS_url)
		self.select_language()
		self.input_usname(name)
		self.input_passwd(pw)
		self.input_code(code)
		self.click_submit()

	def loginaction(self,name,pw,code='8888'):
		self.select_by_value(self.language,'ZH_CN')
		self.input_usname(name)
		self.input_passwd(pw)
		self.input_code(code)
		self.click_submit()

if __name__ =="__main__":
	pass

