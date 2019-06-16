from page.RAMS_loginpage import Login_RA_MS

class SPmanage(Login_RA_MS):
	'''SP管理/审核'''

	sp_managetitle_loc =("css selector",'.bread>a:last-child')											#sp账户管理tips、查看、修改
	sp_manage2excel_loc = ("css selector",'.listBar>a')													#sp账户管理导出excel
	sp_manageTop_loc = ('id','top_spManage')															#sp管理table
	sp_manageleft_loc = ('id','left_serviceProviderAccounts')											#sp账户管理入口
	search_managename_loc = ("css selector",'.left>[name="email"]')										#用户名搜索
	search_managekind_loc = ('id','organizationTypeId')													#用户性质搜索
	search_managestatus_loc = ("css selector",'.left>[name="status"]')									#状态搜索
	search_managebutton_loc = ("css selector",'.searchButton')											#搜索按钮
	table_managename_loc = ("css selector",'tbody>tr:first-child>td:nth-child(2)')						#列表用户名
	table_managekind_loc = ("css selector",'tbody>tr:first-child>td:nth-child(4)')						#列表用户性质
	table_managestatus_loc =("css selector",'tbody>tr:first-child>td:nth-child(8)')						#列表用户状态
	table_manageview_loc= ("css selector",'tbody>tr:first-child>td:last-child>[title="查看"]')			#列表查看
	table_manageedit_loc = ("css selector",'tbody>tr:first-child>td:last-child>[title="修改"]')			#列表修改
	table_managestop_loc = ("css selector",'tbody>tr:first-child>td:last-child>[title="禁用"]')			#列表禁用
	table_managefrost_loc = ("css selector",'tbody>tr:first-child>td:last-child>[title="冻结"]')		#列表冻结
	table_managestart_loc = ("css selector",'tbody>tr:first-child>td:last-child>[title="启用"]')		#列表启用
	view_managename_loc = ('id','spid_email')															#查看用户名
	view_manamgedate_loc = ('id','spid_rgTime')															#注册时间
	view_managestatus_loc = ("css selector",'.detailList>dl:nth-of-type(3)>dd')							#查看状态
	view_managekind_loc = ('id','spid_organizationTypeDesc')											#查看性质
	view_managearea_loc = ('id','spid_areaName')														#所属区域
	view_manageorgname_loc = ('id','spid_orgName')														#查看机构名
	view_manageorgadd_loc = ('id','spid_orgAddress')													#机构注册地址
	view_manageorgid_loc = ('id','spid_idNumber')														#机构社会代码
	view_managewitsite_loc = ('id','spid_website')														#机构网址
	view_managelinkname_loc = ('id','spid_linkman')														#联系人姓名
	view_manageTel_loc = ('id','spid_phone')															#联系人固话
	view_managephone_loc = ('id','spid_mobile')															#联系人手机
	view_manageps_loc = ('id','spid_linkmanPosition')													#联系人职位
	view_managemail_loc=('id','spid_linkmanEmail')														#联系人邮箱
	view_manageadd_loc = ('id','spid_linkmanContact')													#联系人地址
	view_managezip_loc = ('id','spid_linkmanZip')														#联系人邮编
	view_managesubmit_loc = ("css selector",'.mr20')													#查看修改按钮
	alter_managename_loc = ("css selector",'.spList>dl:first-of-type>dd')								#修改用户名
	alter_managestatus_loc =("css selector",'.spList>dl:nth-of-type(3)>dd')								#修改-状态
	alter_manageorgname_loc = ('id','_org_name')														#修改-机构名
	alter_manageorglogo_loc = ('id','_logoFilePath')													#修改-机构logo
	alter_manageaddress_loc = ('id','_org_code')														#修改-注册地址
	alter_manageorgid_loc = ('id','_org_idNumber')														#修改-信用代码
	alter_manageorgidlogo_loc = ('id','_scanningCopyPath')												#修改-信用logo
	alter_managewebsite_loc = ('id','_org_website')														#修改-官方网址
	alter_managelinkname_loc = ("css selector",'[name="linkman"]')										#修改-联系人姓名
	alter_manageTel1_loc = ("css selector",'[name="phoneArea"]')										#修改-固话区号
	alter_manageTel2_loc = ("css selector",'[name="phone"]')											#修改-固话号码
	alter_manageTel3_loc = ("css selector",'[name="phoneExt"]')											#修改-固话分机号
	alter_managephone_loc = ("css selector",'[name="mobile"]')											#修改-手机号
	alter_manageps_loc = ("css selector",'[name="linkmanPosition"]')									#修改-联系人职位
	alter_manageemail_loc = ("css selector",'[name="linkmanEmail"]')									#修改-联系人邮箱
	alter_managelinkadd_loc = ("css selector",'[name="linkmanContact"]')								#修改-联系人地址
	alter_managezip_loc = ("css selector",'[name="linkmanZip"]')										#修改-联系人邮编
	alter_managesubmit_loc = ("css selector",'.centerButton>[value="修改并保存"]')						#修改-提交修改
	alter_alerttips_loc = ('id','changeStatusResultContent')											#修改弹窗提示
	alter_alertsubmit_loc = ("css selector",'[onclick="closeShowBox()"]')								#修改-弹窗确认
	alert_frostinput_loc = ('id','change_box_stauts_frez')												#冻结输入框
	alert_frostsubmit_loc = ("css selector",'[onclick="freezeConfirm()"]')								#冻结提交按钮
	alert_frosttips_loc = ('id','changeStatusInfoSpan2')												#冻结错误提示
	alert_stopinput_loc = ('id','change_box_stauts_disa')												#禁用输入框
	alert_stopsubmit_loc = ("css selector",'[onclick="disableConfirm();"]')								#禁用提交
	alert_stoptips_loc = ('id','changeStatusInfoSpan3')													#禁用提示
	alert_startinput_loc = ('id','change_box_stauts_open')												#禁用启用输入
	alert_startsubmit_loc = ("css selector",'[onclick="enableConfirm()"]')								#禁用启用button
	alert_starttips_loc = ('id','changeStatusInfoSpan1')												#禁用启用提示
	error_altermanagename_loc = ("css selector",'[for="_org_name"]')									#机构名错误
	error_altermanageorglogo_loc = ('id','_logoFilePath_error_text')									#机构logo错误
	error_altermanageaddress_loc = ("css selector",'[for="_org_code"]')									#机构地址错误
	error_altermanageorgid_loc = ("css selector",'[for="_org_idNumber"]')								#机构信用代码
	error_altermanageorgidlogo_loc =('id','_scanningCopyPath_error_text')								#机构信用代码logo
	error_alterlinkname_loc = ("css selector",'[for="linkman"]')										#机构联系人姓名
	error_altermanageTel_loc = ('id','phone_span_id')													#机构联系人电话
	error_altermanagephone_loc = ("css selector",'[for="mobile"]')										#机构联系人手机
	error_altermanagemail_loc =("css selector",'[for="linkmanEmail"]')									#机构联系人邮箱
	error_altermanageadd_loc = ("css selector",'[for="linkmanContact"]')								#机构联系人地址
	error_altermanagezip_loc = ("css selector",'[for="linkmanZip"]')									#机构联系人邮编

	sp_managecheckleft_loc = ("id",'left_serviceProviders')									#左侧账户审核
	sp_managechecktitle_loc = ("css selector",'.bread>a:nth-of-type(2)')								#账户审核title
	search_checkname_loc=("css selector",'[name="email"]')												#用户名搜索
	search_checkkind_loc = ('id','organizationTypeId')													#用户性质搜索
	search_checkstatus_loc = ("css selector",'.left>[name="status"]')									#用户状态搜索
	search_checkbutton_loc = ("css selector",'[value="搜索"]')											#搜索按钮
	table_spcheckname_loc = ("css selector",'tbody>tr:first-child>td:nth-child(2)')						#列表用户名
	table_spcheckstatus_loc =("css selector",'tbody>tr:first-child>td:nth-child(6)')					#列表用状态
	table_spcheckkind_loc =("css selector",'tbody>tr:first-child>td:nth-child(4)')						#列表用户性质
	table_spcheckview_loc =("css selector",'tbody>tr:first-child>td:last-child>[title="查看"]')			#列表查看
	table_spcheckagain_loc = ("css selector",'tbody>tr:first-child>td:last-child>[title="重发注册链接"]')	#列表重发链接
	table_spcheck_loc =("css selector",'tbody>tr:first-child>td:last-child>[title="审核"]')					#列表审核
	alert_checkagaintips_loc = ('id','registerResult')													#重发链接提示
	alert_checkagainbutton_loc = ("css selector",'[onclick="registerClose()"]')							#重发链接button
	alert_checkagree_loc =('id','yes')																	#审批同意
	alert_checkno_loc = ('id','no')																		#审批拒绝
	alert_checkinput_loc = ('id','auditOpinion')														#审批意见
	alert_checktips_loc = ('id','auditOpinionInfo')														#审批错误提示
	alert_checkbutton_loc = ('id','auditApplyId')
	alert_checkclose_loc = ("css selector",'.spBox>.spidClose')




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

if __name__=="__main__":
	pass