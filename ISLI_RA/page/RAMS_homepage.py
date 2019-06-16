from common import base
from page.RAMS_loginpage import Login_RA_MS

#RA后台管理首页修改
class RameHome(Login_RA_MS):
	home_tips_loc =("css selector",'.warnTip')														#首页提示
	home_name_loc = ('id','username')																#用户名显示
	home_jobno_loc=('id','jobno')																	#工号显示
	home_usernma_loc = ('id','realname')															#姓名显示
	home_tel_loc=('id','tel')																		#固话显示
	home_phone_loc = ('id','phone')																	#手机号显示
	home_email_loc = ('id','email')																	#邮箱显示
	home_alterbutton_loc = ("css selector",'[onclick="javascript:editAccount();"]')					#修改信息按钮
	home_alterpw_loc = ("css selector",'.btnl')														#修改密码按钮

	alter_tips_loc = ("css selector",'#editaccount>p:last-child')									#修改tips
	alter_name_loc = ("css selector",'#realname>input')												#姓名修改
	alter_tel_1_loc =("css selector",'#telType')													#固话国际区号修改
	alter_tel_2_loc=('id','telArea')																#固话区号修改
	alter_tel_3_loc = ('id','telNumber')															#固话号码
	alter_tel_4_loc = ('id','telExt')																#固话分机号
	alter_phone_1_loc=('id','mobileType')															#固话手机区号
	alter_phone_2_loc = ('id','mobile')																#固话手机号
	alter_email_loc = ("css selector",'#email>input')												#邮箱
	alter_button_loc=("css selector",'#confirmButtonEditAccount>input')								#修改保存

	error_altername_loc = ("css selector",'#realname>.errorWarn')									#姓名错误信息
	error_alterTel_loc = ("css selector",'#tel>.errorWarn')											#固话错误信息
	error_alterphone_loc = ("css selector",'#phone>.errorWarn')										#手机错误信息
	error_alteremail_loc = ("css selector",'#email>.errorWarn')										#邮箱错误信息

	pw_tips_loc = ("css selector",'.tips>.warnTip')													#密码修改tips
	pw_old_loc = ('id','currentPasswd')																#旧密码
	pw_new1_loc=('id','newPasswd1')																	#新密码
	pw_new2_loc =('id','newPasswd2')																#确认密码
	pw_button_loc = ('id','btnSubmit')																#密码修改确认button
	pw_alerttips_loc = ("css selector",'.detailBox>p')												#密码修改确认提示
	pw_alertbutton_loc = ('id','btnRelogin')														#密码修改确认button
	error_pw_old_loc = ("css selector",'#oldPasswordDD>label')										#旧密码错误信息
	error_pw_new1_loc = ("css selector",'[for="newPasswd1"]')										#新密码错误信息
	error_pw_new2_loc = ("css selector",'[for="newPasswd2"]')										#新密码确认错误
	exit_user_loc= ("css selector",'.header>p>a')													#用户退出

##操作函数
	def clickaction(self,element_loc):
		'''点击操作'''
		self.click(element_loc)

	def inputaction(self,element_loc,num):
		'''输入操作'''
		self.send_keys(element_loc,num)

	def get_about(self,element_loc):
		'''获取提示'''
		return self.get_text(element_loc)

	def selectaction(self,element_loc,index =0):
		'''下拉框擦操作'''
		self.select_by_index(element_loc,index =0)

	def selecttext(self,element_loc,value):
		'''下拉框擦操作'''
		self.select_by_text(element_loc,value)

	def clearaction(self,loc):
		'''清除输入框'''
		self.clearelement(loc)



