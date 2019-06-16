import sys,random,string
# sys.path.append("..")
from page.RAMS_CreateTypePage import RamsCreateType
import unittest,time

class Rams_datasys(unittest.TestCase):
	'''RA后台管理-服务管理-关联/实体类型'''
	@classmethod
	def setUpClass(cls):
		'''登录系统'''
		cls.driver = RamsCreateType()
		cls.driver.login_success()
		cls.driver.clickaction(cls.driver.severmanage_clickloc)
		cls.entityname1 = "测试数据"+str(int(time.time()))						#实体类型名称1
		cls.entityname2 = "测试数据"+str(int(time.time())+1)					#实体类型名称2
		cls.assocname1 ="关联类型"+str(int(time.time()))						#关联类型名称1
		cls.assocname2 ="关联类型"+str(int(time.time())+1)						#关联类型名称2

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		# pass

	def test_001(self):
		'''进入新增实体'''
		self.driver.clickaction(self.driver.entityType_clickloc)
		self.assertEqual("新增实体类型",self.driver.get_about(self.driver.entity_createbuttonloc))
		self.driver.clickaction(self.driver.entity_createbuttonloc)
		self.assertEqual("新增",self.driver.get_about(self.driver.create_titleloc))

	def test_002(self):
		'''实体中文描述为空进行提交'''
		self.driver.inputaction(self.driver.create_entitynameCnloc,'测试输入')
		self.driver.click(self.driver.create_entityaboutCnloc)
		self.driver.inputaction(self.driver.create_entitynameEnloc,'测试输入')
		self.driver.inputaction(self.driver.create_entityaboutEnloc,'测试输入')
		# time.sleep(0.5)
		self.assertIn("请输入描述",self.driver.get_about(self.driver.create_entityaboutCnerrorloc))
		self.driver.clickaction(self.driver.create_submitbuttonloc)
		self.assertEqual("新增",self.driver.get_about(self.driver.create_titleloc))

	def test_003(self):
		'''英文名为空'''
		self.driver.inputaction(self.driver.create_entityaboutCnloc,'测试输入')
		self.driver.clearaction(self.driver.create_entitynameEnloc)
		self.driver.inputaction(self.driver.create_entityaboutEnloc,'测试输入')
		time.sleep(0.5)
		self.assertIn("请输入实体类型名称",self.driver.get_about(self.driver.create_entitynameEnerrorloc))
		self.driver.clickaction(self.driver.create_submitbuttonloc)
		self.assertEqual("新增",self.driver.get_about(self.driver.create_titleloc))

	def test_004(self):
		'''英文描述为空'''
		self.driver.inputaction(self.driver.create_entitynameEnloc,'测试输入')
		self.driver.clearaction(self.driver.create_entityaboutEnloc)
		self.driver.inputaction(self.driver.create_entityaboutCnloc,'测试输入')
		# time.sleep(0.5)
		self.assertIn("请输入描述",self.driver.get_about(self.driver.create_entityaboutEnerrorloc))
		self.driver.clickaction(self.driver.create_submitbuttonloc)
		self.assertEqual("新增",self.driver.get_about(self.driver.create_titleloc))

	def test_005(self):
		'''中文名为空'''
		# str =''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(2))
		self.driver.clearaction(self.driver.create_entitynameCnloc)
		self.driver.inputaction(self.driver.create_entityaboutEnloc,'测试输入')
		time.sleep(0.25)
		self.assertIn("请输入实体类型名称",self.driver.get_about(self.driver.create_entitynameCnerrorloc))
		self.driver.clickaction(self.driver.create_submitbuttonloc)
		self.assertEqual("新增",self.driver.get_about(self.driver.create_titleloc))

	def test_006(self):
		'''新增时候取消'''
		self.driver.inputaction(self.driver.create_entitynameCnloc,self.entityname1)
		self.driver.inputaction(self.driver.create_entityaboutCnloc,"测试中文描述")
		self.driver.inputaction(self.driver.create_entitynameEnloc,self.entityname1)
		self.driver.inputaction(self.driver.create_entityaboutEnloc,'测试英文描述')
		self.driver.clickaction(self.driver.create_abolishbuttonloc)
		self.assertEqual("新增实体类型",self.driver.get_about(self.driver.entity_createbuttonloc))

	def test_007(self):
		'''正常提交实体类型'''
		self.driver.clickaction(self.driver.entity_createbuttonloc)
		self.driver.inputaction(self.driver.create_entitynameCnloc,self.entityname1)
		self.driver.inputaction(self.driver.create_entityaboutCnloc,"测试中文描述")
		self.driver.inputaction(self.driver.create_entitynameEnloc,self.entityname1)
		self.driver.inputaction(self.driver.create_entityaboutEnloc,'测试英文描述')
		self.driver.clickaction(self.driver.create_submitbuttonloc)
		time.sleep(0.5)
		self.assertEqual(self.entityname1,self.driver.get_about(self.driver.table_entitynameloc))

	def test_008(self):
		'''连续多次提交实体类型申请'''
		time.sleep(0.5)
		self.driver.clickaction(self.driver.entity_createbuttonloc)
		time.sleep(0.5)
		self.driver.inputaction(self.driver.create_entitynameCnloc,self.entityname2)
		self.driver.inputaction(self.driver.create_entityaboutCnloc,"测试中文描述")
		self.driver.inputaction(self.driver.create_entitynameEnloc,self.entityname2)
		self.driver.inputaction(self.driver.create_entityaboutEnloc,'测试英文描述')
		self.driver.clickaction(self.driver.create_savebuttonloc)
		self.assertEqual(self.entityname2,self.driver.get_about(self.driver.create_entitysubmittipsloc))
		time.sleep(1)
		self.driver.click(self.driver.create_entitysubmiloc)
		self.assertEqual("新增",self.driver.get_about(self.driver.create_titleloc))


	def test_009(self):
		'''新增实体中文名重复'''
		self.driver.inputaction(self.driver.create_entitynameCnloc,self.entityname2)
		self.driver.inputaction(self.driver.create_entityaboutCnloc,"测试中文描述")
		time.sleep(0.5)
		self.assertIn("名称已存在",self.driver.get_about(self.driver.entity_renameCnerrorloc))


	def test_010(self):
		'''新增实体英文名重复'''
		self.driver.inputaction(self.driver.create_entitynameEnloc,self.entityname2)
		self.driver.inputaction(self.driver.create_entityaboutEnloc,'测试英文描述')
		time.sleep(0.5)
		self.assertTrue(self.driver.get_about(self.driver.entity_renameEnerrorloc))
		self.driver.clickaction(self.driver.create_abolishbuttonloc)

	def test_011(self):
		'''查看'''
		self.driver.click(self.driver.table_entityviewloc)
		self.assertEqual("查看",self.driver.get_about(self.driver.create_titleloc))

	def test_012(self):
		'''修改的中文实体名为空'''
		self.driver.click(('css selector','[value="修改"]'))
		self.driver.clearaction(self.driver.create_entitynameCnloc)
		self.driver.inputaction(self.driver.create_entityaboutEnloc,'测试输入')
		# time.sleep(0.5)
		self.assertIn("请输入实体类型名称",self.driver.get_about(self.driver.create_entitynameCnerrorloc))
		self.driver.clickaction(self.driver.create_submitbuttonloc)
		self.assertEqual("修改",self.driver.get_about(self.driver.create_titleloc))

	def test_013(self):
		'''修改中文描述为空'''
		self.driver.clearaction(self.driver.create_entityaboutCnloc)
		self.driver.inputaction(self.driver.create_entitynameCnloc,'测试输入')
		self.assertIn("请输入描述",self.driver.get_about(self.driver.create_entityaboutCnerrorloc))
		self.driver.clickaction(self.driver.create_submitbuttonloc)
		self.assertEqual("修改",self.driver.get_about(self.driver.create_titleloc))

	def test_014(self):
		'''修改英文名为空'''
		self.driver.clearaction(self.driver.create_entitynameEnloc)
		self.driver.inputaction(self.driver.create_entityaboutCnloc,'测试输入')
		time.sleep(0.25)
		self.assertIn("请输入实体类型名称",self.driver.get_about(self.driver.create_entitynameEnerrorloc))
		self.driver.clickaction(self.driver.create_submitbuttonloc)
		self.assertEqual("修改",self.driver.get_about(self.driver.create_titleloc))

	def test_015(self):
		'''修改英文描述为空'''
		self.driver.clearaction(self.driver.create_entityaboutEnloc)
		self.driver.inputaction(self.driver.create_entitynameCnloc,'测试输入')
		time.sleep(0.25)
		self.assertIn("请输入描述",self.driver.get_about(self.driver.create_entityaboutEnerrorloc))
		self.driver.clickaction(self.driver.create_submitbuttonloc)
		self.assertEqual("修改",self.driver.get_about(self.driver.create_titleloc))

	def test_016(self):
		'''修改已存在的中文名失败'''
		self.driver.inputaction(self.driver.create_entityaboutEnloc,"英文描述")
		self.driver.inputaction(self.driver.create_entitynameCnloc,self.entityname1)
		self.driver.inputaction(self.driver.create_entityaboutCnloc,"测试中文描述")
		time.sleep(0.5)
		self.assertIn("名称已存在",self.driver.get_about(self.driver.entity_renameCnerrorloc))
		self.driver.clickaction(self.driver.create_submitbuttonloc)
		self.assertEqual("修改",self.driver.get_about(self.driver.create_titleloc))

	def test_017(self):
		'''修改已存在的英文名失败'''
		self.driver.inputaction(self.driver.create_entitynameCnloc,self.entityname1+'修改')
		self.driver.inputaction(self.driver.create_entitynameEnloc,self.entityname1)
		self.driver.inputaction(self.driver.create_entityaboutCnloc,"测试描述")
		time.sleep(0.5)
		self.assertTrue(self.driver.get_about(self.driver.entity_renameEnerrorloc))
		# self.assertTrue(self.driver.get_about(self.driver.create_entitynameEnerrorloc))
		self.driver.clickaction(self.driver.create_submitbuttonloc)
		self.assertEqual("修改",self.driver.get_about(self.driver.create_titleloc))

	def test_018(self):
		'''正常修改成功'''
		time.sleep(0.5)
		self.driver.inputaction(self.driver.create_entitynameEnloc,self.entityname1+'修改')
		self.driver.clickaction(self.driver.create_submitbuttonloc)
		time.sleep(0.5)
		self.assertEqual(self.entityname1+'修改',self.driver.get_about(self.driver.table_entitynameloc))

	def test_019(self):
		'''列表入口修改成功'''
		self.driver.clickaction(self.driver.table_entityeditloc)
		time.sleep(0.25)
		self.assertEqual("修改",self.driver.get_about(self.driver.create_titleloc))
		self.driver.inputaction(self.driver.create_entitynameCnloc,self.entityname2)
		self.driver.inputaction(self.driver.create_entitynameEnloc,self.entityname2)
		self.driver.clickaction(self.driver.create_submitbuttonloc)
		time.sleep(0.5)
		self.assertEqual(self.entityname2,self.driver.get_about(self.driver.table_entitynameloc))

	def test_020(self):
		'''实体类型搜索搜索		测试数据1515741699'''
		# self.driver.clickaction(self.driver.entityType_clickloc)
		self.driver.inputaction(self.driver.search_entityloc,self.entityname2)
		self.driver.clickaction(self.driver.search_buttonloc)
		self.assertTrue(self.driver.get_about(self.driver.table_entitynameloc))

	def test_021(self):
		'''停用加搜索'''
		self.driver.clearelement(self.driver.search_entityloc)
		self.driver.clickaction(self.driver.search_buttonloc)
		self.driver.clickaction(self.driver.table_entitystoploc)
		time.sleep(0.5)
		self.assertIn(self.entityname2,self.driver.get_about(self.driver.entity_stoptipsloc))
		time.sleep(0.5)
		self.driver.clickaction(self.driver.entity_stopsubmitloc)
		self.driver.selectaction(self.driver.search_statusloc,index =2)
		self.driver.clickaction(self.driver.search_buttonloc)
		self.assertEqual(self.entityname2,self.driver.get_about(self.driver.table_entitynameloc))
		self.assertTrue(self.driver.is_exists(self.driver.table_entitystartloc))

	def test_022(self):
		'''启用 加搜索'''
		self.driver.clickaction(self.driver.table_entitystartloc)
		time.sleep(0.5)
		self.assertIn(self.entityname2,self.driver.get_about(self.driver.entity_stoptipsloc))
		self.driver.clickaction(self.driver.entity_stopsubmitloc)
		self.driver.selectaction(self.driver.search_statusloc,index =1)
		self.driver.clickaction(self.driver.search_buttonloc)
		self.assertEqual(self.entityname2,self.driver.get_about(self.driver.table_entitynameloc))
		self.assertTrue(self.driver.is_exists(self.driver.table_entitystoploc))

	def test_023(self):
		'''进入新增关联类型页面'''
		self.driver.clickaction(self.driver.associationType_clickloc)
		self.assertEqual("新增关联类型",self.driver.get_about(self.driver.associationType_createbuttonloc))
		self.driver.clickaction(self.driver.associationType_createbuttonloc)
		self.assertEqual("新增",self.driver.get_about(self.driver.create_titleloc))

	def test_024(self):
		'''操作中文源类型为空'''
		time.sleep(0.5)
		self.driver.selecttext(self.driver.create_sourcenameCnloc,self.entityname1)
		self.driver.selecttext(self.driver.create_targetnameCnloc,self.entityname1)
		self.driver.inputaction(self.driver.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.driver.inputaction(self.driver.create_associationnameEnloc,self.assocname1)
		self.driver.inputaction(self.driver.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.driver.inputaction(self.driver.create_associationnameCnloc,self.assocname1)
		self.driver.selectaction(self.driver.create_sourcenameCnloc,index=0)
		time.sleep(0.5)
		self.driver.inputaction(self.driver.create_associationaboutCnloc,"测试新增关联类型中文描述")
		# self.assertIn("请选择源类型",self.driver.get_about(self.driver.error_sourcenameCnloc))
		self.assertIn("请选择源类型",self.driver.get_about(self.driver.error_sourcenameEnloc))
		self.driver.clickaction(self.driver.association_createsubmitloc)
		self.assertEqual("新增",self.driver.get_about(self.driver.create_titleloc))

	def test_025(self):
		'''操作中文关联类型为空'''
		self.driver.clearaction(self.driver.create_associationnameCnloc)
		self.driver.selecttext(self.driver.create_sourcenameCnloc,self.entityname1)
		self.driver.inputaction(self.driver.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.assertIn("请输入关联类型名称",self.driver.get_about(self.driver.error_associationnameCnloc))
		self.driver.selecttext(self.driver.create_targetnameCnloc,self.entityname1)
		self.driver.inputaction(self.driver.create_associationnameEnloc,self.assocname1)
		self.driver.inputaction(self.driver.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.driver.clickaction(self.driver.association_createsubmitloc)
		self.assertEqual("新增",self.driver.get_about(self.driver.create_titleloc))

	def test_026(self):
		'''操作中文目标类型为空'''
		self.driver.selectaction(self.driver.create_sourcenameCnloc,index=1)
		time.sleep(0.5)
		self.driver.selectaction(self.driver.create_targetnameCnloc,index=0)
		time.sleep(0.5)
		self.driver.inputaction(self.driver.create_associationaboutCnloc,"测试新增关联类型中文描述")
		time.sleep(0.25)
		self.assertIn("请选择目标类型",self.driver.get_about(self.driver.error_targetnameCnloc))
		self.assertIn("请选择目标类型",self.driver.get_about(self.driver.error_targetnameEnloc))
		self.driver.clickaction(self.driver.association_createsubmitloc)
		self.assertEqual("新增",self.driver.get_about(self.driver.create_titleloc))

	def test_027(self):
		'''中文描述为空'''
		self.driver.selectaction(self.driver.create_targetnameCnloc,index=1)
		self.driver.clearaction(self.driver.create_associationaboutCnloc)
		self.driver.inputaction(self.driver.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.assertIn('请输入描述',self.driver.get_about(self.driver.error_associationaboutCnloc))
		self.driver.clickaction(self.driver.association_createsubmitloc)
		self.assertEqual("新增",self.driver.get_about(self.driver.create_titleloc))

	def test_028(self):
		'''英文关联名为空'''
		self.driver.inputaction(self.driver.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.driver.clearaction(self.driver.create_associationnameEnloc)
		self.driver.inputaction(self.driver.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.assertIn("请输入关联类型名称",self.driver.get_about(self.driver.error_associationnameEnloc))
		self.driver.clickaction(self.driver.association_createsubmitloc)
		self.assertEqual("新增",self.driver.get_about(self.driver.create_titleloc))

	def test_029(self):
		'''操作英文源为空'''
		self.driver.inputaction(self.driver.create_associationnameEnloc,self.assocname1)
		self.driver.selectaction(self.driver.create_sourcenameEnloc,index=0)
		self.driver.inputaction(self.driver.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.assertIn("请选择源类型",self.driver.get_about(self.driver.error_sourcenameCnloc))
		self.assertIn("请选择源类型",self.driver.get_about(self.driver.error_sourcenameEnloc))
		self.driver.clickaction(self.driver.association_createsubmitloc)
		self.assertEqual("新增",self.driver.get_about(self.driver.create_titleloc))

	def test_030(self):
		'''操作英文目标类型为空'''
		self.driver.selectaction(self.driver.create_sourcenameEnloc,index=1)
		self.driver.selectaction(self.driver.create_targetnameEnloc,index=0)
		self.driver.inputaction(self.driver.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.assertIn("请选择目标类型",self.driver.get_about(self.driver.error_targetnameCnloc))
		self.assertIn("请选择目标类型",self.driver.get_about(self.driver.error_targetnameEnloc))
		self.driver.clickaction(self.driver.association_createsubmitloc)
		self.assertEqual("新增",self.driver.get_about(self.driver.create_titleloc))

	def test_031(self):
		'''英文描述为空'''
		self.driver.selectaction(self.driver.create_targetnameEnloc,index=1)
		self.driver.clearaction(self.driver.create_associationaboutEnloc)
		self.driver.inputaction(self.driver.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.assertIn('请输入描述',self.driver.get_about(self.driver.error_associationaboutEnloc))
		self.driver.clickaction(self.driver.association_createsubmitloc)
		self.assertEqual("新增",self.driver.get_about(self.driver.create_titleloc))

	def test_032(self):
		'''新增时取消并重新进入'''
		self.driver.clickaction(self.driver.association_abolishloc)
		self.assertEqual("新增关联类型",self.driver.get_about(self.driver.associationType_createbuttonloc))
		self.driver.clickaction(self.driver.associationType_createbuttonloc)
		self.assertEqual("新增",self.driver.get_about(self.driver.create_titleloc))

	def test_033(self):
		'''正常提交注册'''
		self.driver.inputaction(self.driver.create_associationnameCnloc,self.assocname1)
		self.driver.selecttext(self.driver.create_sourcenameCnloc,self.entityname1)
		self.driver.inputaction(self.driver.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.driver.selecttext(self.driver.create_targetnameCnloc,self.entityname1)
		self.driver.inputaction(self.driver.create_associationnameEnloc,self.assocname1)
		self.driver.inputaction(self.driver.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.driver.clickaction(self.driver.association_createsubmitloc)
		self.assertEqual(self.assocname1,self.driver.get_about(self.driver.table_associationnameloc))
		self.assertEqual(self.entityname1,self.driver.get_about(self.driver.table_sourceloc))
		self.assertEqual(self.entityname1,self.driver.get_about(self.driver.table_targetloc))

	def test_034(self):
		'''连续提交多次申请'''
		self.driver.clickaction(self.driver.associationType_createbuttonloc)
		self.assertEqual("新增",self.driver.get_about(self.driver.create_titleloc))
		self.driver.inputaction(self.driver.create_associationnameCnloc,self.assocname2)
		self.driver.selecttext(self.driver.create_sourcenameCnloc,self.entityname2)
		self.driver.inputaction(self.driver.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.driver.selecttext(self.driver.create_targetnameCnloc,self.entityname2)
		self.driver.inputaction(self.driver.create_associationnameEnloc,self.assocname2)
		self.driver.inputaction(self.driver.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.driver.clickaction(self.driver.association_savebuttonloc)
		time.sleep(0.5)
		self.assertIn(self.assocname2,self.driver.get_about(self.driver.association_savetipsloc))
		time.sleep(0.5)
		self.driver.clickaction(self.driver.association_framesubmitloc)
		self.assertEqual("新增",self.driver.get_about(self.driver.create_titleloc))

	def test_035(self):
		'''新增关联类型名称中文名重复'''
		self.driver.inputaction(self.driver.create_associationnameCnloc,self.assocname2)
		self.driver.selecttext(self.driver.create_sourcenameCnloc,self.entityname1)
		self.driver.inputaction(self.driver.create_associationaboutCnloc,"测试新增关联类型中文描述")
		time.sleep(0.25)
		self.assertIn('名称已存在',self.driver.get_about(self.driver.error_associationnameOneCnloc))
		self.driver.selecttext(self.driver.create_targetnameCnloc,self.entityname1)
		self.driver.inputaction(self.driver.create_associationnameEnloc,str(int(time.time())))
		self.driver.inputaction(self.driver.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.driver.clickaction(self.driver.association_createsubmitloc)
		self.assertEqual("新增",self.driver.get_about(self.driver.create_titleloc))

	def test_036(self):
		'''新增关联类型名称英文名重复'''
		self.driver.inputaction(self.driver.create_associationnameCnloc,str(int(time.time())))
		self.driver.selecttext(self.driver.create_sourcenameCnloc,self.entityname1)
		self.driver.inputaction(self.driver.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.driver.selecttext(self.driver.create_targetnameCnloc,self.entityname1)
		self.driver.inputaction(self.driver.create_associationnameEnloc,self.assocname2)
		self.driver.inputaction(self.driver.create_associationaboutEnloc,"测试新增关联类型英文描述")
		time.sleep(0.5)
		self.assertTrue(self.driver.get_about(self.driver.error_associationnameOneEnloc))
		self.driver.clickaction(self.driver.association_createsubmitloc)
		self.assertEqual("新增",self.driver.get_about(self.driver.create_titleloc))
		self.driver.clickaction(self.driver.create_abolishbuttonloc)
		self.assertEqual("新增关联类型",self.driver.get_about(self.driver.associationType_createbuttonloc))

	def test_037(self):
		'''查看关联类型'''
		self.driver.clickaction(self.driver.table_assocviewloc)
		self.assertIn("查看",self.driver.get_about(self.driver.create_titleloc))

	def test_038(self):
		'''修改-关联名中文为空'''
		self.driver.click(('css selector','[value="修改"]'))
		self.driver.clearaction(self.driver.association_renameCnloc)
		self.driver.inputaction(self.driver.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.assertIn("输入关联类型名称",self.driver.get_about(self.driver.error_associationnameCnloc))
		self.driver.clickaction(self.driver.association_createsubmitloc)
		self.assertEqual("修改",self.driver.get_about(self.driver.create_titleloc))

	def test_039(self):
		'''修改-中文关联名重复'''
		time.sleep(0.5)
		self.driver.inputaction(self.driver.association_renameCnloc,self.assocname1)
		self.driver.inputaction(self.driver.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.assertIn("名称已存在",self.driver.get_about(self.driver.error_associationnameOneCnloc))
		self.driver.clickaction(self.driver.association_createsubmitloc)
		self.assertEqual("修改",self.driver.get_about(self.driver.create_titleloc))

	def test_040(self):
		'''修改-中文描述为空'''
		self.driver.inputaction(self.driver.association_renameCnloc,self.assocname2+"修改")
		self.driver.clearaction(self.driver.create_associationaboutCnloc)
		self.driver.inputaction(self.driver.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.assertIn('请输入描述',self.driver.get_about(self.driver.error_associationaboutCnloc))
		self.driver.clickaction(self.driver.association_createsubmitloc)
		self.assertEqual("修改",self.driver.get_about(self.driver.create_titleloc))

	def test_041(self):
		'''修改-英文名为空'''
		self.driver.inputaction(self.driver.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.driver.clearaction(self.driver.association_renameEnloc)
		self.driver.inputaction(self.driver.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.assertIn("请输入关联类型名称",self.driver.get_about(self.driver.error_associationnameEnloc))
		self.driver.clickaction(self.driver.association_createsubmitloc)
		self.assertEqual("修改",self.driver.get_about(self.driver.create_titleloc))

	def test_042(self):
		'''修改-英文名重复'''
		self.driver.inputaction(self.driver.association_renameEnloc,self.assocname1)
		self.driver.inputaction(self.driver.create_associationaboutEnloc,"测试新增关联类型英文描述")
		time.sleep(0.5)
		self.assertTrue(self.driver.get_about(self.driver.error_associationnameOneEnloc))
		self.driver.clickaction(self.driver.association_createsubmitloc)
		self.assertEqual("修改",self.driver.get_about(self.driver.create_titleloc))

	def test_043(self):
		'''修改-英文描述为空'''
		self.driver.inputaction(self.driver.association_renameEnloc,self.assocname2+'修改')
		self.driver.clearaction(self.driver.create_associationaboutEnloc)
		self.driver.inputaction(self.driver.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.assertIn('请输入描述',self.driver.get_about(self.driver.error_associationaboutEnloc))
		self.driver.clickaction(self.driver.association_createsubmitloc)
		self.assertEqual("修改",self.driver.get_about(self.driver.create_titleloc))

	def test_044(self):
		'''正常修改成功'''
		self.driver.inputaction(self.driver.association_renameCnloc,self.assocname2+'修改')
		self.driver.selecttext(self.driver.create_sourcenameCnloc,self.entityname2)
		self.driver.inputaction(self.driver.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.driver.selecttext(self.driver.create_targetnameCnloc,self.entityname2)
		self.driver.inputaction(self.driver.association_renameEnloc,self.assocname2+'修改')
		self.driver.inputaction(self.driver.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.driver.clickaction(self.driver.association_createsubmitloc)
		self.assertEqual(self.assocname2+'修改',self.driver.get_about(self.driver.table_associationnameloc))
		self.assertEqual(self.entityname2,self.driver.get_about(self.driver.table_sourceloc))
		self.assertEqual(self.entityname2,self.driver.get_about(self.driver.table_targetloc))

	def test_045(self):
		'''列表修改成功'''
		self.driver.clickaction(self.driver.table_assoceditloc)
		self.assertEqual("修改",self.driver.get_about(self.driver.create_titleloc))
		self.driver.inputaction(self.driver.association_renameCnloc,self.assocname2)
		self.driver.selecttext(self.driver.create_sourcenameCnloc,self.entityname2)
		self.driver.inputaction(self.driver.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.driver.selecttext(self.driver.create_targetnameCnloc,self.entityname2)
		self.driver.inputaction(self.driver.association_renameEnloc,self.assocname2)
		self.driver.inputaction(self.driver.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.driver.clickaction(self.driver.association_createsubmitloc)
		time.sleep(1.5)
		self.assertEqual(self.assocname2,self.driver.get_about(self.driver.table_associationnameloc))
		self.assertEqual(self.entityname2,self.driver.get_about(self.driver.table_sourceloc))
		self.assertEqual(self.entityname2,self.driver.get_about(self.driver.table_targetloc))

	def test_046(self):
		'''停用+状态停用搜索'''
		time.sleep(0.5)
		self.driver.clickaction(self.driver.table_assocstoploc)
		self.assertIn(self.assocname2,self.driver.get_about(self.driver.association_savetipsloc))
		time.sleep(0.5)
		self.driver.clickaction(self.driver.association_submitloc)
		time.sleep(0.5)
		self.driver.selectaction(self.driver.search_statusloc,index=2)
		self.driver.clickaction(self.driver.search_buttonloc)
		self.assertEqual(self.assocname2,self.driver.get_about(self.driver.table_associationnameloc))
		self.assertTrue(self.driver.is_exists(self.driver.table_assocstartloc))

	def test_047(self):
		'''关联类型搜索'''
		self.driver.selectaction(self.driver.search_statusloc,index=0)
		self.driver.inputaction(self.driver.search_associationloc,self.assocname1)
		self.driver.clickaction(self.driver.search_buttonloc)
		self.assertEqual(self.assocname1,self.driver.get_about(self.driver.table_associationnameloc))
		self.assertTrue(self.driver.is_exists(self.driver.table_assocstoploc))

	def test_048(self):
		'''源类型搜索'''
		self.driver.clearaction(self.driver.search_associationloc)
		self.driver.inputaction(self.driver.search_sourceloc,self.entityname2)
		self.driver.clickaction(self.driver.search_buttonloc)
		time.sleep(1.5)
		self.assertEqual(self.entityname2,self.driver.get_about(self.driver.table_sourceloc))
		self.assertTrue(self.driver.is_exists(self.driver.table_assocstartloc))

	def test_049(self):
		'''目标类型搜索'''
		self.driver.clearaction(self.driver.search_sourceloc)
		self.driver.inputaction(self.driver.search_targetloc,self.entityname1)
		self.driver.clickaction(self.driver.search_buttonloc)
		self.assertEqual(self.entityname1,self.driver.get_about(self.driver.table_targetloc))
		self.assertTrue(self.driver.is_exists(self.driver.table_assocstoploc))

	def test_050(self):
		'''正常启用'''
		time.sleep(1)
		self.driver.clearaction(self.driver.search_targetloc)
		self.driver.clickaction(self.driver.search_buttonloc)
		self.driver.clickaction(self.driver.table_assocstartloc)
		self.assertIn(self.assocname2,self.driver.get_about(self.driver.association_savetipsloc))
		time.sleep(0.5)
		self.driver.clickaction(self.driver.association_submitloc)
		time.sleep(0.5)
		self.assertEqual(self.assocname2,self.driver.get_about(self.driver.table_associationnameloc))
		self.assertTrue(self.driver.is_exists(self.driver.table_assocstoploc))

	def test_051(self):
		'''停用新增关联'''
		self.driver.inputaction(self.driver.search_associationloc,self.assocname1)
		self.driver.clickaction(self.driver.search_buttonloc)
		self.driver.clickaction(self.driver.table_assocstoploc)
		self.assertIn(self.assocname1,self.driver.get_about(self.driver.association_savetipsloc))
		time.sleep(0.5)
		self.driver.clickaction(self.driver.association_submitloc)
		time.sleep(1)
		self.assertEqual(self.assocname1,self.driver.get_about(self.driver.table_associationnameloc))
		self.assertTrue(self.driver.is_exists(self.driver.table_assocstartloc))

		# self.driver.inputaction(self.driver.search_associationloc,self.assocname2)
		# self.driver.clickaction(self.driver.search_buttonloc)
		# self.driver.clickaction(self.driver.table_assocstoploc)
		# self.assertIn(self.assocname2,self.driver.get_about(self.driver.association_savetipsloc))
		# time.sleep(0.5)
		# self.driver.clickaction(self.driver.association_submitloc)
		# time.sleep(1)
		# self.assertEqual(self.assocname2,self.driver.get_about(self.driver.table_associationnameloc))
		# self.assertTrue(self.driver.is_exists(self.driver.table_assocstartloc))


	def test_052(self):
		'''停用新增实体'''
		self.driver.clickaction(self.driver.entityType_clickloc)
		time.sleep(0.75)
		self.driver.inputaction(self.driver.search_entityloc,self.entityname2)
		self.driver.clickaction(self.driver.search_buttonloc)
		self.driver.clickaction(self.driver.table_entitystoploc)
		time.sleep(0.5)
		self.assertIn(self.entityname2,self.driver.get_about(self.driver.entity_stoptipsloc))
		time.sleep(0.5)
		self.driver.clickaction(self.driver.entity_stopsubmitloc)
		self.assertEqual(self.entityname2,self.driver.get_about(self.driver.table_entitynameloc))
		self.assertTrue(self.driver.is_exists(self.driver.table_entitystartloc))

		self.driver.inputaction(self.driver.search_entityloc,self.entityname1)
		self.driver.clickaction(self.driver.search_buttonloc)
		self.driver.clickaction(self.driver.table_entitystoploc)
		time.sleep(0.5)
		self.assertIn(self.entityname1,self.driver.get_about(self.driver.entity_stoptipsloc))
		time.sleep(0.5)
		self.driver.clickaction(self.driver.entity_stopsubmitloc)
		self.assertEqual(self.entityname1,self.driver.get_about(self.driver.table_entitynameloc))
		self.assertTrue(self.driver.is_exists(self.driver.table_entitystartloc))




if __name__=="__main__":
	unittest.main()