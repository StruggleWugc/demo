import sys
sys.path.append("..")
from page.RAMS_loginpage import Login_RA_MS

class RamsCreateType(Login_RA_MS):
	'''	实体类型/关联类型	'''
	#实体类型
	severmanage_clickloc =('css selector','#top_smManage')													#服务管理table
	entityType_clickloc = ("css selector",'#left_entityType')												#实体类型
	entity_createbuttonloc= ("css selector",'.listBar>.addNew')												#新增实体类型
	search_statusloc = ("css selector",'#enabledFlag')														#状态搜索 1正常，2停用
	search_entityloc = ('css selector','[name="entityTypeNameZh"][type="text"]')							#实体类型搜索
	search_buttonloc = ('css selector','.searchButton')														#搜索button
	table_entitynameloc = ('css selector','tbody>tr:nth-child(1)>td:nth-child(2)')							#列表实体类型名称
	table_entityviewloc =('css selector','tbody>tr:nth-child(1)>td:last-child>a[title="查看"]')				#列表查看
	table_entityeditloc =('css selector','tbody>tr:nth-child(1)>td:last-child>a[title="修改"]')				#列表编辑
	table_entitystoploc =('css selector','tbody>tr:nth-child(1)>td:last-child>a[title="停用"]')				#列表停用
	table_entitystartloc =('css selector','tbody>tr:nth-child(1)>td:last-child>a[title="启用"]')			#列表启用
	create_titleloc = ('css selector','.bread>a:last-child')												#新增实体标题/修改/关联/实体
	create_entitynameCnloc=('css selector','#entityTypeNameZh')												#实体名称中文/修改
	create_entityaboutCnloc=('css selector','#descriptionZh')												#实体描述中文/修改
	create_entitynameEnloc=('css selector','#entityTypeNameEn')												#实体名称英文/修改
	create_entityaboutEnloc=('css selector','#descriptionEn')												#实体描述英文/修改
	create_submitbuttonloc =('css selector',".submitBox>[value='确定']")									#确定按钮/修改
	create_savebuttonloc = ('css selector',".submitBox>[value='保存并继续']")								#保存并继续
	create_abolishbuttonloc = ('css selector',".submitBox>[value='取消']")									#取消/修改
	create_entitynameCnerrorloc = ('css selector',"[for='entityTypeNameZh']")								#实体类型名称错误
	create_entityaboutCnerrorloc = ('css selector','[for="descriptionZh"]')									#实体描述错误/修改
	create_entitynameEnerrorloc = ('css selector','[for="entityTypeNameEn"]')								#实体名称En错误
	create_entityaboutEnerrorloc = ('css selector','[for="descriptionEn"]')									#实体描述En错误/修改
	create_entitysubmittitleloc = ('css selector','.registrationBox>h5')									#创建实体保存并继续title
	create_entitysubmittipsloc =('css selector','#registerResult>span')										#创建提示信息
	create_entitysubmiloc =('css selector','.submitBox>[onclick="continueAdd()"]')							#继续创建
	entity_stoptipstitleloc = ('css selector','h5')															#实体停用title/启用
	entity_stoptipsloc =('css selector','.closeClear>span')													#实体停用提示/启用
	entity_stopsubmitloc =('css selector','.submit[value="确定"]')											#实体停用确定/启用
	entity_stopabolishloc = ('css selector','.reset[value="取消"]')											#实体停用取消/启用
	entity_renameCnerrorloc = ('css selector','#entityTypeNameZherror')										#修改中文实体名
	entity_renameEnerrorloc = ('css selector','#entityTypeNameZherrors')									#修改英文实体名

	#关联类型
	associationType_clickloc = ('css selector','#left_relevanceType')										#关联类型入口
	associationType_createbuttonloc = ('css selector','.listBar>a')											#新增入口
	search_associationstatusloc =  ("css selector",'#enabledFlag')											#状态搜索 1正常，2停用
	search_associationloc=('css selector','input[name="relevanceTypeNameZh"]')								#关联类型输入框
	search_sourceloc=('css selector','[name="sourceName"]')													#源类型输入框
	search_targetloc=('css selector','[name="targetName"]')													#目标类型输入框
	table_associationnameloc = ('css selector','tbody>tr:first-child>td:nth-child(2)')						#列表关联类型
	table_sourceloc =('css selector','tbody>tr:first-child>td:nth-child(3)')								#列表源类型
	table_targetloc = ('css selector','tbody>tr:first-child>td:nth-child(4)')								#列表目标类型
	table_assocviewloc =('css selector','tbody>tr:first-child>td:last-child>[title="查看"]')				#列表查看
	table_assoceditloc=('css selector','tbody>tr:first-child>td:last-child>[title="修改"]')					#列表修改
	table_assocstoploc =('css selector','tbody>tr:first-child>td:last-child>[title="停用"]')				#列表停用
	table_assocstartloc = ('css selector','tbody>tr:first-child>td:last-child>[title="启用"]')				#/启用
	association_stoptitleloc = ('css selector','h5')														#停用title/启用
	association_tipsloc =('css selector','#registerResult>span')											#停用tips/启用
	association_submitloc =('css selector','.submitBox>.submit')											#停用确认/启用
	association_abolishloc =('css selector','.submitBox>.reset')											#停用取消/启用
	create_associationnameCnloc =('css selector','#relevanceTypeNameZh')									#关联名中文
	create_sourcenameCnloc = ('css selector','#sourceTypeZh')												#源类型下拉框/修改
	create_targetnameCnloc = ('css selector','#targetTypeZh')												#目标类型下拉框/修改
	create_associationaboutCnloc =('css selector','#descriptionZh')											#描述中文/修改
	create_associationnameEnloc =('css selector','#relevanceTypeNameEn')									#关联名En
	create_sourcenameEnloc = ('css selector','#sourceTypeEn')												#源类型EN/修改
	create_targetnameEnloc = ('css selector','#targetTypeEn')												#目标类型En/修改
	create_associationaboutEnloc =('css selector','#descriptionEn')											#描述EN/修改
	error_associationnameCnloc =('css selector','[for="relevanceTypeNameZh"]')								#中文关联名错误/修改
	error_sourcenameCnloc = ('css selector','[for="sourceTypeZh"]')											#中文源类型错误
	error_targetnameCnloc = ('css selector','[for="targetTypeZh"]')											#中文目标类型错误
	error_associationaboutCnloc =('css selector','[for="descriptionZh"]')									#中文描述错误/修改
	error_associationnameEnloc =('css selector','[for="relevanceTypeNameEn"]')								#英文关联名错误/修改
	error_sourcenameEnloc = ('css selector','[for="sourceTypeEn"]')											#英文源类型错误
	error_targetnameEnloc = ('css selector','[for="targetTypeEn"]')											#英文目标类型错误
	error_associationaboutEnloc =('css selector','[for="descriptionEn"]')									#英文描述错误/修改
	error_associationnameOneCnloc =('css selector','#relevanceTypeNameZherror')								#新建中文名称重复
	error_associationnameOneEnloc =('css selector','#relevanceTypeNameEnerrors')							#新建英文名称重复
	association_createsubmitloc= ('css selector','.submit[value="确定"]')									#新增确定
	association_savebuttonloc = ('css selector','[onclick="save()"]')										#新增确定并继续
	association_createabolishloc = ('css selector','.reset[onclick="cancel()"]')							#新增取消
	association_savetitleloc =('css selector','h5')															#新增弹窗title
	association_savetipsloc =('css selector','#registerResult>span')										#新增弹窗提示
	association_framesubmitloc = ('css selector','[onclick="continueAdd()"]')								#新增弹窗保存
	association_renameCnloc =('css selector','[name="relevanceTypeNameZh"]')								#修改关联名中文
	association_renameEnloc =('css selector','[name="relevanceTypeNameEn"]')								#修改关联名英文


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

if __name__ =="__mian__":
	pass