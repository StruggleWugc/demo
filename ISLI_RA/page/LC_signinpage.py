from common.base import BasePage

#LC登记者注册页面
class Signpage(BasePage):
	#页面元素--输入框

	sing_url = r"http://172.16.3.52:8080/irap/web/provider/toAdd"
	email_loc=("id","applyUserMail")  									#申请人邮箱
	name_loc=("id","applyUserName")   									#申请人姓名
	tel_loc_01_01_loc=("css selector",'.width35[name="applyUserTelOffice"]')   	#联系电话输入框一
	tel_loc_01_02_loc=("css selector",'.width190[name="applyUserTelOffice"]')  	#联系电话输入框二
	phone_01_loc=('id','applyUserTelPhone')   							#联系电话（手机）
	province_loc=("id","provinceId")									#出版单位省份
	affiliation_loc =("id","groupProperty")								#出版单位归属
	group_loc=("id","select2")											#集团下属出版单位
	publisherCn_loc=("id","publisherCn")								#出版单位中文名
	publisherEn_loc=("id","publisherEn")								#出版单位英文名
	creditcode_loc=("id","regno")										#统一社会信用代码
	book_loc =('id',"tushu")											#出版物资质-图书
	news_loc=('id','baozhi')											#出版物资质-报纸
	periodical_loc=('id','qikan')										#出版物资质-期刊
	video_loc=("id","yinxiang")											#出版物资质-音像
	electronic_loc =("id","dianzi")										#出版物资质-电子
	internet_loc =("id","internet")										#出版物资质-互联网
	bookrange_loc =("id","bookrange")									#出版物范围
	add_loc =("id","address")											#通讯地址
	zipcode_loc=("id","zipCode")										#邮政编码
	website_loc=("id","website")										#出版单位网址
	sponsor_loc=("id",'zbdw')											#主办单位
	organization_loc=("id","zgdw")										#主管单位
	legalPersonName_loc =("id","legalPersonName")						#法人代表姓名
	legal_tel_01_loc =("css selector",'[name="legalPersonTel"].width35')			#法人代表电话-1
	legal_tel_02_loc=("css selector",'[name="legalPersonTel"].width190')			#法人代表电话-2
	legal_phone_loc=("id","legalPersonMobile")							#法人代表手机
	legalPersonPost_loc = ("id","legalPersonPost")						#法人代表职务
	legalPersonFax_loc=("id","legalPersonFax")							#法人代表传真
	legalPersonMail_loc =("id","legalPersonMail")						#法人代表邮箱
	contactName_loc = ("id","contactName")								#联系姓名
	contact_tel_01_loc =("css selector",'[name="contactTel"].width35')			#联系人电话-1
	contact_tel_02_loc =("css selector",'[name="contactTel"].width190')			#联系人电话-2
	contactMobile_loc = ("id",'contactMobile')							#联系人手机
	contactPost_loc =("id","contactPost")								#联系人职务
	contactFax_loc =("id",'contactFax')									#联系人传真
	contactMail_loc =("id","contactMail")								#联系人邮箱
	btnsubmit_loc =("css selector",".btnOk")										#提交
	btnback_loc =("css selector",".btnBackh")									#返回上一步
	issn_1_loc=("css selector","#createqikanli1>dd>input:nth-child(1)")			#期刊issn输入框1
	issn_2_loc=("css selector","#createqikanli1>dd>input:nth-child(2)")			#期刊issn输入框2
	bookisbn_1_loc=("css selector","#createtushuli1>dd>input:nth-child(1)")      #图书isbn输入框1
	bookisbn_2_loc=("css selector","#createtushuli1>dd>input:nth-child(2)")      #图书isbn输入框2
	bookisbn_3_loc=("css selector","#createtushuli1>dd>input:nth-child(3)")      #图书isbn输入框3
	newscn_1_loc =("css selector","#createbaozhili1>dd>input:nth-child(1)")		#报纸cn输入框1
	newscn_2_loc =("css selector","#createbaozhili1>dd>input:nth-child(2)")		#报纸cn输入框2
	videoisbn_1_loc =("css selector","#createyinxiangli1>dd>input:nth-child(1)") #音像ISBN输入框1
	videoisbn_2_loc =("css selector","#createyinxiangli1>dd>input:nth-child(2)") #音像ISBN输入框2
	videoisbn_3_loc =("css selector","#createyinxiangli1>dd>input:nth-child(3)") #音像ISBN输入框3
	eleisbn_1_loc =("css selector","#createdianzili1>dd>input:nth-child(1)")     #电子出版物ISBN输入框1
	eleisbn_2_loc =("css selector","#createdianzili1>dd>input:nth-child(2)")     #电子出版物ISBN输入框2
	eleisbn_3_loc =("css selector","#createdianzili1>dd>input:nth-child(3)")     #电子出版物ISBN输入框3
	elecn_1_loc =("css selector","#createdianzicn1>dd>input:nth-child(1)")       #电子出版物cn输入框1
	elecn_2_loc =("css selector","#createdianzicn1>dd>input:nth-child(2)")       #电子出版物cn输入框2

	##错误提示
	email_error_loc =("css selector",'.error[for="applyUserMail"]')				#注册邮箱错误提示
	name_error_loc =("css selector",'.error[for="applyUserName"]')				#申请人姓名错误提示
	tel_error_loc =("css selector","#applyUserTelOfficeSpanId")   				#联系电话错误提示
	phone_error_loc =("css selector",'.error[for="applyUserTelPhone"]')			#联系手机错误提示
	province_erroe_loc =("css selector",'.error[for="provinceId"]')				#出版单位省份错误提示
	group_error_loc=("css selector",'.error[for="groupProperty"]')				#集团归属错误提示
	group_select_error_loc=("css selector",'.error[for="select2"]')				#集团选择错误
	publisherCn_error_loc =("css selector",'.error[for="publisherCn"]')			#出版单位中文名错误提示
	publisherEn_error_loc =("css selector",'.error[for="publisherEn"]')			#出版单位英文名错误提示
	creditcode_error_loc=("css selector",'.error#regnoSpan')					#统一社会信用代码错误提示
	apt_error_loc =("css selector",'#msgshow')									#出版物资质错误提示
	bookrange_error_loc =("css selector",'.error[for="bookrange"]')				#出版范围错误提示
	add_error_loc =("css selector",'.error[for="address"]')						#通讯地址错误提示
	zipcode_error_loc =("css selector",'.error[for="zipCode"]')					#邮编错误提示
	website_error_loc =("css selector",'.error[for="website"]')					#出版单位网址错误提示
	sponsor_error_loc =("css selector",'.error[for="zbdw"]')						#主办单位错误提示
	organization_error_loc =("css selector",'.error[for="zgdw"]')				#主管单位错误提示
	legalPersonName_error_loc =("css selector",'.error[for="legalPersonName"]')  #法人代表姓名错误提示
	legal_tel_error_loc = ("css selector",'#legalPersonTelSpanId')				#法人代表电话错误提示
	legal_phone_error_loc =("css selector",'.error[for="legalPersonMobile"]')	#法人代表手机错误提示
	legalPersonPost_error_loc =("css selector",'.error[for="legalPersonPost"]')  #法人代表职务错误提示
	legalPersonFax_error_loc =("css selector",'.error[for="legalPersonFax"]')    #法人代表传真错误提示
	legalPersonMail_error_loc =("css selector",'.error[for="legalPersonMail"]')  #法人代表邮箱错误提示
	contactName_error_loc =("css selector",'.error[for="contactName"]')			#联系人姓名错误提示
	contact_tel_error_loc =("css selector",'#contactTelSpanId')					#联系人电话错误提示
	contactMobile_error_loc =("css selector",'.error[for="contactMobile"]')		#联系人手机错误提示
	contactPost_error_loc =("css selector",'.error[for="contactPost"]')			#联系人职务错误提示
	contactFax_error_loc =("css selector",'.error[for="contactFax"]') 			#联系人传真错误提示
	contactMail_error_loc =("css selector",'.error[for="contactMail"]')			#联系人邮箱错误提示
	bookisbn_error_loc =("css selector",'#createtushuliisbns1')					#图书ISBN输入错误提示
	newscn_error_loc =("css selector",'#cnshow1')								#报纸CN输入错误提示
	issn_error_loc =("css selector",'#issnshow1')								#期刊ISSN错误提示
	videoisbn_error_loc =("css selector",'#createyinxiangliisbns1')				#音像ISBN错误提示
	eleisbn_error_loc =("css selector",'#createdianziliisbns1')					#电子出版物ISBN错误提示
	elecn_error_loc = ("css selector",'#electroniccnshow1')						#电子出版物CN错误提示

	def inputaction(self,locs,num):
		'''输入操作'''
		self.send_keys(locs,num)

	def input_eamil(self,useremail):
		'''输入注册邮箱'''
		self.send_keys(self.email_loc,useremail)

	def input_name(self,username):
		'''输入申请人姓名'''
		self.send_keys(self.name_loc,username)

	def input_tel_01(self,tel_1):
		'''输入联系电话第一段'''
		self.send_keys(self.tel_loc_01_01_loc,tel_1)

	def input_tel_02(self,tel_2):
		'''输入联系电话第二段'''
		self.send_keys(self.tel_loc_01_02_loc,tel_2)

	def input_phone_01(self,phone):
		'''输入电话号码（手机）'''
		self.send_keys(self.phone_01_loc,phone)

	def input_province(self,value):
		'''选择出版单位省份'''
		self.select_by_value(self.province_loc,value)

	def input_affiliation(self,value):
		'''选择出版单位归属
		0   独立出版社     1     集团下属出版单位      2   集团
		'''
		self.select_by_value(self.affiliation_loc,value)

	def input_group(self,value):
		'''集团下属出版单位选择所属集团       50000172    50000173  50000167'''
		self.select_by_value(self.group_loc,value)

	def input_publisherCn(self,publisherCn):
		'''输入出版社中文名称'''
		self.send_keys(self.publisherCn_loc,publisherCn)

	def input_publisherEn(self,publisherEn):
		'''输入出版社英文名称'''
		self.send_keys(self.publisherEn_loc,publisherEn)

	def input_creditcode(self,creditcode):
		"""输入统一社会信用代码"""
		self.send_keys(self.creditcode_loc,creditcode)

	def click_book(self):
		"""出版物资质勾选图书"""
		self.click(self.book_loc)

	def click_news(self):
		'''出版物资质勾选报纸'''
		self.click(self.news_loc)

	def click_periodical(self):
		'''出版物资质勾选期刊'''
		self.click(self.periodical_loc)

	def click_video(self):
		'''出版物勾选音像'''
		self.click(self.video_loc)

	def click_ele(self):
		'''出版物资质勾选电子出版物'''
		self.click(self.electronic_loc)

	def click_internet(self):
		'''出版物资质勾选互联网出版物'''
		self.click(self.internet_loc)

	def input_bookrange(self,bookrange):
		'''输入出版物范围'''
		self.send_keys(self.bookrange_loc,bookrange)

	def input_add(self,add):
		'''输入通讯地址'''
		self.send_keys(self.add_loc,add)

	def input_zipcode(self,zipcode):
		'''输入邮政编码'''
		self.send_keys(self.zipcode_loc,zipcode)

	def input_website(self,website):
		'''输入出版单位网址'''
		self.send_keys(self.website_loc,website)

	def input_sponsor(self,sponsor):
		'''输入主办单位'''
		self.send_keys(self.sponsor_loc,sponsor)

	def input_organ(self,organ):
		'''输入主管单位'''
		self.send_keys(self.organization_loc,organ)

	def input_lpname(self,lpname):
		'''输入法人代表姓名'''
		self.send_keys(self.legalPersonName_loc,lpname)

	def input_lptel_1(self,lptel1):
		'''输入法人代表电话第一段'''
		self.send_keys(self.legal_tel_01_loc,lptel1)

	def input_lptel_2(self,lptel2):
		'''输入法人代表电话第二段'''
		self.send_keys(self.legal_tel_02_loc,lptel2)

	def input_lpphone(self,lpphone):
		'''输入法人代表手机号码'''
		self.send_keys(self.legal_phone_loc,lpphone)

	def input_lppost(self,lppost):
		'''输入法人代表职务'''
		self.send_keys(self.legalPersonPost_loc,lppost)

	def input_lpfax(self,lpfax):
		'''输入法人代表传真'''
		self.send_keys(self.legalPersonFax_loc,lpfax)

	def input_lpmail(self,lpmail):
		'''输入法人代表邮箱'''
		self.send_keys(self.legalPersonMail_loc,lpmail)

	def input_contactname(self,conname):
		'''输入联系人姓名'''
		self.send_keys(self.contactName_loc,conname)

	def input_contact_tel_1(self,contel1):
		'''输入联系人电话号码第一段'''
		self.send_keys(self.contact_tel_01_loc,contel1)

	def input_contact_tel_2(self,contel2):
		'''输入联系人电话号码第二段'''
		self.send_keys(self.contact_tel_02_loc,contel2)

	def input_contact_phone(self,conphone):
		'''输入联系人手机号码'''
		self.send_keys(self.contactMobile_loc,conphone)

	def input_contact_post(self,conpost):
		'''输入联系人职务'''
		self.send_keys(self.contactPost_loc,conpost)

	def input_contact_fax(self,confax):
		'''输入联系人传真'''
		self.send_keys(self.contactFax_loc,confax)

	def input_contact_mail(self,conmail):
		'''输入联系人邮箱'''
		self.send_keys(self.contactMail_loc,conmail)

	def click_submit(self):
		'''点击提交'''
		self.click(self.btnsubmit_loc)

	def click_back(self):
		'''点击返回上一页'''
		self.click(self.btnback_loc)

	def input_issn_1(self,issn1):
		'''输入期刊第一段'''
		self.send_keys(self.issn_1_loc,issn1)

	def input_issn_2(self,issn2):
		'''输入期刊第二段'''
		self.send_keys(self.issn_2_loc,issn2)

	def input_bookisbn_1(self,bookisbn1):
		'''输入图书ISBN第一段'''
		self.send_keys(self.bookisbn_1_loc,bookisbn1)


	def input_bookisbn_2(self,bookisbn2):
		'''输入图书ISBN第二段'''
		self.send_keys(self.bookisbn_2_loc,bookisbn2)

	def input_bookisbn_3(self,bookisbn3):
		'''输入图书ISBN第三段'''
		self.send_keys(self.bookisbn_3_loc,bookisbn3)

	def input_newscn_1(self,newcn1):
		'''输入报纸cn第一段'''
		self.send_keys(self.newscn_1_loc,newcn1)

	def input_newscn_2(self,newcn2):
		'''输入报纸cn第一段'''
		self.send_keys(self.newscn_2_loc,newcn2)

	def input_videoisbn_1(self,videoisbn1):
		'''输入音像ISBN输入框第一段'''
		self.send_keys(self.videoisbn_1_loc,videoisbn1)

	def input_videoisbn_2(self,videoisbn2):
		'''输入音像ISBN输入框第二段'''
		self.send_keys(self.videoisbn_2_loc,videoisbn2)

	def input_videoisbn_3(self,videoisbn3):
		'''输入音像ISBN输入框第三段'''
		self.send_keys(self.videoisbn_3_loc,videoisbn3)

	def input_eleisbn_1(self,eleisbn1):
		'''输入电子出版物isbn第一段'''
		self.send_keys(self.eleisbn_1_loc,eleisbn1)

	def input_eleisbn_2(self,eleisbn2):
		'''输入电子出版物isbn第二段'''
		self.send_keys(self.eleisbn_2_loc,eleisbn2)

	def input_eleisbn_3(self,eleisbn3):
		'''输入电子出版物isbn第三段'''
		self.send_keys(self.eleisbn_3_loc,eleisbn3)

	def input_elecn_1(self,elecn1):
		'''输入电子出版物cn第一段'''
		self.send_keys(self.elecn_1_loc,elecn1)

	def input_elecn_2(self,elecn2):
		'''输入电子出版物cn第二段'''
		self.send_keys(self.elecn_2_loc,elecn2)

	###错误信息定位
	def get_mail_error(self):
		'''获取邮箱错误信息'''
		return self.get_text(self.email_error_loc)

	def get_name_error(self):
		'''获取申请人姓名错误提示'''
		return self.get_text(self.name_error_loc)

	def get_tel_error(self):
		'''获取联系电话错误信息提示'''
		return self.get_text(self.tel_error_loc)

	def get_phone_error(self):
		'''获取联系电话（手机）错误提示'''
		return self.get_text(self.phone_error_loc)

	def get_province_error(self):
		'''获取出版单位省份错误提示'''
		return self.get_text(self.province_erroe_loc)

	def get_group_error(self):
		'''获取单位归属错误提示'''
		return self.get_text(self.group_error_loc)

	def get_group_select_error(self):
		'''获取归属集团错误提示'''
		return self.get_text(self.group_select_error_loc)

	def get_publishCn_error(self):
		'''获取出版单位名称中文错误提示'''
		return self.get_text(self.publisherCn_error_loc)

	def get_publishEn_error(self):
		'''获取出版单位英文错误提示'''
		return self.get_text(self.publisherEn_error_loc)

	def get_creditcode_error(self):
		'''获取统一社会信用代码错误提示信息'''
		return self.get_text(self.creditcode_error_loc)

	def get_apt_error(self):
		'''获取出版物资质错误提示信息'''
		return self.get_text(self.apt_error_loc)

	def get_bookrange_error(self):
		'''获取出版物范围错误提示'''
		return self.get_text(self.bookrange_error_loc)

	def get_add_error(self):
		'''获取通讯地址错误提示'''
		return self.get_text(self.add_error_loc)

	def get_zipcode_error(self):
		'''获取邮编错误提示'''
		return self.get_text(self.zipcode_error_loc)

	def get_website_error(self):
		'''获取出版单位网址错误提示'''
		return self.get_text(self.website_error_loc)

	def get_sponsor_error(self):
		'''获取主办单位错误提示'''
		return self.get_text(self.sponsor_error_loc)

	def get_organization_error(self):
		'''获取主管单位错误提示'''
		return self.get_text(self.organization_error_loc)

	def get_legalname_error(self):
		'''获取法人代表错误提示'''
		return self.get_text(self.legalPersonName_error_loc)

	def get_legaltel_error(self):
		'''获取法人代表电话错误提示'''
		return self.get_text(self.legal_tel_error_loc)

	def get_legalphone_error(self):
		'''获取法人代表手机错误提示'''
		return self.get_text(self.legal_phone_error_loc)

	def get_legalpost_error(self):
		'''获取法人代表职位错误提示'''
		return  self.get_text(self.legalPersonPost_error_loc)

	def get_legalfax_error(self):
		'''获取法人代表传真错误'''
		return self.get_text(self.legalPersonFax_error_loc)

	def get_legalmail_error(self):
		'''获取法人代表邮箱错误'''
		return self.get_text(self.legalPersonMail_error_loc)

	def get_contactname_error(self):
		'''获取联系人姓名错误'''
		return self.get_text(self.contactName_error_loc)

	def get_contacttel_error(self):
		'''获取联系人电话错误提示'''
		return self.get_text(self.contact_tel_error_loc)

	def get_contactmobile_error(self):
		'''获取联系人手机错误提示'''
		return self.get_text(self.contactMobile_error_loc)

	def get_contactpost_error(self):
		'''获取联系人职务错误提示'''
		return self.get_text(self.contactPost_error_loc)

	def get_contactfax_error(self):
		'''获取联系人传真错误提示'''
		return self.get_text(self.contactFax_error_loc)

	def get_contactmail_error(self):
		'''获取联系人邮箱错误提示'''
		return self.get_text(self.contactMail_error_loc)

	def get_bookisbn_error(self):
		'''获取图书isbn错误提示'''
		return self.get_text(self.bookisbn_error_loc)

	def get_newscn_error(self):
		'''获取报纸	CN错误提示'''
		return self.get_text(self.newscn_error_loc)

	def get_issn_error(self):
		'''获取期刊issn错误提示'''
		return self.get_text(self.issn_error_loc)

	def get_videoisbn_error(self):
		'''获取音视频isbn错误提示信息'''
		return self.get_text(self.videoisbn_error_loc)

	def get_eleisbn_error(self):
		'''获取电子出版物ISBN错误提示'''
		return self.get_text(self.eleisbn_error_loc)

	def get_eleicn_error(self):
		'''获取电子出版物CN错误提示'''
		return self.get_text(self.elecn_error_loc)


if __name__ =="__main__":
	pass