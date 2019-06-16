from page.RAMS_loginpage import Login_RA_MS

class Server(Login_RA_MS):
	'''服务管理-服务'''
	server_topbutton_loc = ('id','top_smManage')											#服务管理table
	server_leftbutton_loc = ('id','left_serviceInfo')										#左侧服务table
	server_tabletitle_loc = ("css selector",'.bread>a:nth-of-type(2)')						#服务页title
	server_newbutton_loc = ("css selector",'.listBar>a')									#新建按钮
	search_serverid_loc = ('id','serviceCodeZh')											#服务编码搜索框
	search_servername_loc = ("css selector",'[name="serviceNameZh"]')						#服务名称搜索框
	search_Association_loc = ("css selector",'[name="relevanceTypeNameZh"]')				#关联类型搜索
	search_button_loc = ("css selector",'.searchButton')									#搜索按钮
	table_server_loc = ("css selector",'tbody>tr:first-child>td:nth-child(2)')				#table服务名显示
	table_association_loc = ("css selector",'tbody>tr:first-child>td:nth-child(3)')			#table关联类型显示
	table_view_loc = ("css selector",'tbody>tr:first-child>td:last-child>[title="查看"]')	#table查看按钮
	table_edit_loc = ("css selector",'tbody>tr:first-child>td:last-child>[title="修改"]')	#table编辑按钮

	create_servertitle_loc = ("css selector",'.bread>a:last-child')							#新建title
	create_servernameCn_loc= ("css selector",'[name="serviceNameZh"]')						#中文-服务名
	create_serveridCn_loc = ('id','serviceCodeZh')											#中文-服务编码
	create_serveridbuttonCn_loc = ("css selector",'.detailList>dl:nth-of-type(2)>dd>a')		#中文-服务编码获取button
	create_serverassociationCn_loc = ("css selector",'[name="sendObject"]')					#中文-关联类型
	create_serverassocbuttonCn_loc = ("css selector",'.serviceList>dl:nth-of-type(3)>dd>div>a')			#中文-关联类型下拉
	create_serverassocbuttonEn_loc = ("css selector",'.serviceList>dl:nth-of-type(10)>dd>div>a')		#中文-关联类型下拉
	create_serverassocNo1Cn_loc = ("css selector",'.serviceList>dl:nth-of-type(3)>dd>div>div>ul>li:first-child>input')
	create_serverassocNo2Cn_loc = ("css selector",'.serviceList>dl:nth-of-type(3)>dd>div>div>ul>li:last-child>input')
	create_serverassocNo1En_loc = ("css selector",'.serviceList>dl:nth-of-type(10)>dd>div>div>ul>li:first-child>input')
	create_serverassocNo2En_loc = ("css selector",'.serviceList>dl:nth-of-type(10)>dd>div>div>ul>li:last-child>input')
	create_serverlongCn_loc = ('id','relevanceLengthZh')									#中文-长度
	create_serversectionCn_loc = ('id','relevanceNumZh')									#中文-分段
	create_serverfileCn_loc = ('id','_org_serviceWordUrlZh')								#中文-说明文件
	create_serverfileCnbutton_loc =('id','serviceWordUrlFilePath')							#中文-说明文件button
	create_serveraboutCn_loc =("css selector",'[name="descriptionZh"]')						#中文-说明
	create_serversectionsCn_loc = ("css selector",'[name="relevanceSubsectionZh"]')			#中文-分段段落（elements)
	create_serversectionsCn_1_loc = ("css selector",'#multi-input-Zh>input:first-child')	#中文-段落长度1
	create_serversectionsCn_2_loc = ("css selector",'#multi-input-Zh>input:last-child')		#中文-段落长度2
	create_servernameEn_loc= ("css selector",'[name="serviceNameEn"]')						#英文-服务名
	create_serveridEn_loc = ('id','serviceCodeEn')											#英文-服务编号
	create_serveridbuttonEn_loc = ("css selector",'.serviceList>dl:nth-of-type(9)>dd>a')	#英文-服务编码按钮
	create_serverassociationEn_loc = ("css selector",'[name="sendObjectEn"]')				#英文-关联类型
	create_serverlongEn_loc = ('id','relevanceLengthEn')									#英文-关联长度
	create_serversectionEn_loc = ('id','relevanceNumEn')									#英文-关联段落
	create_serversectionsEn_loc = ("css selector",'[name="relevanceSubsectionEn"]')			#英文-分段段落（elements)
	create_serversectionsEn_1_loc = ("css selector",'#multi-input-En>input:first-child')	#英文-关联段落长度1
	create_serversectionsEn_2_loc = ("css selector",'#multi-input-En>input:last-child')		#英文-关联段落长度2
	create_serverfileEn_loc = ('id','_org_serviceWordUrlEn')								#英文-说明文件
	create_serverfileEnbutton_loc =('id','serviceWordUrlFilePathEn')						#英文-说明文件button
	create_serveraboutEn_loc =("css selector",'[name="descriptionEn"]')						#英文-说明
	create_serverbutton_loc = ("css selector",'.mt25>[value="确定"]')						#确定按钮
	create_serveragain_loc = ('id','save')													#确定并继续按钮
	create_serveranolish_loc =("css selector",'[onclick="cancel()"]')						#取消按钮
	create_againtips_loc = ("css selector",'.mt25 >p>span')									#继续创建提示
	create_againbutton_loc = ("css selector",'[value="继续创建"]')							#继续创建按钮

	error_serverassocexitEn_loc = ('id','p_error_relevanceTypeEn')
	error_serverassocexitCn_loc = ('id','p_error_relevanceTypeZh')
	error_servernameexistCn_loc = ('id','p_error_serviceNameZh')							#中文服务名重复
	error_servernameexistEn_loc = ('id','p_error_serviceNameEn')							#英文服务名重复
	error_servernameCn_loc = ("css selector",'[for="serviceNameZh"]')						#服务名错误-中文
	error_serveridCn_loc = ("css selector",'[for="serviceCodeZh"]')							#服务id错误-中文
	error_serveridredoCn_loc = ('id','p_error_serviceCodeZh')								#服务id重复-中文
	error_serverassociationCn_loc = ("css selector",'[for="sendObject"]')					#服务关联类型错误-中文
	error_serverlongCn_loc = ("css selector",'[for="relevanceLengthZh"]')					#服务长度错误-中文
	error_serversectionNoCn_loc=("css selector",'[for="relevanceSubsectionZh"]')			#服务分段错误-中文
	error_serversectionsumCn_loc = ('id','relevanceNumZherror')
	error_serversectionsumEn_loc = ('id','relevanceNumEnerror')
	error_serverfileCn_loc = ('id','p_error_text')											#服务文件错误-中文
	error_serveraboutCn_loc = ("css selector",'[for="descriptionZh"]')						#服务简介错误-中文
	error_servernameEn_loc = ("css selector",'[for="serviceNameEn"]')						#服务名错误-英文
	error_serveridEn_loc = ("css selector",'[for="serviceCodeEn"]')							#服务id错误-英文
	error_serveridredoEn_loc = ('id','p_error_serviceCodeEn')								#服务id重复-英文
	error_serverassociationEn_loc = ("css selector",'[for="sendObjectEn"]')					#服务关联类型错误-英文
	error_serverlongEn_loc = ("css selector",'[for="relevanceLengthEn"]')					#服务长度错误-英文
	error_serversectionNoEn_loc=("css selector",'[for="relevanceSubsectionEn"]')			#服务分段错误-英文
	error_serverfileEn_loc = ('id','p_error_text_en')										#服务文件错误-英文
	error_serveraboutEn_loc = ("css selector",'[for="descriptionEn"]')						#服务简介错误-英文

	view_servertitle_loc = ("css selector",'.bread>a:last-child')							#查看title
	view_servernameCn_loc = ("css selector",'.detailList>dl:nth-of-type(1)>dd>span')		#查看-中文服务名
	view_serveridCn_loc = ("css selector",'.detailList>dl:nth-of-type(2)>dd>span')			#查看-中文服务编码
	view_serverlongCn_loc = ("css selector",'.detailList>dl:nth-of-type(3)>dd>span')		#查看-中文关联长度
	view_serversectionCn_loc = ("css selector",'.detailList>dl:nth-of-type(4)>dd>span')		#查看-中文关联分段
	view_serverfileCn_loc = ("css selector","css selector",'.detailList>dl:nth-of-type(5)>dd>.filename')	#查看-中文文件名
	view_serveraboutCn_loc = ("css selector",'.detailList>dl:nth-of-type(6)>dd>span')						#查看-中文简介
	view_serverassocCn_loc= ("css selector",'.detailList>table:nth-of-type(1)>tbody>tr:first-child>td:first-child')		#查看中文关联类型
	view_serversourceCn_loc = ("css selector",'.detailList>table:nth-of-type(1)>tbody>tr:first-child>td:nth-child(2)')	#查看中文源类型
	view_servertargetCn_loc = ("css selector",'.detailList>table:nth-of-type(1)>tbody>tr:first-child>td:last-child')	#查看中文目标类型
	view_servernameEn_loc = ("css selector",'.detailList>dl:nth-of-type(7)>dd>span')			#查看英文服务名
	view_serveridEn_loc = ("css selector",'.detailList>dl:nth-of-type(8)>dd>span')				#查看英文服务编码
	view_serverlongEn_loc = ("css selector",'.detailList>dl:nth-of-type(9)>dd>span')			#查看英文字段长度
	view_serversectionEn_loc = ("css selector",'.detailList>dl:nth-of-type(10)>dd>span')		#查看英文字段分段
	view_serverfileEn_loc = ("css selector",'.detailList>dl:nth-of-type(11)>dd>.filename')		#查看英文文件名
	view_serveraboutEn_loc = ("css selector",'.detailList>dl:nth-of-type(12)>dd>span')			#查看英文描述
	view_serverassocEn_loc= ("css selector",'.detailList>table:nth-of-type(2)>tbody>tr:first-child>td:first-child')		#查看英文关联类型
	view_serversourceEn_loc = ("css selector",'.detailList>table:nth-of-type(2)>tbody>tr:first-child>td:nth-child(2)')	#查看英文源类型
	view_servertargetEn_loc = ("css selector",'.detailList>table:nth-of-type(2)>tbody>tr:first-child>td:last-child')	#查看英文目标类型
	view_serveredit_loc=("css selector",'.ml180 >.mr20')										#查看修改按按钮
	alter_serverbutton_loc = ("css selector",'.ml180 >.submit')									#修改保存按钮


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