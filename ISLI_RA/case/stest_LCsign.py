# import sys
# sys.path.append("..")
import run_all
from page.LC_signinpage import Signpage

from common.read_excel import Read
import unittest
import time,os


class Login_test(unittest.TestCase):
	'''LC 注册'''
	@classmethod
	def setUpClass(cls):
		file_xpath = run_all.fppath+r'\date\ISLI_RA_signLCdata.xls'
		# print(file_xpath)
		cls.data = Read(file_xpath)
		cls.driver = Signpage()
		cls.driver.open(Signpage.sing_url)

	def test_001(self):
		'''邮箱格式错误'''
		self.driver.input_eamil(self.data.read_cell(2,1))
		self.driver.click_submit()
		self.assertEqual('邮箱不正确',self.driver.get_mail_error())

	def test_002(self):
		'''邮箱已注册'''

		self.driver.input_eamil(self.data.read_cell(3,1))
		self.driver.click_submit()
		self.assertEqual('邮箱已注册',self.driver.get_mail_error())

	def test_003(self):
		'''申请人姓名超过20字符'''
		self.driver.input_name(self.data.read_cell(4,2))
		self.driver.click_submit()
		self.assertIn('姓名最长为',self.driver.get_name_error())

	def test_004(self):
		'''验证电话号码输入框一为中文'''
		self.driver.input_tel_01(self.data.read_cell(5,3))
		self.driver.input_tel_02(self.data.read_cell(5,4))
		self.driver.click_submit()
		self.assertIn('输入1~4位数字',self.driver.get_tel_error())			#输入框一为中文

	def test_005(self):
		'''验证电话号码输入框一为空'''
		self.driver.input_tel_01(self.data.read_cell(6,3))
		self.driver.click_submit()
		self.assertIn('输入完整的固话',self.driver.get_tel_error())			#输入框一为空

	def test_006(self):
		'''验证电话号码输入框二为中文'''
		self.driver.input_tel_01(self.data.read_cell(7,3))
		self.driver.input_tel_02(self.data.read_cell(7,4))
		self.driver.click_submit()
		self.assertIn('输入6~11位数字',self.driver.get_tel_error())			#输入框二为中文

	def test_007(self):
		'''验证电话号码输入框二为空'''
		self.driver.input_tel_02(self.data.read_cell(8,4))
		self.driver.click_submit()
		self.assertIn('输入完整的固话',self.driver.get_tel_error())			#输入框二为空

	def test_008(self):
		'''验证电话号码输入框二小于6位'''
		self.driver.input_tel_02(self.data.read_cell(9,4))
		self.driver.click_submit()
		self.assertIn('输入6~11位数字',self.driver.get_tel_error())			#输入框二小于6位

	def test_009(self):
		'''联系电话手机超过11位'''
		self.driver.input_phone_01(self.data.read_cell(10,5))
		self.driver.click_submit()
		self.assertIn("联系电话（手机）不正",self.driver.get_phone_error())		#联系电话手机超过11位

	def test_010(self):
		'''联系电话手机小于11位'''
		self.driver.input_phone_01(self.data.read_cell(11,5))
		self.driver.click_submit()
		self.assertIn("联系电话（手机）不正",self.driver.get_phone_error())		#联系电话手机小于11位

	def test_011(self):
		'''联系电话手机非数字'''
		self.driver.input_phone_01(self.data.read_cell(12,5))
		self.driver.click_submit()
		self.assertIn("联系电话（手机）不正",self.driver.get_phone_error())		#联系电话手机非数字

	def test_012(self):
		"""选择出版单位省份"""
		###后期优化底层封装
		# self.driver.click_submit()
		# c = self.driver.is_exists(Signpage.province_erroe_loc)   				#未选择省份，提示信息存在
		# self.assertTrue(c)
		self.assertTrue(self.driver.is_visibility(Signpage.province_erroe_loc))
		self.driver.input_province('2')
		# b = self.driver.is_exists(Signpage.province_erroe_loc)					#选择省份之后，提示信息不存在
		# self.assertFalse(b)
		self.assertTrue(self.driver.is_invisibility(Signpage.province_erroe_loc))

	def test_013(self):
		'''选择出版单位归属'''
		###后期优化底层封装
		# self.driver.click_submit()
		# self.assertTrue(self.driver.is_exists(Signpage.group_error_loc))		#未选择出版单位归属，错误信息存在
		self.assertTrue(self.driver.is_visibility(Signpage.group_error_loc))		#封装后
		self.driver.input_affiliation('0')
		self.driver.click_submit()
		time.sleep(0.5)
		# self.assertFalse(self.driver.is_exists(Signpage.group_error_loc))		#选择独立出版社，错误提示不存在
		self.assertTrue(self.driver.is_invisibility(Signpage.group_error_loc))		#封装后

	def test_014(self):
		'''选择出版单位归属集团下属'''
		self.driver.input_affiliation('1')
		self.driver.click_submit()
		# self.assertTrue(self.driver.is_exists(Signpage.group_select_error_loc))		#选择集团下属出版社，错误信息存在
		self.assertTrue(self.driver.is_visibility(Signpage.group_select_error_loc))
		self.driver.input_group('50000172')
		# self.assertFalse(self.driver.is_exists(Signpage.group_select_error_loc))	#选择所属集团，错误信息不存在
		self.assertTrue(self.driver.is_invisibility(Signpage.group_select_error_loc))

	def test_015(self):
		'''出版单位中文名超过100字符长度'''
		self.driver.input_publisherCn(self.data.read_cell(14,9))
		self.driver.click_submit()
		self.assertIn("中文最长为100个",self.driver.get_publishCn_error())	#出版社中文名超过100字符长度

	def test_016(self):
		'''出版社英文长度超过500'''
		self.driver.input_publisherEn(self.data.read_cell(15,10))
		self.driver.click_submit()
		self.assertIn("单位名称英文最长为500个",self.driver.get_publishEn_error())

	def test_017(self):
		'''出版单位英文名不为数字或字母'''
		self.driver.input_publisherEn(self.data.read_cell(16,10))
		self.driver.click_submit()
		self.assertIn("只能输入英文",self.driver.get_publishEn_error())

	def test_018(self):
		'''统一社会代码非数字'''
		self.driver.input_creditcode(self.data.read_cell(17,11))			#统一社会代码非数字
		time.sleep(2)
		self.driver.click_submit()
		time.sleep(1)
		self.assertIn("输入15-18位数字或字母",self.driver.get_creditcode_error())

	def test_019(self):
		'''统一社会代码非15或18位'''
		self.driver.input_creditcode(self.data.read_cell(18,11))			#统一社会代码非15或18位
		self.driver.click_submit()
		time.sleep(1)
		self.assertIn("输入15-18位数字或字母",self.driver.get_creditcode_error())

	def test_020(self):
		'''出版范围超过200字符长度'''
		self.driver.input_bookrange(self.data.read_cell(19,12))
		self.driver.click_submit()
		self.assertIn("出版范围最长为200个",self.driver.get_bookrange_error())

	def test_021(self):
		'''通讯地址超过100字符长度'''
		self.driver.input_add(self.data.read_cell(20,13))
		self.driver.click_submit()
		self.assertIn("通讯地址最长为100个",self.driver.get_add_error())

	def test_022(self):
		'''邮编不为数字'''
		self.driver.input_zipcode(self.data.read_cell(21,14))
		self.driver.click_submit()
		self.assertIn("邮编不正",self.driver.get_zipcode_error())		#邮编不为数字

	def test_023(self):
		'''邮编小于六位'''
		self.driver.input_zipcode(self.data.read_cell(22,14))
		self.driver.click_submit()
		self.assertIn("邮编不正",self.driver.get_zipcode_error())		#邮编小于六位

	def test_024(self):
		'''邮编大于六位'''
		self.driver.input_zipcode(self.data.read_cell(23,14))
		self.driver.click_submit()
		self.assertIn("邮编不正",self.driver.get_zipcode_error())		#邮编大于六位

	def test_025(self):
		'''出版单位网址格式错误'''
		self.driver.input_website(self.data.read_cell(24,15))
		self.driver.click_submit()
		self.assertIn("网址不正确",self.driver.get_website_error())

	def test_026(self):
		'''主办单位超过100字符长度'''
		self.driver.input_sponsor(self.data.read_cell(25,16))
		self.driver.click_submit()
		self.assertIn("主办单位最长为100个",self.driver.get_sponsor_error())

	def test_027(self):
		'''主管单位超过100字符长度'''
		self.driver.input_organ(self.data.read_cell(26,17))
		self.driver.click_submit()
		self.assertIn("主管单位最长为100个字",self.driver.get_organization_error())

	def test_028(self):
		'''法人代表姓名超过20字符'''
		self.driver.input_lpname(self.data.read_cell(27,18))
		self.driver.click_submit()
		self.assertIn("法人代表姓名最长20个",self.driver.get_legalname_error())

	def test_029(self):
		'''法人代表电话输入框一位非数字'''
		self.driver.input_lptel_1(self.data.read_cell(28,19))
		self.driver.click_submit()
		time.sleep(1)
		self.assertIn('请输入1~4位数',self.driver.get_legaltel_error())			#法人代表电话输入框一位非数字

	def test_030(self):
		'''法人代表电话输入框一位空'''
		self.driver.input_lptel_1(self.data.read_cell(29,19))
		self.driver.input_lptel_2(self.data.read_cell(28,20))
		self.driver.click_submit()
		time.sleep(1)
		self.assertIn('请输入完整的固',self.driver.get_legaltel_error())		#法人代表电话输入框一位空

	def test_031(self):
		'''法人代表电话输入框二为非数字'''
		time.sleep(0.5)
		self.driver.input_lptel_1(self.data.read_cell(30,19))
		self.driver.input_lptel_2(self.data.read_cell(30,20))
		self.driver.click_submit()
		time.sleep(1.4)
		self.assertIn('请输入6~11位数',self.driver.get_legaltel_error())			#法人代表电话输入框二为非数字

	def test_032(self):
		'''法人代表电话输入框二为空'''
		self.driver.input_lptel_2(self.data.read_cell(31,20))
		self.driver.click_submit()
		time.sleep(1)
		self.assertIn('请输入完整的固',self.driver.get_legaltel_error())			#法人代表电话输入框二为空

	def test_033(self):
		'''法人代表电话输入框二小于6位'''
		self.driver.input_lptel_2(self.data.read_cell(32,20))
		self.driver.click_submit()
		time.sleep(0.5)
		self.assertIn('请输入6~11位',self.driver.get_legaltel_error())				#法人代表输入框二小于6位

	def test_034(self):
		'''法人代表手机非数字'''
		self.driver.input_lpphone(self.data.read_cell(33,21))
		self.driver.click_submit()
		self.assertIn('法人代表手机不',self.driver.get_legalphone_error())					#法人代表手机非数字

	def test_035(self):
		'''法人代表手机大于11位'''
		self.driver.input_lpphone(self.data.read_cell(34,21))
		self.driver.click_submit()
		self.assertIn('法人代表手机不',self.driver.get_legalphone_error())					#法人手机大于11位

	def test_036(self):
		'''法人代表手机小于11位'''
		self.driver.input_lpphone(self.data.read_cell(35,21))
		self.driver.click_submit()
		self.assertIn('法人代表手机不',self.driver.get_legalphone_error())					#法人手机小于11位

	def test_037(self):
		'''法人代表职务超过20字符'''
		self.driver.input_lppost(self.data.read_cell(36,22))
		self.driver.click_submit()
		self.assertIn('法人代表职位最长20个',self.driver.get_legalpost_error())

	def test_038(self):
		'''法人代表传真不为数字	'''
		self.driver.input_lpfax(self.data.read_cell(37,23))
		self.driver.click_submit()
		self.assertIn('法人代表传真不正',self.driver.get_legalfax_error())				#法人代表传真不为数字

	def test_039(self):
		'''法人代表传真不为数字	'''
		self.driver.input_lpfax(self.data.read_cell(38,23))
		self.driver.click_submit()
		self.assertIn('法人代表传真不正',self.driver.get_legalfax_error())				#法人代表传真小于7位

	def test_040(self):
		'''法人代表传真大于13位	'''
		self.driver.input_lpfax(self.data.read_cell(39,23))
		self.driver.click_submit()
		self.assertIn('法人代表传真不正',self.driver.get_legalfax_error())				#法人代表传真大于13位

	def test_041(self):
		'''法人代表邮箱格式不正确'''
		self.driver.input_lpmail(self.data.read_cell(40,24))
		self.driver.click_submit()
		self.assertIn('法人代表邮箱不正',self.driver.get_legalmail_error())

	def test_042(self):
		'''联系人姓名超过20字符'''
		self.driver.input_contactname(self.data.read_cell(41,25))
		self.driver.click_submit()
		self.assertIn("联系姓名最长20个",self.driver.get_contactname_error())

	def test_043(self):
		'''联系人电话输入框一位非数字'''
		time.sleep(0.5)
		self.driver.input_contact_tel_1(self.data.read_cell(42,26))
		self.driver.click_submit()
		time.sleep(1)
		self.assertIn('请输入1~4位数',self.driver.get_contacttel_error())			#联系人电话输入框一位非数字

	def test_044(self):
		'''联系人电话输入框一位空'''
		self.driver.input_contact_tel_1(self.data.read_cell(43,26))
		self.driver.input_contact_tel_2(self.data.read_cell(42,27))
		self.driver.click_submit()
		time.sleep(1)
		self.assertIn('请输入完整的固',self.driver.get_contacttel_error())		#联系人电话输入框一位空

	def test_045(self):
		'''联系人电话输入框二为非数字'''
		self.driver.input_contact_tel_1(self.data.read_cell(44,26))
		self.driver.input_contact_tel_2(self.data.read_cell(44,27))
		self.driver.click_submit()
		time.sleep(1)
		self.assertIn('请输入6~11位数',self.driver.get_contacttel_error())			#联系人电话输入框二为非数字

	def test_046(self):
		'''联系人电话输入框二为空'''
		self.driver.input_contact_tel_2(self.data.read_cell(45,27))
		self.driver.click_submit()
		time.sleep(1)
		self.assertIn('请输入完整的固',self.driver.get_contacttel_error())			#联系人电话输入框二为空

	def test_047(self):
		'''联系人电话输入框二小于6位'''
		self.driver.input_contact_tel_2(self.data.read_cell(46,27))
		self.driver.click_submit()
		self.assertIn('请输入6~11位',self.driver.get_contacttel_error())				#联系人电话输入框二小于6位

	def test_048(self):
		'''联系人手机非数字'''
		self.driver.input_contact_phone(self.data.read_cell(49,28))
		self.driver.click_submit()
		self.assertIn('联系人手机不正',self.driver.get_contactmobile_error())					#法人代表手机非数字

	def test_049(self):
		'''联系人手机大于11位'''
		self.driver.input_lpphone(self.data.read_cell(47,28))
		self.driver.click_submit()
		self.assertIn('联系人手机不正',self.driver.get_contactmobile_error())					#法人手机大于11位

	def test_050(self):
		'''联系人手机小于11位'''
		self.driver.input_lpphone(self.data.read_cell(48,28))
		self.driver.click_submit()
		self.assertIn('联系人手机不正',self.driver.get_contactmobile_error())					#法人手机小于11位

	def test_051(self):
		'''联系人职务超过20字符'''
		self.driver.input_contact_post(self.data.read_cell(50,29))
		self.driver.click_submit()
		self.assertIn('联系人职务最长20个',self.driver.get_contactpost_error())

	def test_052(self):
		'''联系人传真非数字'''
		self.driver.input_contact_fax(self.data.read_cell(51,30))
		self.driver.click_submit()
		self.assertIn('联系人传真不正',self.driver.get_contactfax_error())						#联系人传真非数字

	def test_053(self):
		'''联系人传真小于7位'''
		self.driver.input_contact_fax(self.data.read_cell(52,30))
		self.driver.click_submit()
		self.assertIn('联系人传真不正',self.driver.get_contactfax_error())						#联系人传真小于7位

	def test_054(self):
		'''联系人传真大于13位'''
		self.driver.input_contact_fax(self.data.read_cell(53,30))
		self.driver.click_submit()
		self.assertIn('联系人传真不正',self.driver.get_contactfax_error())								#联系人传真大于13位

	def test_055(self):
		'''联系人邮箱格式错误'''
		self.driver.input_contact_mail(self.data.read_cell(54,31))
		self.driver.click_submit()
		self.assertIn("联系人邮箱不正",self.driver.get_contactmail_error())

	def test_056(self):
		'''出版物资质勾选图书'''
		self.assertTrue(self.driver.is_invisibility(Signpage.bookisbn_1_loc))
		self.driver.click_book()
		# time.sleep(2)
		self.assertTrue(self.driver.is_visibility(Signpage.bookisbn_1_loc))

	def test_057(self):
		'''出版物资质勾选报纸'''
		self.assertTrue(self.driver.is_invisibility(Signpage.newscn_1_loc))
		self.driver.click_news()
		self.assertTrue(self.driver.is_visibility(Signpage.newscn_1_loc))

	def test_058(self):
		'''出版物资质勾选期刊'''
		self.assertTrue(self.driver.is_invisibility(Signpage.issn_1_loc))
		self.driver.click_periodical()
		self.assertTrue(self.driver.is_visibility(Signpage.issn_1_loc))

	def test_059(self):
		'''出版物资质勾选音像'''
		self.assertTrue(self.driver.is_invisibility(Signpage.videoisbn_1_loc))
		self.driver.click_video()
		self.assertTrue(self.driver.is_visibility(Signpage.videoisbn_1_loc))

	def test_060(self):
		'''出版物资质勾选电子出版物'''
		self.assertTrue(self.driver.is_invisibility(Signpage.eleisbn_1_loc))
		self.assertTrue(self.driver.is_invisibility(Signpage.elecn_1_loc))
		self.driver.click_ele()
		self.assertTrue(self.driver.is_visibility(Signpage.eleisbn_1_loc))
		self.assertTrue(self.driver.is_visibility(Signpage.elecn_1_loc))

	def test_061(self):
		'''图书isbn输入框一为空'''
		time.sleep(2)
		self.driver.input_bookisbn_1(self.data.read_cell(56,32))
		self.driver.input_bookisbn_2(self.data.read_cell(56,33))
		self.driver.input_bookisbn_3(self.data.read_cell(56,34))
		self.driver.click_submit()
		time.sleep(0.5)
		self.assertIn('请输入完整的ISBN',self.driver.get_bookisbn_error())

	def test_062(self):
		'''图书ISBN输入框二为空'''
		self.driver.input_bookisbn_1(self.data.read_cell(57,32))
		self.driver.input_bookisbn_2(self.data.read_cell(57,33))
		self.driver.click_submit()
		self.assertIn('请输入完整的ISBN',self.driver.get_bookisbn_error())

	def test_063(self):
		'''图书ISBN输入框三为空'''
		self.driver.input_bookisbn_2(self.data.read_cell(58,33))
		self.driver.input_bookisbn_3(self.data.read_cell(58,34))
		self.driver.click_submit()
		self.assertIn('请输入完整的ISBN',self.driver.get_bookisbn_error())

	def test_064(self):
		'''图书ISBN输入框一不为978/979'''
		self.driver.input_bookisbn_1(self.data.read_cell(55,32))
		self.driver.input_bookisbn_3(self.data.read_cell(55,34))
		self.driver.click_submit()
		self.assertIn('输入框一为978或979',self.driver.get_bookisbn_error())

	def test_065(self):
		'''图书ISBN输入框二超过1位'''
		self.driver.input_bookisbn_1(self.data.read_cell(59,32))
		self.driver.input_bookisbn_2(self.data.read_cell(59,33))
		self.driver.click_submit()
		self.assertIn('输入框二为1位的数',self.driver.get_bookisbn_error())

	def test_066(self):
		'''图书ISBN输入框二为非数字'''
		self.driver.input_bookisbn_2(self.data.read_cell(62,33))
		self.driver.click_submit()
		self.assertIn('输入框二为1位的数',self.driver.get_bookisbn_error())

	def test_067(self):
		'''图书ISBN输入框三小于2位'''
		self.driver.input_bookisbn_2(self.data.read_cell(60,33))
		self.driver.input_bookisbn_3(self.data.read_cell(60,34))
		self.driver.click_submit()
		self.assertIn('输入框三为2~7位',self.driver.get_bookisbn_error())

	def test_068(self):
		'''图书ISBN输入框三大于7位'''
		self.driver.input_bookisbn_3(self.data.read_cell(61,34))
		self.driver.click_submit()
		self.assertIn('输入框三为2~7位',self.driver.get_bookisbn_error())

	def test_069(self):
		'''图书ISBN输入框三非数字'''
		self.driver.input_bookisbn_3(self.data.read_cell(63,34))
		self.driver.click_submit()
		self.assertIn('输入框三为2~7位',self.driver.get_bookisbn_error())

	def test_070(self):
		'''报纸CN第一个输入框为空'''
		self.driver.input_newscn_1(self.data.read_cell(64,35))
		self.driver.input_newscn_2(self.data.read_cell(64,36))
		self.driver.click_submit()
		self.assertIn('请填写完整的（CN',self.driver.get_newscn_error())

	def test_071(self):
		'''报纸CN第一个输入框小于2位'''
		self.driver.input_newscn_1(self.data.read_cell(66,35))
		self.driver.click_submit()
		self.assertIn('输入框一长度为2位数',self.driver.get_newscn_error())

	def test_072(self):
		'''报纸CN第一个输入框大于2位'''
		self.driver.input_newscn_1(self.data.read_cell(67,35))
		self.driver.click_submit()
		self.assertIn('输入框一长度为2位数',self.driver.get_newscn_error())

	def test_073(self):
		'''报纸CN第一个输入框非数字'''
		self.driver.input_newscn_1(self.data.read_cell(68,35))
		self.driver.click_submit()
		self.assertIn('输入框一长度为2位数',self.driver.get_newscn_error())

	def test_074(self):
		'''报纸CN第二个输入框为空'''
		self.driver.input_newscn_1(self.data.read_cell(65,35))
		self.driver.input_newscn_2(self.data.read_cell(65,36))
		self.driver.click_submit()
		self.assertIn('请填写完整的（C',self.driver.get_newscn_error())

	def test_075(self):
		''''期刊ISSN输入框一为空'''
		self.driver.input_issn_1(self.data.read_cell(69,37))
		self.driver.input_issn_2(self.data.read_cell(69,38))
		self.driver.click_submit()
		self.assertIn('请填写完整的',self.driver.get_issn_error())

	def test_076(self):
		''''期刊ISSN输入框二为空'''
		self.driver.input_issn_1(self.data.read_cell(70,37))
		self.driver.input_issn_2(self.data.read_cell(70,38))
		self.driver.click_submit()
		self.assertIn('请填写完整的',self.driver.get_issn_error())

	def test_077(self):
		'''音像isbn输入框一为空'''
		self.driver.input_videoisbn_1(self.data.read_cell(79,42))
		self.driver.input_videoisbn_2(self.data.read_cell(79,43))
		self.driver.input_videoisbn_3(self.data.read_cell(79,44))
		self.driver.click_submit()
		self.assertIn('请输入完整的ISBN',self.driver.get_videoisbn_error())

	def test_078(self):
		'''音像ISBN输入框二为空'''
		self.driver.input_videoisbn_1(self.data.read_cell(80,42))
		self.driver.input_videoisbn_2(self.data.read_cell(80,43))
		self.driver.click_submit()
		self.assertIn('请输入完整的ISBN',self.driver.get_videoisbn_error())

	def test_079(self):
		'''音像ISBN输入框三为空'''
		self.driver.input_videoisbn_2(self.data.read_cell(81,43))
		self.driver.input_videoisbn_3(self.data.read_cell(81,44))
		self.driver.click_submit()
		self.assertIn('请输入完整的ISBN',self.driver.get_videoisbn_error())

	def test_080(self):
		'''音像ISBN输入框一不为978/979'''
		self.driver.input_videoisbn_1(self.data.read_cell(55,32))
		self.driver.input_videoisbn_3(self.data.read_cell(82,44))
		self.driver.click_submit()
		self.assertIn('输入框一为978或979',self.driver.get_videoisbn_error())

	def test_081(self):
		'''音像ISBN输入框二超过1位'''
		self.driver.input_videoisbn_1(self.data.read_cell(82,42))
		self.driver.input_videoisbn_2(self.data.read_cell(82,43))
		self.driver.click_submit()
		self.assertIn('输入框二为1位的数',self.driver.get_videoisbn_error())

	def test_082(self):
		'''音像ISBN输入框二为非数字'''
		self.driver.input_videoisbn_2(self.data.read_cell(85,43))
		self.driver.click_submit()
		self.assertIn('输入框二为1位的数',self.driver.get_videoisbn_error())

	def test_083(self):
		'''音像ISBN输入框三小于2位'''
		self.driver.input_videoisbn_2(self.data.read_cell(83,43))
		self.driver.input_videoisbn_3(self.data.read_cell(83,44))
		self.driver.click_submit()
		self.assertIn('输入框三为2~7位',self.driver.get_videoisbn_error())

	def test_084(self):
		'''音像ISBN输入框三大于7位'''
		self.driver.input_videoisbn_3(self.data.read_cell(84,44))
		self.driver.click_submit()
		self.assertIn('输入框三为2~7位',self.driver.get_videoisbn_error())

	def test_085(self):
		'''音像ISBN输入框三非数字'''
		self.driver.input_videoisbn_3(self.data.read_cell(86,44))
		self.driver.click_submit()
		self.assertIn('输入框三为2~7位',self.driver.get_videoisbn_error())

	def test_086(self):
		'''电子出版物CN第一个输入框为空'''
		self.driver.input_elecn_1(self.data.read_cell(87,45))
		self.driver.input_elecn_2(self.data.read_cell(87,46))
		self.driver.click_submit()
		self.assertIn('请填写完整的（CN',self.driver.get_eleicn_error())

	def test_087(self):
		'''电子出版物CN第一个输入框小于2位'''
		self.driver.input_elecn_1(self.data.read_cell(89,45))
		self.driver.click_submit()
		self.assertIn('输入框一长度为2位数',self.driver.get_eleicn_error())

	def test_088(self):
		'''电子出版物CN第一个输入框大于2位'''
		self.driver.input_elecn_1(self.data.read_cell(90,45))
		self.driver.click_submit()
		self.assertIn('输入框一长度为2位数',self.driver.get_eleicn_error())

	def test_089(self):
		'''电子出版物CN第一个输入框非数字'''
		self.driver.input_elecn_1(self.data.read_cell(91,45))
		self.driver.click_submit()
		self.assertIn('输入框一长度为2位数',self.driver.get_eleicn_error())

	def test_090(self):
		'''电子出版物CN第二个输入框为空'''
		self.driver.input_elecn_1(self.data.read_cell(88,45))
		self.driver.input_elecn_2(self.data.read_cell(88,46))
		self.driver.click_submit()
		self.assertIn('请填写完整的（C',self.driver.get_eleicn_error())

	def test_091(self):
		'''电子出版物isbn输入框一为空'''
		self.driver.input_eleisbn_1(self.data.read_cell(79,42))
		self.driver.input_eleisbn_2(self.data.read_cell(79,43))
		self.driver.input_eleisbn_3(self.data.read_cell(79,44))
		self.driver.click_submit()
		self.assertIn('请输入完整的ISBN',self.driver.get_eleisbn_error())

	def test_092(self):
		'''电子出版物ISBN输入框二为空'''
		self.driver.input_eleisbn_1(self.data.read_cell(80,42))
		self.driver.input_eleisbn_2(self.data.read_cell(80,43))
		self.driver.click_submit()
		self.assertIn('请输入完整的ISBN',self.driver.get_eleisbn_error())

	def test_093(self):
		'''电子出版物ISBN输入框三为空'''
		self.driver.input_eleisbn_2(self.data.read_cell(81,43))
		self.driver.input_eleisbn_3(self.data.read_cell(81,44))
		self.driver.click_submit()
		self.assertIn('请输入完整的ISBN',self.driver.get_eleisbn_error())

	def test_094(self):
		'''电子出版物ISBN输入框一不为978/979'''
		self.driver.input_eleisbn_1(self.data.read_cell(55,32))
		self.driver.input_eleisbn_3(self.data.read_cell(82,44))
		self.driver.click_submit()
		self.assertIn('输入框一为978或979',self.driver.get_eleisbn_error())

	def test_095(self):
		'''电子出版物ISBN输入框二超过1位'''
		self.driver.input_eleisbn_1(self.data.read_cell(82,42))
		self.driver.input_eleisbn_2(self.data.read_cell(82,43))
		self.driver.click_submit()
		self.assertIn('输入框二为1位的数',self.driver.get_eleisbn_error())

	def test_096(self):
		'''电子出版物ISBN输入框二为非数字'''
		self.driver.input_eleisbn_2(self.data.read_cell(85,43))
		self.driver.click_submit()
		self.assertIn('输入框二为1位的数',self.driver.get_eleisbn_error())

	def test_097(self):
		'''电子出版物ISBN输入框三小于2位'''
		self.driver.input_eleisbn_2(self.data.read_cell(83,43))
		self.driver.input_eleisbn_3(self.data.read_cell(83,44))
		self.driver.click_submit()
		self.assertIn('输入框三为2~7位',self.driver.get_eleisbn_error())

	def test_098(self):
		'''电子出版物ISBN输入框三大于7位'''
		self.driver.input_eleisbn_3(self.data.read_cell(84,44))
		self.driver.click_submit()
		self.assertIn('输入框三为2~7位',self.driver.get_eleisbn_error())

	def test_099(self):
		'''电子出版物ISBN输入框三非数字'''
		self.driver.input_eleisbn_3(self.data.read_cell(86,44))
		self.driver.click_submit()
		self.assertIn('输入框三为2~7位',self.driver.get_eleisbn_error())

	def test_100(self):
		'''返回上一步：注册协议界面'''
		self.driver.click_back()
		text = self.driver.get_text(('css selector','.btnBackh'))
		self.assertEqual('稍后再说',text)

	def test_101(self):
		'''协议页面跳转至信息填写页面'''
		self.driver.click(('css selector','.regBtnOk'))
		self.assertEqual('申请人信息',self.driver.get_text(('css selector','.regisBox>h3:nth-child(1)')))

	def test_102(self):
		'''单个必填项错误进行提交'''
		time.sleep(1)
		self.driver.input_eamil(self.data.read_cell(92,1))
		self.driver.input_name(self.data.read_cell(92,2))
		self.driver.input_phone_01(self.data.read_cell(92,5))
		self.driver.input_province(self.data.read_cell(92,6))
		self.driver.input_affiliation(self.data.read_cell(92,7))
		self.driver.input_publisherCn(self.data.read_cell(92,9))
		self.driver.input_publisherEn(self.data.read_cell(92,10))
		self.driver.input_creditcode(self.data.read_cell(92,11))
		self.driver.input_add(self.data.read_cell(92,13))
		self.driver.input_zipcode(self.data.read_cell(92,14))
		self.driver.input_sponsor(self.data.read_cell(92,16))
		self.driver.input_organ(self.data.read_cell(92,17))
		self.driver.input_lpname(self.data.read_cell(92,18))
		self.driver.input_contactname(self.data.read_cell(92,25))
		self.driver.input_contact_tel_1(self.data.read_cell(92,26))
		self.driver.input_contact_tel_2(self.data.read_cell(92,27))
		self.driver.input_contact_phone(self.data.read_cell(92,28))
		self.driver.input_contact_mail(self.data.read_cell(92,31))
		self.driver.click_book()
		self.driver.click_submit()
		self.assertEqual('邮箱不正确',self.driver.get_mail_error())

	def test_103(self):
		'''所有必填项输入正确'''
		time.sleep(1)
		self.driver.input_eamil(self.data.read_cell(93,1))
		self.driver.click_submit()
		self.assertEqual("ISLI关联标识符登记者（出版机构）注册表",self.driver.get_text(('css selector','.priH3')))

	def test_104(self):
		'''非必填项输入错误    --电话号码错误'''
		self.driver.click(('css selector','.btnBack'))
		self.driver.input_tel_01(self.data.read_cell(94,3))
		self.driver.input_tel_02(self.data.read_cell(94,4))
		self.driver.click_submit()
		self.assertEqual('请输入6~11位数字',self.driver.get_tel_error())

	def test_105(self):
		'''所有输入框正常输入注册'''
		self.driver.input_tel_02(self.data.read_cell(95,4))
		self.driver.input_affiliation(self.data.read_cell(95,7))
		self.driver.input_group(str(self.data.read_cell(95,8)))
		self.driver.input_bookrange(self.data.read_cell(95,12))
		self.driver.input_website(self.data.read_cell(95,15))
		self.driver.input_lptel_1(self.data.read_cell(95,19))
		self.driver.input_lptel_2(self.data.read_cell(95,20))
		self.driver.input_lpphone(self.data.read_cell(95,21))
		self.driver.input_lppost(self.data.read_cell(95,22))
		self.driver.input_lpfax(self.data.read_cell(95,23))
		self.driver.input_lpmail(self.data.read_cell(95,24))
		self.driver.input_contact_post(self.data.read_cell(95,29))
		self.driver.input_contact_fax(self.data.read_cell(95,30))
		self.driver.click_book()
		self.driver.click_news()
		self.driver.click_video()
		self.driver.click_ele()
		self.driver.click_periodical()
		self.driver.click_internet()
		self.driver.click_submit()
		self.assertEqual("ISLI关联标识符登记者（出版机构）注册表",self.driver.get_text(('css selector','.priH3')))

	def test_106(self):
		'''管理后台验证注册成功'''
		self.driver.open(r'https://172.16.5.162:8443/mpr/mcrs-system/mvc/syslogin/login')
		self.driver.inputaction(('id','userName'),'xuxuerlai')
		self.driver.inputaction(('id','passWord'),'123456')
		self.driver.inputaction(('id','codeCon'),'1234')
		self.driver.click(('id','login'))
		time.sleep(2)
		self.driver.click(('css selector','[title="出版者管理"]'))
		time.sleep(0.5)
		self.driver.switch_iframe(('id','j_menu'))
		self.driver.click(('css selector','.left-nav>[title="出版者申请管理"]'))
		self.driver.switch_iframe2default()
		time.sleep(0.5)
		self.driver.switch_iframe(('id','j_main'))
		time.sleep(0.5)
		self.assertEqual(self.data.read_cell(95,9),self.driver.get_text(('css selector','tbody>tr:first-child>[name="publisherCn"]>span')))

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()

if __name__=="__main__":
	unittest.main()
	# print(os.path.abspath('..\data\\')+'\ISLI_RA_signLCdata.xls')