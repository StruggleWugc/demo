import sys
# sys.path.append("..")
from page.RAMS_systempage import Rams_system
import unittest,time,os
from common.read_excel import Read
import  run_all

class Rams_sysmanage(unittest.TestCase):
	'''RA后台-系统管理-角色/系统账户'''
	@classmethod
	def setUpClass(cls):
		'''登入系统,进入系统管理table'''
		cls.driver = Rams_system()
		cls.driver.login_success()
		cls.driver.clickaction(cls.driver.systemclick_loc)
		cls.data = Read(run_all.fppath+r'\date\ISLI_RA_MS.xls')						#角色管理
		cls.data1 =Read(run_all.fppath+r'\date\ISLI_RA_MS.xls',1)					#系统账户
		cls.rolename ="角色名称"+str(int(time.time()))

	def test_001(self):
		'''进入角色管理'''
		self.driver.clickaction(self.driver.rolemanage_loc)
		self.assertEqual("创建角色",self.driver.get_about(self.driver.rolecreate_loc))
		self.driver.clickaction(self.driver.rolecreate_loc)
		self.assertEqual("创建角色",self.driver.get_about(self.driver.roletitle_loc))

	def test_002(self):
		'''创建角色所属区域为空'''
		self.driver.selectaction(self.driver.roleareaCn_loc,index=0)
		self.driver.inputaction(self.driver.rolenameCn_loc,self.rolename)
		self.assertIn("选择所属区域",self.driver.get_about(self.driver.error_roleareaCn_loc))
		self.driver.clickaction(self.driver.rolesubmit_loc)
		self.assertEqual("创建角色",self.driver.get_about(self.driver.roletitle_loc))

	def test_003(self):
		'''创建角色名称中文为空'''
		self.driver.selecttext(self.driver.roleareaCn_loc,'阿富汗')
		self.driver.clearaction(self.driver.rolenameCn_loc)
		self.driver.inputaction(self.driver.roleaboutCn_loc,"测试中文角色描述")
		self.assertIn('输入角色名称',self.driver.get_about(self.driver.error_rolenameCn_loc))
		self.driver.clickaction(self.driver.rolesubmit_loc)
		self.assertEqual("创建角色",self.driver.get_about(self.driver.roletitle_loc))

	def test_004(self):
		'''英文区域为空'''
		self.driver.inputaction(self.driver.rolenameCn_loc,self.rolename)
		self.driver.selectaction(self.driver.roleareaEn_loc,index =0)
		self.driver.inputaction(self.driver.rolenameEn_loc,self.rolename)
		self.assertTrue(self.driver.get_about(self.driver.error_roleareaEn_loc))
		self.driver.clickaction(self.driver.rolesubmit_loc)
		self.assertEqual("创建角色",self.driver.get_about(self.driver.roletitle_loc))

	def test_005(self):
		'''角色名称英文名为空'''
		self.driver.selecttext(self.driver.roleareaEn_loc,"Albania")
		self.driver.inputaction(self.driver.rolenameEn_loc,'   ')
		self.driver.inputaction(self.driver.roleaboutEn_loc,"测试英文描述输入")
		# self.driver.clickaction(self.driver.rolesubmit_loc)
		time.sleep(0.5)
		self.assertTrue(self.driver.get_about(self.driver.error_rolenameEn_loc))
		self.assertEqual("创建角色",self.driver.get_about(self.driver.roletitle_loc))


	def test_006(self):
		'''正常创建成功'''
		self.driver.inputaction(self.driver.rolenameEn_loc,self.rolename)
		time.sleep(0.25)
		self.driver.clickaction(self.driver.rolesubmit_loc)
		time.sleep(0.25)
		self.assertEqual("角色管理",self.driver.get_about(self.driver.table_roletitle_loc))
		self.assertEqual(self.rolename,self.driver.get_about(self.driver.table_rolename_loc))


	def test_007(self):
		'''角色名称中文已存在'''
		self.driver.clickaction(self.driver.rolecreate_loc)
		time.sleep(0.25)
		self.assertEqual("创建角色",self.driver.get_about(self.driver.roletitle_loc))
		self.driver.inputaction(self.driver.rolenameCn_loc,self.rolename)
		self.driver.inputaction(self.driver.roleaboutCn_loc,"测试中文名已存在")
		self.driver.clickaction(self.driver.rolesubmit_loc)
		time.sleep(0.5)
		self.assertIn('名称已存在',self.driver.get_about(self.driver.error_rolenameCnone_loc))


	def test_008(self):
		'''英文角色名已存在'''
		self.driver.inputaction(self.driver.rolenameEn_loc,self.rolename)
		self.driver.inputaction(self.driver.roleaboutEn_loc,"测试英文名已存在")
		self.driver.clickaction(self.driver.rolesubmit_loc)
		time.sleep(0.75)
		self.assertTrue(self.driver.get_about(self.driver.error_rolenameEnone_loc))
		time.sleep(0.5)
		self.driver.selecttext(self.driver.roleareaCn_loc,'阿富汗')
		self.driver.inputaction(self.driver.rolenameCn_loc,self.rolename+'二')
		self.driver.inputaction(self.driver.roleaboutCn_loc,"第二次创建角色")
		self.driver.inputaction(self.driver.rolenameEn_loc,self.rolename+'二')
		self.driver.inputaction(self.driver.roleaboutEn_loc,"第二次创建角色")
		self.driver.clickaction(self.driver.rolesubmit_loc)
		self.assertEqual("角色管理",self.driver.get_about(self.driver.table_roletitle_loc))
		self.assertEqual(self.rolename+'二',self.driver.get_about(self.driver.table_rolename_loc))

	def test_009(self):
		'''测试修改区域为空'''
		time.sleep(0.75)
		self.driver.clickaction(self.driver.table_roleedit_loc)
		time.sleep(0.5)
		self.driver.selecttext(self.driver.roleareaCn_loc,'-请选择 -')
		time.sleep(0.5)
		self.driver.inputaction(self.driver.roleaboutCn_loc,"修改")
		time.sleep(0.5)
		self.assertTrue(self.driver.get_about(self.driver.error_roleareaEn_loc))
		self.driver.clickaction(self.driver.rolesubmit_loc)
		self.assertEqual("创建角色",self.driver.get_about(self.driver.roletitle_loc))


	def test_010(self):
		'''修改-角色名称中文已存在'''
		self.driver.inputaction(self.driver.rolenameCn_loc,self.rolename)
		self.driver.inputaction(self.driver.roleaboutCn_loc,"修改2")
		self.driver.clickaction(self.driver.rolesubmit_loc)
		time.sleep(1)
		self.assertIn('名称已存在',self.driver.get_about(self.driver.error_rolenameCnone_loc))
		self.driver.clickaction(self.driver.rolesubmit_loc)
		self.assertEqual("创建角色",self.driver.get_about(self.driver.roletitle_loc))

	def test_011(self):
		'''修改角色名称中文名为空'''
		self.driver.clearaction(self.driver.rolenameCn_loc)
		self.driver.inputaction(self.driver.roleaboutCn_loc,"修改2")
		self.assertIn('输入角色名',self.driver.get_about(self.driver.error_rolenameCn_loc))
		self.driver.clickaction(self.driver.rolesubmit_loc)
		self.assertEqual("创建角色",self.driver.get_about(self.driver.roletitle_loc))


	def test_012(self):
		'''修改角色区域英文为空'''
		self.driver.selectaction(self.driver.roleareaEn_loc,index =0)
		self.driver.inputaction(self.driver.roleaboutEn_loc,self.rolename)
		self.assertTrue(self.driver.get_about(self.driver.error_roleareaEn_loc))
		self.driver.clickaction(self.driver.rolesubmit_loc)
		self.assertEqual("创建角色",self.driver.get_about(self.driver.roletitle_loc))

	def test_013(self):
		'''修改-英文角色名已存在'''
		self.driver.inputaction(self.driver.rolenameEn_loc,self.rolename)
		self.driver.inputaction(self.driver.roleaboutCn_loc,"修改2")
		time.sleep(0.5)
		self.driver.clickaction(self.driver.rolesubmit_loc)
		time.sleep(0.75)
		self.assertTrue(self.driver.get_about(self.driver.error_rolenameEnone_loc))
		self.assertEqual("创建角色",self.driver.get_about(self.driver.roletitle_loc))


	def test_014(self):
		'''修改英文角色名为空'''
		self.driver.clearaction(self.driver.rolenameEn_loc)
		self.driver.inputaction(self.driver.roleaboutCn_loc,"修改2")
		self.assertTrue(self.driver.get_about(self.driver.error_rolenameEn_loc))
		self.driver.clickaction(self.driver.rolesubmit_loc)
		self.assertEqual("创建角色",self.driver.get_about(self.driver.roletitle_loc))

	def test_015(self):
		'''正常修改成功'''
		self.driver.selecttext(self.driver.roleareaCn_loc,'阿富汗')
		self.driver.inputaction(self.driver.rolenameCn_loc,"测试数据")
		self.driver.inputaction(self.driver.rolenameEn_loc,"测试数据")
		time.sleep(0.75)
		self.driver.clickaction(self.driver.rolesubmit_loc)
		time.sleep(0.75)
		self.assertEqual("角色管理",self.driver.get_about(self.driver.table_roletitle_loc))
		# self.assertEqual("测试数据",self.driver.get_about(self.driver.table_rolename_loc))

	def test_016(self):
		'''删除新建角色'''
		self.driver.clickaction(self.driver.table_roledel_loc)
		time.sleep(0.5)
		self.assertIn('确定要删除该角色',self.driver.get_about(self.driver.stop_rolealerttips_loc))
		time.sleep(0.5)
		self.driver.clickaction(self.driver.stop_rolealertbutton_loc)
		time.sleep(0.5)
		self.assertEqual(self.rolename,self.driver.get_about(self.driver.table_rolename_loc))

	def test_017(self):
		'''停用角色'''
		time.sleep(0.5)
		self.driver.clickaction(self.driver.table_rolestop_loc)
		time.sleep(0.5)
		self.assertIn('是否确定停用当前角色',self.driver.get_about(self.driver.stop_rolealerttips_loc))
		time.sleep(0.5)
		self.driver.clickaction(self.driver.stop_rolealertbutton_loc)
		self.assertTrue(self.driver.find_element(self.driver.table_rolestart_loc))

	def test_018(self):
		'''启用角色后删除'''
		self.driver.clickaction(self.driver.table_rolestart_loc)
		time.sleep(0.5)
		self.assertIn('是否确定启用当前角色',self.driver.get_about(self.driver.stop_rolealerttips_loc))
		time.sleep(0.5)
		self.driver.clickaction(self.driver.stop_rolealertbutton_loc)
		self.assertTrue(self.driver.find_element(self.driver.table_rolestop_loc))
		self.assertEqual(self.rolename,self.driver.get_about(self.driver.table_rolename_loc))
		self.driver.clickaction(self.driver.table_roledel_loc)
		time.sleep(0.5)
		self.assertIn('确定要删除该角色',self.driver.get_about(self.driver.stop_rolealerttips_loc))
		time.sleep(0.75)
		self.driver.clickaction(self.driver.stop_rolealertbutton_loc)
		time.sleep(0.25)
		self.driver.refresh()
		time.sleep(0.25)
		self.assertNotEquals(self.rolename,self.driver.get_about(self.driver.table_rolename_loc))


	def test_019(self):
		'''进入系统账户创建帐户'''
		time.sleep(0.5)
		self.driver.clickaction(self.driver.sys_accounts_loc)
		time.sleep(0.5)
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_create_loc))
		time.sleep(0.5)
		self.driver.clickaction(self.driver.accounts_create_loc)
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_020(self):
		'''用户名为空'''
		self.driver.inputaction(self.driver.accounts_jobno_loc,self.data1.read_cell(1,2))
		self.driver.inputaction(self.driver.accounts_name_loc,self.data1.read_cell(1,3))
		self.driver.inputaction(self.driver.accounts_tel_2_loc,self.data1.read_cell(1,5))
		self.driver.inputaction(self.driver.accounts_tel_3_loc,self.data1.read_cell(1,6))
		self.driver.inputaction(self.driver.accounts_tel_4_loc,self.data1.read_cell(1,7))
		self.driver.inputaction(self.driver.accounts_phone_loc,self.data1.read_cell(1,9))
		self.driver.inputaction(self.driver.accounts_eamil_loc,self.data1.read_cell(1,10))
		self.driver.inputaction(self.driver.accounts_pw1_loc,self.data1.read_cell(1,11))
		self.driver.inputaction(self.driver.accounts_pw2_loc,self.data1.read_cell(1,12))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('户名不能为空',self.driver.get_about(self.driver.error_accountsusname_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_021(self):
		'''用户名小于3位'''
		self.driver.inputaction(self.driver.accounts_usname_loc,self.data1.read_cell(2,1))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('户名由3~50位字母',self.driver.get_about(self.driver.error_accountsusname_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_022(self):
		'''用户名非数字/字母/下划线'''
		self.driver.inputaction(self.driver.accounts_usname_loc,self.data1.read_cell(3,1))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('户名由3~50位字母',self.driver.get_about(self.driver.error_accountsusname_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_023(self):
		'''用户名已存在'''
		self.driver.inputaction(self.driver.accounts_usname_loc,self.data1.read_cell(4,1))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		time.sleep(0.25)
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_024(self):
		'''工号为空'''
		# self.driver.inputaction(self.driver.accounts_usname_loc,self.data1.read_cell(5,1))
		self.driver.clearaction(self.driver.accounts_jobno_loc)
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('用户名已经被使用',self.driver.get_about(self.driver.error_accountsusname_loc))
		self.assertIn('工号不可以为空',self.driver.get_about(self.driver.error_accountsjbno_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_025(self):
		'''工号小于6位'''
		self.driver.inputaction(self.driver.accounts_jobno_loc,self.data1.read_cell(6,2))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('由6位字母或数字组成',self.driver.get_about(self.driver.error_accountsjbno_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_026(self):
		'''工号非数字/字母'''
		self.driver.inputaction(self.driver.accounts_jobno_loc,self.data1.read_cell(7,2))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('由6位字母或数字组成',self.driver.get_about(self.driver.error_accountsjbno_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_027(self):
		'''工号已存在'''
		self.driver.inputaction(self.driver.accounts_jobno_loc,self.data1.read_cell(8,2))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('工号已经被使用',self.driver.get_about(self.driver.error_accountsjbno_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_028(self):
		'''姓名为空'''
		self.driver.inputaction(self.driver.accounts_jobno_loc,self.data1.read_cell(9,2))
		self.driver.clearaction(self.driver.accounts_name_loc)
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('姓名不能为空',self.driver.get_about(self.driver.error_accountsname_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_029(self):
		'''姓名为符号'''
		self.driver.inputaction(self.driver.accounts_name_loc,self.data1.read_cell(10,3))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('能包含特殊字符',self.driver.get_about(self.driver.error_accountsname_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_030(self):
		'''固话区号为空'''
		self.driver.inputaction(self.driver.accounts_name_loc,self.data1.read_cell(11,3))
		self.driver.inputaction(self.driver.accounts_tel_2_loc,' ')
		self.assertIn('区号不能为空',self.driver.get_about(self.driver.error_alterTel_loc))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_031(self):
		'''区号非数字'''
		self.driver.inputaction(self.driver.accounts_tel_2_loc,self.data1.read_cell(12,5))
		self.driver.inputaction(self.driver.accounts_tel_3_loc,'12345678')
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		time.sleep(0.25)
		self.assertIn('区号格式不正确',self.driver.get_about(self.driver.error_alterTel_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_032(self):
		'''固话号码为空'''
		self.driver.inputaction(self.driver.accounts_tel_2_loc,self.data1.read_cell(13,5))
		self.driver.inputaction(self.driver.accounts_tel_3_loc,' ')
		self.assertIn('固定号码不能为空',self.driver.get_about(self.driver.error_accountsTel_loc))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_033(self):
		'''固定号码非数字'''
		self.driver.inputaction(self.driver.accounts_tel_3_loc,self.data1.read_cell(14,6))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('号码格式不正确',self.driver.get_about(self.driver.error_accountsTel_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_034(self):
		'''固定号码小于6位'''
		self.driver.inputaction(self.driver.accounts_tel_3_loc,self.data1.read_cell(15,6))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('号码格式不正确',self.driver.get_about(self.driver.error_accountsTel_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_035(self):
		'''分机号非数字'''
		self.driver.inputaction(self.driver.accounts_tel_3_loc,self.data1.read_cell(16,6))
		self.driver.inputaction(self.driver.accounts_tel_4_loc,self.data1.read_cell(16,7))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		time.sleep(0.5)
		self.assertIn('机号格式不正确',self.driver.get_about(self.driver.error_accountsTel4_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_036(self):
		'''手机号为空'''
		self.driver.inputaction(self.driver.accounts_tel_4_loc,self.data1.read_cell(17,7))
		self.driver.clearaction(self.driver.accounts_phone_loc)
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('电话号码不能为空',self.driver.get_about(self.driver.error_accountsMobile_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_037(self):
		'''手机号码小于6位'''
		self.driver.inputaction(self.driver.accounts_phone_loc,self.data1.read_cell(18,9))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('电话号码格式不正确',self.driver.get_about(self.driver.error_accountsMobile_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_038(self):
		'''手机号码非数字'''
		self.driver.inputaction(self.driver.accounts_phone_loc,self.data1.read_cell(19,9))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('电话号码格式不正确',self.driver.get_about(self.driver.error_accountsMobile_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_039(self):
		'''邮箱为空'''
		self.driver.inputaction(self.driver.accounts_phone_loc,self.data1.read_cell(20,9))
		self.driver.clearaction(self.driver.accounts_eamil_loc)
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('电子邮箱不能为空',self.driver.get_about(self.driver.error_accountsemail_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_040(self):
		'''邮箱非数字字母符号'''
		self.driver.inputaction(self.driver.accounts_eamil_loc,self.data1.read_cell(21,10))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('电子邮箱格式不正确',self.driver.get_about(self.driver.error_accountsemail_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_041(self):
		'''非邮箱格式'''
		self.driver.inputaction(self.driver.accounts_eamil_loc,self.data1.read_cell(22,10))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('电子邮箱格式不正确',self.driver.get_about(self.driver.error_accountsemail_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_042(self):
		'''邮箱已使用'''
		self.driver.inputaction(self.driver.accounts_eamil_loc,self.data1.read_cell(23,10))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		time.sleep(0.25)
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_043(self):
		'''密码为空'''
		self.driver.clearaction(self.driver.accounts_pw1_loc)
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('电子邮箱已经被使用',self.driver.get_about(self.driver.error_accountsemail_loc))
		self.assertIn('密码不能为空',self.driver.get_about(self.driver.error_accountspw1_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_044(self):
		'''密码小于6位'''
		self.driver.inputaction(self.driver.accounts_eamil_loc,self.data1.read_cell(24,10))
		self.driver.inputaction(self.driver.accounts_pw1_loc,self.data1.read_cell(25,11))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('密码是英文字母、数字或符号组合',self.driver.get_about(self.driver.error_accountspw1_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_045(self):
		'''密码为纯数字'''
		self.driver.inputaction(self.driver.accounts_pw1_loc,self.data1.read_cell(26,11))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('密码是英文字母、数字或符号组合',self.driver.get_about(self.driver.error_accountspw1_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_046(self):
		'''密码为纯字母'''
		self.driver.inputaction(self.driver.accounts_pw1_loc,self.data1.read_cell(27,11))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('密码是英文字母、数字或符号组合',self.driver.get_about(self.driver.error_accountspw1_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_047(self):
		'''确认密码为空'''
		self.driver.inputaction(self.driver.accounts_pw1_loc,self.data1.read_cell(28,11))
		self.driver.clearaction(self.driver.accounts_pw2_loc)
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('确认密码不能为空',self.driver.get_about(self.driver.error_accountspw2_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_048(self):
		'''确认密码小于6位'''
		self.driver.inputaction(self.driver.accounts_pw2_loc,self.data1.read_cell(29,12))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('密码是英文字母、数字或符号组合',self.driver.get_about(self.driver.error_accountspw2_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))


	def test_049(self):
		'''确认密码为纯数字'''
		self.driver.inputaction(self.driver.accounts_pw2_loc,self.data1.read_cell(30,12))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('密码是英文字母、数字或符号组合',self.driver.get_about(self.driver.error_accountspw2_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_050(self):
		'''确认密码为纯字母'''
		self.driver.inputaction(self.driver.accounts_pw2_loc,self.data1.read_cell(31,12))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('密码是英文字母、数字或符号组合',self.driver.get_about(self.driver.error_accountspw2_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_051(self):
		'''确认密码与密码不一致'''
		self.driver.inputaction(self.driver.accounts_pw2_loc,self.data1.read_cell(32,12))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('密码与确认密码必须一致',self.driver.get_about(self.driver.error_accountspw2_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_052(self):
		'''固话国际区号\手机区号切换正常'''
		self.driver.selecttext(self.driver.accounts_tel_1_loc,self.data1.read_cell(33,4))
		self.driver.selecttext(self.driver.accounts_phonecode_loc,self.data1.read_cell(34,8))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('密码与确认密码必须一致',self.driver.get_about(self.driver.error_accountspw2_loc))
		self.assertEqual("创建帐户",self.driver.get_about(self.driver.accounts_title_loc))

	def test_053(self):
		'''正常注册'''
		self.driver.inputaction(self.driver.accounts_usname_loc,self.data1.read_cell(5,1))
		self.driver.inputaction(self.driver.accounts_pw2_loc,self.data1.read_cell(35,12))
		time.sleep(0.5)
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		# self.driver.refresh()
		time.sleep(1.5)
		self.assertEqual("系统账户",self.driver.get_about(self.driver.table_accountstitle_loc))
		time.sleep(0.5)
		self.assertIn(self.data1.read_cell(5,1),self.driver.get_about(self.driver.table_accountsusname_loc))
		self.assertIn(self.data1.read_cell(9,2),self.driver.get_about(self.driver.table_accountsjobno_loc))
		self.assertIn(self.data1.read_cell(11,3),self.driver.get_about(self.driver.table_accountsname_loc))
		self.assertIn(self.data1.read_cell(24,10),self.driver.get_about(self.driver.table_accountsemail_loc))
		self.assertIn("正常",self.driver.get_about(self.driver.table_accountsstatus_loc))

	def test_054(self):
		'''分配角色'''
		self.driver.clickaction(self.driver.table_accountsallot_loc)
		time.sleep(1)
		self.assertEqual("分配角色",self.driver.get_about(self.driver.accounts_rolealerttitleloc))
		time.sleep(0.5)
		self.driver.clickaction(self.driver.accounts_rolealertclick_loc)
		self.driver.clickaction(self.driver.accounts_rolealertsubmit_loc)
		time.sleep(0.5)
		self.assertIn("长期使用",self.driver.get_about(self.driver.table_accountsrole_loc))
		self.assertEqual("系统账户",self.driver.get_about(self.driver.table_accountstitle_loc))

	def test_055(self):
		'''验证注册账号工号能登入'''
		self.driver.clickaction(self.driver.exituser_button_loc)					#退出
		self.driver.loginaction(self.data1.read_cell(36,2),self.data1.read_cell(36,11))
		time.sleep(0.5)
		self.assertIn('或修改帐户密码',self.driver.get_about(self.driver.hometitle_loc))
		self.assertEqual(self.data1.read_cell(5,1),self.driver.get_about(self.driver.homeusname_loc))
		self.driver.clickaction(self.driver.exituser_button_loc)

	def test_056(self):
		'''验证账号用户名能登入'''
		self.driver.loginaction(self.data1.read_cell(5,1),self.data1.read_cell(36,11))
		time.sleep(0.5)
		self.assertIn('或修改帐户密码',self.driver.get_about(self.driver.hometitle_loc))
		self.assertEqual(self.data1.read_cell(5,1),self.driver.get_about(self.driver.homeusname_loc))
		self.driver.clickaction(self.driver.exituser_button_loc)

	def test_057(self):
		'''测试禁用账号'''
		self.driver.loginaction('isli','aaaaaa')
		self.driver.clickaction(self.driver.systemclick_loc)
		self.driver.clickaction(self.driver.sys_accounts_loc)
		self.driver.clickaction(self.driver.table_accountsstop_loc)
		time.sleep(0.5)
		self.assertIn('是否确定停用当前工作人员',self.driver.get_about(self.driver.accounts_stopalerttips_loc))
		time.sleep(0.5)
		self.driver.clickaction(self.driver.accounts_stopsubmit_loc)
		time.sleep(1)
		self.assertTrue(self.driver.table_accountsstart_loc)
		time.sleep(0.5)
		self.assertEqual('停用',self.driver.get_about(self.driver.table_accountsstatus_loc))

	def ttest_058(self):
		'''禁用账号无法登入'''
		self.driver.clickaction(self.driver.exituser_button_loc)
		self.driver.loginaction(self.data1.read_cell(5,1),self.data1.read_cell(36,11))
		self.assertIn('帐户已被禁用，请联系ISLI注',self.driver.get_error())
		time.sleep(0.5)
		self.driver.loginaction(self.data1.read_cell(5,1),self.data1.read_cell(36,11))
		self.assertIn('帐户已被禁用，请联系ISLI注',self.driver.get_error())

	def test_059(self):
		'''测试启用账号'''
		self.driver.clickaction(self.driver.table_accountsstart_loc)
		time.sleep(0.5)
		self.assertIn('是否确定启用当前',self.driver.get_about(self.driver.accounts_stopalerttips_loc))
		time.sleep(0.5)
		self.driver.clickaction(self.driver.accounts_stopsubmit_loc)
		time.sleep(1)
		self.assertTrue(self.driver.table_accountsstop_loc)
		self.assertEqual('正常',self.driver.get_about(self.driver.table_accountsstatus_loc))

	def test_060(self):
		'''进入修改'''
		self.driver.clickaction(self.driver.table_accountsedit_loc)
		self.assertEqual('修改',self.driver.get_about(self.driver.accounts_title_loc))

	def test_061(self):
		'''修改时工号为空'''
		time.sleep(0.5)
		self.driver.clearaction(self.driver.alter_accountsjobno_loc)
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		time.sleep(0.5)
		self.assertIn('工号不可以为空',self.driver.get_about(self.driver.error_accountsjbno_loc))
		self.assertEqual('修改',self.driver.get_about(self.driver.accounts_title_loc))

	def test_062(self):
		'''修改时工号小于6位'''
		self.driver.inputaction(self.driver.alter_accountsjobno_loc,self.data1.read_cell(38,2))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('号由6位字母或数字',self.driver.get_about(self.driver.error_accountsjbno_loc))
		self.assertEqual('修改',self.driver.get_about(self.driver.accounts_title_loc))

	def test_063(self):
		'''修改时工号非数字/字母'''
		self.driver.inputaction(self.driver.alter_accountsjobno_loc,self.data1.read_cell(39,2))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('号由6位字母或数字',self.driver.get_about(self.driver.error_accountsjbno_loc))
		self.assertEqual('修改',self.driver.get_about(self.driver.accounts_title_loc))

	def test_064(self):
		'''修改时工号已存在'''
		self.driver.inputaction(self.driver.alter_accountsjobno_loc,self.data1.read_cell(40,2))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('号已经被使用',self.driver.get_about(self.driver.error_accountsjbno_loc))
		self.assertEqual('修改',self.driver.get_about(self.driver.accounts_title_loc))

	def test_065(self):
		'''修改时姓名为空'''
		self.driver.inputaction(self.driver.alter_accountsjobno_loc,self.data1.read_cell(41,2))
		self.driver.clearaction(self.driver.alter_accountsname_loc)
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('姓名不能为空',self.driver.get_about(self.driver.error_accountsname_loc))

	def test_066(self):
		'''修改时姓名为符号'''
		self.driver.inputaction(self.driver.alter_accountsname_loc,self.data1.read_cell(42,3))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('名不能包含特殊字符',self.driver.get_about(self.driver.error_accountsname_loc))
		self.assertEqual('修改',self.driver.get_about(self.driver.accounts_title_loc))

	def test_067(self):
		'''修改时固话区号为空'''
		self.driver.inputaction(self.driver.alter_accountsname_loc,self.data1.read_cell(43,3))
		self.driver.inputaction(self.driver.accounts_tel_2_loc,' ')
		# self.driver.clearaction(self.driver.accounts_tel_2_loc)
		# self.driver.clickaction(self.driver.accounts_tel_3_loc)
		time.sleep(0.25)
		self.assertIn('区号不能为空',self.driver.get_about(self.driver.error_alterTel_loc))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertEqual('修改',self.driver.get_about(self.driver.accounts_title_loc))

	def test_068(self):
		'''修改时区号非数字'''
		self.driver.inputaction(self.driver.accounts_tel_2_loc,self.data1.read_cell(44,5))
		# self.driver.inputaction(self.driver.alter_accountsname_loc,self.data1.read_cell(43,3))
		self.assertIn('区号格式不正确',self.driver.get_about(self.driver.error_alterTel_loc))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertEqual('修改',self.driver.get_about(self.driver.accounts_title_loc))

	def test_069(self):
		'''修改时固话号码为空'''
		self.driver.inputaction(self.driver.accounts_tel_2_loc,self.data1.read_cell(45,5))
		self.driver.inputaction(self.driver.accounts_tel_3_loc,' ')
		# self.driver.clickaction(self.driver.accounts_tel_2_loc)
		# self.driver.inputaction(self.driver.alter_accountsname_loc,self.data1.read_cell(43,3))
		self.assertIn('固定号码不能为空',self.driver.get_about(self.driver.error_accountsTel_loc))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertEqual('修改',self.driver.get_about(self.driver.accounts_title_loc))

	def test_070(self):
		'''修改时固定号码非数字'''
		self.driver.inputaction(self.driver.accounts_tel_3_loc,self.data1.read_cell(46,6))
		# self.driver.inputaction(self.driver.alter_accountsname_loc,self.data1.read_cell(43,3))
		self.assertIn('号码格式不正确',self.driver.get_about(self.driver.error_accountsTel_loc))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertEqual('修改',self.driver.get_about(self.driver.accounts_title_loc))

	def test_071(self):
		'''修改时固定号码小于6位'''
		self.driver.inputaction(self.driver.accounts_tel_3_loc,self.data1.read_cell(47,6))
		# self.driver.inputaction(self.driver.alter_accountsname_loc,self.data1.read_cell(43,3))
		self.assertIn('号码格式不正确',self.driver.get_about(self.driver.error_accountsTel_loc))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertEqual('修改',self.driver.get_about(self.driver.accounts_title_loc))

	def test_072(self):
		'''修改时分机号非数字'''
		self.driver.inputaction(self.driver.accounts_tel_4_loc,self.data1.read_cell(48,7))
		self.assertIn('分机号格式不正确',self.driver.get_about(self.driver.error_accountsTel4_loc))
		self.driver.inputaction(self.driver.accounts_tel_3_loc,self.data1.read_cell(48,6))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertEqual('修改',self.driver.get_about(self.driver.accounts_title_loc))

	def test_073(self):
		'''修改时手机号为空'''
		self.driver.inputaction(self.driver.accounts_tel_4_loc,self.data1.read_cell(49,7))
		self.driver.clearaction(self.driver.accounts_phone_loc)
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('号码不能为空',self.driver.get_about(self.driver.error_accountsMobile_loc))
		self.assertEqual('修改',self.driver.get_about(self.driver.accounts_title_loc))

	def test_074(self):
		'''修改时手机号码不为11位'''
		self.driver.inputaction(self.driver.accounts_phone_loc,self.data1.read_cell(50,9))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('号码格式不正确',self.driver.get_about(self.driver.error_accountsMobile_loc))
		self.assertEqual('修改',self.driver.get_about(self.driver.accounts_title_loc))

	def test_075(self):
		'''修改时手机号码非数字'''
		self.driver.inputaction(self.driver.accounts_phone_loc,self.data1.read_cell(51,9))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('号码格式不正确',self.driver.get_about(self.driver.error_accountsMobile_loc))
		self.assertEqual('修改',self.driver.get_about(self.driver.accounts_title_loc))

	def test_076(self):
		'''修改时邮箱为空'''
		self.driver.inputaction(self.driver.accounts_phone_loc,self.data1.read_cell(52,9))
		self.driver.clearaction(self.driver.accounts_eamil_loc)
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('邮箱不能为空',self.driver.get_about(self.driver.error_accountsemail_loc))
		self.assertEqual('修改',self.driver.get_about(self.driver.accounts_title_loc))

	def test_077(self):
		'''修改时邮箱非数字字母符号'''
		self.driver.inputaction(self.driver.accounts_eamil_loc,self.data1.read_cell(53,10))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('请输入正确的邮箱',self.driver.get_about(self.driver.error_accountsemail_loc))
		self.assertEqual('修改',self.driver.get_about(self.driver.accounts_title_loc))

	def test_078(self):
		'''修改时非邮箱格式'''
		self.driver.inputaction(self.driver.accounts_eamil_loc,self.data1.read_cell(54,10))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('请输入正确的邮箱',self.driver.get_about(self.driver.error_accountsemail_loc))
		self.assertEqual('修改',self.driver.get_about(self.driver.accounts_title_loc))

	def test_079(self):
		'''修改时邮箱已使用'''
		self.driver.inputaction(self.driver.accounts_eamil_loc,self.data1.read_cell(55,10))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('邮箱已经被使用',self.driver.get_about(self.driver.error_accountsemail_loc))
		self.assertEqual('修改',self.driver.get_about(self.driver.accounts_title_loc))

	def test_080(self):
		'''修改时固话/手机区号切换正常'''
		self.driver.selecttext(self.driver.accounts_tel_1_loc,self.data1.read_cell(56,4))
		self.driver.selecttext(self.driver.accounts_phonecode_loc,self.data1.read_cell(57,8))
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		self.assertIn('邮箱已经被使用',self.driver.get_about(self.driver.error_accountsemail_loc))
		self.assertEqual('修改',self.driver.get_about(self.driver.accounts_title_loc))

	def test_081(self):
		'''正常修改成功'''
		self.driver.inputaction(self.driver.accounts_eamil_loc,self.data1.read_cell(58,10))
		time.sleep(0.5)
		self.driver.clickaction(self.driver.accounts_sumbit_loc)
		time.sleep(0.25)
		self.assertEqual("系统账户",self.driver.get_about(self.driver.table_accountstitle_loc))
		self.assertIn(self.data1.read_cell(5,1),self.driver.get_about(self.driver.table_accountsusname_loc))
		self.assertIn(self.data1.read_cell(58,2),self.driver.get_about(self.driver.table_accountsjobno_loc))
		self.assertIn(self.data1.read_cell(58,3),self.driver.get_about(self.driver.table_accountsname_loc))
		self.assertIn(self.data1.read_cell(58,10),self.driver.get_about(self.driver.table_accountsemail_loc))
		self.assertIn("正常",self.driver.get_about(self.driver.table_accountsstatus_loc))

	def test_082(self):
		'''账号修改前的jobno不能能登入'''
		self.driver.clickaction(self.driver.exituser_button_loc)
		time.sleep(0.5)
		self.driver.loginaction(self.data1.read_cell(59,2),self.data1.read_cell(59,11))
		self.assertIn('帐号不存在',self.driver.get_error())

	def test_083(self):
		'''账号修改后的jobno能登入'''
		self.driver.loginaction(self.data1.read_cell(60,2),self.data1.read_cell(60,11))
		time.sleep(0.5)
		self.assertIn('或修改帐户密码',self.driver.get_about(self.driver.hometitle_loc))
		self.assertEqual(self.data1.read_cell(5,1),self.driver.get_about(self.driver.homeusname_loc))
		time.sleep(0.5)
		self.driver.clickaction(self.driver.exituser_button_loc)

	def test_084(self):
		'''删除账号'''
		self.driver.loginaction('isli','aaaaaa')
		self.driver.clickaction(self.driver.systemclick_loc)
		self.driver.clickaction(self.driver.sys_accounts_loc)
		self.driver.click(self.driver.table_accountsdel_loc)
		time.sleep(0.5)
		self.assertIn('删除',self.driver.get_about(self.driver.accounts_deltips_loc))
		self.driver.clickaction(self.driver.accounts_delsubmit_loc)
		time.sleep(0.25)
		self.driver.refresh()
		self.assertNotIn(self.data1.read_cell(5,1),self.driver.get_about(self.driver.table_accountsusname_loc))

	def test_085(self):
		'''删除后的账号无法登入'''
		self.driver.clickaction(self.driver.exituser_button_loc)
		time.sleep(0.5)
		self.driver.loginaction(self.data1.read_cell(61,2),self.data1.read_cell(61,11))
		self.assertIn('帐号不存在',self.driver.get_error())





	@classmethod
	def tearDownClass(cls):
		cls.driver.close()

if __name__=="__main__":
	unittest.main()