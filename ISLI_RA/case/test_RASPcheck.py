from page.RA_SPManagePage import SPmanage
from common.read_excel import Read
import run_all
import unittest,time,os


class Spcheck(unittest.TestCase):
	'''Sp账户审核'''

	@classmethod
	def setUpClass(cls):
		cls.file_path = os.path.join(run_all.fppath,'date')
		cls.data = Read(cls.file_path+r'\ISLI_RA_MS.xls')
		cls.driver = SPmanage()
		cls.driver.login_success()
		# cls.driver.clickaction(cls.driver.sp_manageTop_loc)
		# cls.driver.clickaction(cls.driver.sp_manageleft_loc)

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()


	def test_001(self):
		'''进入sp账户审核页面正常'''
		self.driver.clickaction(self.driver.sp_manageTop_loc)
		self.driver.clickaction(self.driver.sp_managecheckleft_loc)
		self.assertEqual("SP帐户审核",self.driver.get_about(self.driver.sp_managechecktitle_loc))
		self.assertEqual("导出 Excel",self.driver.get_about(self.driver.sp_manage2excel_loc))

	def test_002(self):
		'''用户名搜索功能正常'''
		self.driver.inputaction(self.driver.search_checkname_loc,"liuhongliang_33@163.com")
		self.driver.clickaction(self.driver.search_checkbutton_loc)
		time.sleep(0.25)
		self.assertEqual('liuhongliang_33@163.com',self.driver.get_about(self.driver.table_spcheckname_loc))

	def test_003(self):
		'''机构搜索正常'''
		self.driver.clearaction(self.driver.search_checkname_loc)
		self.driver.selecttext(self.driver.search_managekind_loc,'机构')
		self.driver.clickaction(self.driver.search_checkbutton_loc)
		time.sleep(0.25)
		self.assertEqual('机构',self.driver.get_about(self.driver.table_spcheckkind_loc))

	def test_004(self):
		'''个人搜索成功'''
		self.driver.selecttext(self.driver.search_managekind_loc,'个人')
		self.driver.clickaction(self.driver.search_checkbutton_loc)
		time.sleep(0.25)
		self.assertEqual('个人',self.driver.get_about(self.driver.table_spcheckkind_loc))

	def test_005(self):
		'''状态-待初审搜索成功'''
		self.driver.selecttext(self.driver.search_managekind_loc,'- 全部 -')
		self.driver.selecttext(self.driver.search_managestatus_loc,'待初审')
		self.driver.clickaction(self.driver.search_checkbutton_loc)
		time.sleep(0.25)
		self.assertEqual('待初审',self.driver.get_about(self.driver.table_spcheckstatus_loc))

	def test_006(self):
		'''状态-待复审搜索成功'''
		self.driver.selecttext(self.driver.search_managekind_loc,'- 全部 -')
		self.driver.selecttext(self.driver.search_managestatus_loc,'待复审')
		self.driver.clickaction(self.driver.search_checkbutton_loc)
		time.sleep(0.25)
		self.assertEqual('待复审',self.driver.get_about(self.driver.table_spcheckstatus_loc))

	def test_007(self):
		'''状态-未通过搜索成功'''
		self.driver.selecttext(self.driver.search_managestatus_loc,'未通过')
		self.driver.clickaction(self.driver.search_checkbutton_loc)
		time.sleep(0.25)
		self.assertEqual('未通过',self.driver.get_about(self.driver.table_spcheckstatus_loc))

	def test_008(self):
		'''状态-已通过搜索成功'''
		self.driver.selecttext(self.driver.search_managestatus_loc,'已通过')
		self.driver.clickaction(self.driver.search_checkbutton_loc)
		time.sleep(0.25)
		self.assertEqual('已通过',self.driver.get_about(self.driver.table_spcheckstatus_loc))

	def test_009(self):
		'''审核-拒绝-意见为空'''
		self.driver.selecttext(self.driver.search_managestatus_loc,'- 全部 -')
		self.driver.inputaction(self.driver.search_checkname_loc,"liuhongliang01@163.com")
		self.driver.clickaction(self.driver.search_checkbutton_loc)
		time.sleep(0.25)
		self.assertEqual('待初审',self.driver.get_about(self.driver.table_spcheckstatus_loc))
		self.assertEqual('liuhongliang01@163.com',self.driver.get_about(self.driver.table_spcheckname_loc))
		self.driver.clickaction(self.driver.table_spcheck_loc)
		time.sleep(0.5)
		self.driver.clickaction(self.driver.alert_checkno_loc)
		self.driver.clickaction(self.driver.alert_checkbutton_loc)
		time.sleep(0.5)
		self.assertIn('请输入审批意见',self.driver.get_about(self.driver.alert_checktips_loc))
		self.driver.clickaction(self.driver.alert_checkclose_loc)

	def test_010(self):
		'''重发链接成功'''
		self.driver.inputaction(self.driver.search_checkname_loc,"xitest111@163.com")
		self.driver.clickaction(self.driver.search_checkbutton_loc)
		time.sleep(0.25)
		self.assertEqual('未通过',self.driver.get_about(self.driver.table_spcheckstatus_loc))
		self.assertEqual('xitest111@163.com',self.driver.get_about(self.driver.table_spcheckname_loc))
		self.driver.clickaction(self.driver.table_spcheckagain_loc)
		time.sleep(1)
		self.assertIn('恭喜您！已成功发送新的注册链接',self.driver.get_about(self.driver.alert_checkagaintips_loc))
		self.driver.clickaction(self.driver.alert_checkagainbutton_loc)
		time.sleep(0.5)

	def test_011(self):
		'''查看成功'''
		self.driver.inputaction(self.driver.search_checkname_loc,'liuhongliang_33@163.com')
		self.driver.clickaction(self.driver.search_checkbutton_loc)
		time.sleep(0.5)
		self.assertEqual('已通过',self.driver.get_about(self.driver.table_spcheckstatus_loc))
		self.assertEqual('liuhongliang_33@163.com',self.driver.get_about(self.driver.table_spcheckname_loc))
		self.driver.clickaction(self.driver.table_manageview_loc)
		time.sleep(0.5)
		self.assertEqual(self.data.read_cell(1,1),self.driver.get_about(self.driver.view_managename_loc))
		self.assertEqual('已通过',self.driver.get_about(self.driver.view_managestatus_loc))
		self.assertEqual('2017-11-06',self.driver.get_about(self.driver.view_manamgedate_loc))
		self.assertEqual('阿尔巴尼亚',self.driver.get_about(self.driver.view_managearea_loc))
		self.assertEqual("机构",self.driver.get_about(self.driver.view_managekind_loc))
		self.assertEqual('测试数据-HLLiu',self.driver.get_about(self.driver.view_manageorgname_loc))
		self.assertEqual(self.data.read_cell(1,5),self.driver.get_about(self.driver.view_manageorgadd_loc))
		self.assertEqual('1251241211',self.driver.get_about(self.driver.view_manageorgid_loc))
		self.assertEqual('',self.driver.get_about(self.driver.view_managewitsite_loc))
		self.assertEqual('测试数据-HLLiu',self.driver.get_about(self.driver.view_managelinkname_loc))
		self.assertEqual('-',self.driver.get_about(self.driver.view_manageTel_loc))
		self.assertEqual('86-18513519528',self.driver.get_about(self.driver.view_managephone_loc))
		self.assertEqual('',self.driver.get_about(self.driver.view_manageps_loc))
		self.assertEqual('liuhongliang_35@163.com',self.driver.get_about(self.driver.view_managemail_loc))
		self.assertEqual('深圳',self.driver.get_about(self.driver.view_manageadd_loc))
		self.assertEqual('',self.driver.get_about(self.driver.view_managezip_loc))


if __name__ =="__mian__":
	unittest.main()















