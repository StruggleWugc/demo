import sys
sys.path.append("..")
from common import base
from page.RAMS_loginpage import Login_RA_MS
# a = Login_RA_MS()

class Rams_system(Login_RA_MS):
	###系统账户模块
	#系统账户新增
	hometitle_loc = ("css selector",'.warnTip')													#首页title
	homeusname_loc = ('id','username')															#首页用户名显示
	systemclick_loc = ("css selector",'#top_system')											#系统管理入口
	sys_accounts_loc = ('id','left_accountManage')												#系统账户按钮
	accounts_create_loc =("css selector",'.addNew')												#系统账户创建账户
	accounts_usname_loc =("id",'username')														#用户名
	accounts_jobno_loc =("id",'jobNo')															#工号
	accounts_name_loc =("id",'name')															#姓名
	accounts_tel_1_loc =("id",'telType')														#固话国家区号/修改
	accounts_tel_2_loc=("css selector",'[name="telArea"]')										#区号/修改
	accounts_tel_3_loc =("css selector",'[name="telNumber"]')									#固话号码/修改
	accounts_tel_4_loc=("css selector",'[name="telExt"]')										#分机号/修改
	accounts_phonecode_loc =("id",'mobileType')													#手机区号/修改
	accounts_phone_loc =("css selector",'[name="mobile"]')										#手机号/修改
	accounts_eamil_loc =("css selector",'[name="email"]')										#联系邮箱/修改
	accounts_pw1_loc =("id",'password')															#输入密码
	accounts_pw2_loc =("css selector",'[name="confirmPassword"]')								#确认密码
	accounts_sumbit_loc =("css selector",'.submit')												#确认按钮
	accounts_title_loc =("css selector",'.bread>a:last-child')									#创建页面title
	error_accountsusname_loc =("css selector",'[for="username"]')								#用户名错误信息
	error_accountsjbno_loc =("css selector",'[for="jobNo"]')									#工号错误信息/修改
	error_accountsname_loc =("css selector",'[for="name"]')										#姓名错误信息/修改
	error_accountsTel_loc = ("css selector",'[for="telNumber"]')								#固话错误信息
	error_accountsTel4_loc=("css selector",'[for="telExt"]')									#固话分机号错误
	error_alterTel_loc = ("css selector",'[for="telArea"]')										#修改时固话错误信息
	error_accountsMobile_loc =("css selector",'[for="mobile"]')									#手机错误信息/修改
	error_accountsemail_loc =("css selector",'[for="email"]')									#联系邮箱错误信息/修改
	error_accountspw1_loc = ("css selector",'[for="password"]')									#密码错误信息
	error_accountspw2_loc = ("css selector",'[for="confirmPassword"]')							#确认密码错误信息
	alter_accountsusname_loc = ("css selector",'[name="username"]')								#修改状态下用户名
	alter_accountsjobno_loc = ("css selector",'[name="jobNo"]')									#修改状态下工号
	alter_accountsname_loc = ("css selector",'[name="name"]')									#修改状态下姓名
	table_accountsusname_loc = ("css selector",'#table_tbody>tr:first-child>td:nth-child(2)')	#列表账户信息展示-用户名
	table_accountsjobno_loc =("css selector",'#table_tbody>tr:first-child>td:nth-child(3)') 	#列表账户信息展示-工号
	table_accountsrole_loc = ("css selector",'#table_tbody>tr:first-child>td:nth-child(4)') 	#列表账户信息展示-角色
	table_accountsname_loc = ("css selector",'#table_tbody>tr:first-child>td:nth-child(5)')		#列表账户信息展示-姓名
	table_accountsmobile_loc = ("css selector",'#table_tbody>tr:first-child>td:nth-child(6)') 	#列表账户信息展示-电话
	table_accountsemail_loc = ("css selector",'#table_tbody>tr:first-child>td:nth-child(7)') 	#列表账户信息展示-邮箱
	table_accountsstoptime_loc=("css selector",'#table_tbody>tr:first-child>td:nth-child(9)')	#列表账户信息展示-停用时间
	table_accountsstatus_loc = ("css selector",'#table_tbody>tr:first-child>td:nth-child(10)')	#列表账户信息展示-状态
	table_accountsedit_loc =("css selector",'#table_tbody>tr:first-child>td:last-child>.edit')			#列表中编辑
	table_accountsstop_loc =("css selector",'#table_tbody>tr:first-child>td:last-child>[title="停用"]')	#列表中停用
	table_accountsstart_loc=("css selector",'#table_tbody>tr:first-child>td:last-child>[title="启用"]')	#列表中启用
	table_accountsallot_loc =("css selector",'#table_tbody>tr:first-child>td:last-child>.role')			#列表中分配角色
	table_accountsdel_loc =("css selector",'#table_tbody>tr:first-child>td:last-child>[title="删除"]')	#列表中删除
	table_accountstitle_loc = ("css selector",'.bread>[href="accounts"]')								#列表title
	accounts_stopalerttips_loc = ("css selector",'.accountStop11>.clearfix>p')							#停用tips/启用
	accounts_stopsubmit_loc = ("css selector",'.centerButton>[onclick="disableAccount(this)"]')			#停用提交/启用
	accounts_deltips_loc = ("css selector",'.confirmDialog>.clearfix>p')								#删除提示
	accounts_delsubmit_loc = ("css selector",'.confirmDialog>.detailBox>.mt15>[value="确定"]')			#删除确认按钮
	accounts_rolealerttitleloc = ("css selector",'.accountRole>h5')										#角色分配title
	accounts_rolealertclick_loc = ("css selector",'.checkbox>[rolename="长期使用自动化权限"]')			#选择角色
	accounts_rolealertsubmit_loc = ("css selector",'.accountRole>.centerButton>.submit')				#角色分配提交
	exituser_button_loc = ("css selector",'.header>p>a')													#退出按钮


	######角色管理模块
	rolemanage_loc =("css selector",'#left_roleManage')											#角色管理入口
	rolecreate_loc =("css selector",'.listBar>.edit')											#创建角色
	roletitle_loc =("css selector",'.bread>a:last-child')										#角色创建弹窗title/修改
	roleareaCn_loc = ("css selector",'[name="areaId"]')											#中文区域/修改
	rolenameCn_loc = ("css selector",'[name="Rolename"]')										#中文角色名/修改
	roleaboutCn_loc = ("css selector",'[name="Desc"]')											#中文描述/修改
	roleareaEn_loc =("css selector",'[name="areaIdEn"]')										#英文区域/修改
	rolenameEn_loc = ("css selector",'[name="RolenameEn"]')										#英文角色名/修改
	roleaboutEn_loc = ("css selector",'[name="DescEn"]')										#英文描述/修改
	rolesubmit_loc = ("css selector",'.submit')													#提交/修改
	error_roleareaCn_loc =("css selector",'[for="areaId"]')										#中文区域错误/修改
	error_rolenameCn_loc =("css selector",'[for="Rolename"]')									#中文角色名错误/修改
	error_rolenameCnone_loc = ("css selector",'#RolenameZherror')								#中文名重复
	error_rolenameEnone_loc = ("css selector",'#RolenameEnerror')								#英文名重复
	error_roleareaEn_loc =("css selector",'[for="areaIdEn"]')									#英文区域错误/修改
	error_rolenameEn_loc =("css selector",'[for="RolenameEn"]')									#英文角色名错误/修改
	table_rolename_loc = ("css selector",'tbody>tr:first-child>td>pre')							#列表角色名和描述
	table_roleedit_loc =("css selector",'tbody>tr:first-child>td:last-child>[title="修改"]')	#修改
	table_roledel_loc = ("css selector",'tbody>tr:first-child>td:last-child>[title="删除"]')	#删除
	table_rolestop_loc = ("css selector",'tbody>tr:first-child>td:last-child>[title="停用"]')	#停用
	table_rolestart_loc = ("css selector",'tbody>tr:first-child>td:last-child>[title="启用"]')	#启用
	table_roletitle_loc = ("css selector",'.bread>[href="index"]')								#table页面标题
	stop_rolealerttips_loc =("css selector",'.detailBox>p')										#停用tips/启用/删除
	stop_rolealertbutton_loc =("css selector",'.mt15>[type="button"]')							#停用确认/启用/删除


###操作函数
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

	def login(self):
		self.login_success()

if __name__=="__main__":
	pass
