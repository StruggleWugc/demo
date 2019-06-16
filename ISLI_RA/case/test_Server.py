from page.RA_Servermakepage import Server
from common.mysql_pulic import MysqlUtil						#数据库
import run_all
import unittest,time,os,random


class ServerMake(unittest.TestCase):
	'''服务管理-新增/修改'''
	@classmethod
	def setUpClass(cls):
		cls.driver = Server()
		cls.driver.login_success()
		cls.file_path = os.path.join(run_all.fppath,'date')
		cls.servername1='服务名称'+str(int(time.time()))
		cls.servername2='服务名称'+str(int(time.time())+1)
		cls.serverid=''.join([str(random.randint(0,9)) for i in range(6) ])
		cls.driver.clickaction(cls.driver.server_topbutton_loc)
		cls.driver.clickaction(cls.driver.server_leftbutton_loc)
		time.sleep(0.25)
		# cls.driver.clickaction(cls.driver.server_newbutton_loc)
		# time.sleep(0.5)

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		# pass

	def test_001(self):
		'''进入服务列表页成功'''
		self.assertEqual("服务",self.driver.get_about(self.driver.server_tabletitle_loc))
		self.assertEqual('新增服务',self.driver.get_about(self.driver.server_newbutton_loc))

	def test_002(self):
		'''服务编码搜索成功'''
		self.driver.selecttext(self.driver.search_serverid_loc,'000001')
		self.driver.clickaction(self.driver.search_button_loc)
		time.sleep(0.25)
		self.assertEqual('MPR期刊-报纸阅读多媒体复合呈现',self.driver.get_about(self.driver.table_server_loc))

	def test_003(self):
		'''服务名称搜索成功'''
		self.driver.selecttext(self.driver.search_serverid_loc,'- 全部 -')
		self.driver.inputaction(self.driver.search_servername_loc,"MPR其它文献")
		self.driver.clickaction(self.driver.search_button_loc)
		time.sleep(0.25)
		self.assertEqual('MPR其它文献',self.driver.get_about(self.driver.table_server_loc))

	def test_004(self):
		'''关联名称搜索成功'''
		self.driver.clearaction(self.driver.search_servername_loc)
		self.driver.inputaction(self.driver.search_Association_loc,"图书")
		self.driver.clickaction(self.driver.search_button_loc)
		time.sleep(0.25)
		self.assertIn('图书',self.driver.get_about(self.driver.table_association_loc))

	def test_005(self):
		'''进入新增服务页面，服务名为空'''
		self.driver.clickaction(self.driver.server_newbutton_loc)
		time.sleep(0.5)
		self.assertEqual('新增',self.driver.get_about(self.driver.create_servertitle_loc))
		self.driver.inputaction(self.driver.create_servernameCn_loc,'    ')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'测试服务名为空')
		self.assertIn('请输入服务名称，内容限100',self.driver.get_about(self.driver.error_servernameCn_loc))

	def test_006(self):
		'''服务编码为空'''
		self.driver.inputaction(self.driver.create_serveridCn_loc,'    ')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'服务编码为空')
		self.assertIn('请获取服务编码',self.driver.get_about(self.driver.error_serveridCn_loc))
		self.assertIn('请获取服务编码',self.driver.get_about(self.driver.error_serveridEn_loc))

	def test_007(self):
		'''中文服务编码重复'''
		self.driver.inputaction(self.driver.create_serveridCn_loc,'000001')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'服务编码重复')
		self.assertIn('服务编码已存在',self.driver.get_about(self.driver.error_serveridredoCn_loc))
		self.assertIn('服务编码已存在',self.driver.get_about(self.driver.error_serveridredoEn_loc))

	def test_008(self):
		'''服务编码小于6位'''
		self.driver.inputaction(self.driver.create_serveridCn_loc,'0000')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'服务编码小于6位')
		time.sleep(0.25)
		self.assertIn('输入六位数字',self.driver.get_about(self.driver.error_serveridCn_loc))
		self.assertIn('输入六位数字',self.driver.get_about(self.driver.error_serveridEn_loc))

	def test_009(self):
		'''服务编码非数字'''
		self.driver.inputaction(self.driver.create_serveridCn_loc,'12中文2飞')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'服务编码非数字')
		time.sleep(0.25)
		self.assertIn('输入六位数字',self.driver.get_about(self.driver.error_serveridCn_loc))
		self.assertIn('输入六位数字',self.driver.get_about(self.driver.error_serveridEn_loc))

	def test_010(self):
		'''自动获取编码正常-中文'''
		self.driver.clickaction(self.driver.create_serveridbuttonCn_loc)
		time.sleep(0.5)
		self.assertNotEqual('12中文2飞',self.driver.get_attribute(self.driver.create_serveridCn_loc,'value'))
		self.assertNotEqual('12中文2飞',self.driver.get_attribute(self.driver.create_serveridEn_loc,'value'))

	def test_011(self):
		'''自动获取编码正常-英文'''
		self.driver.inputaction(self.driver.create_serveridCn_loc,'124567')
		self.driver.clickaction(self.driver.create_serveridbuttonEn_loc)
		time.sleep(0.5)
		self.assertNotEqual('124567',self.driver.get_attribute(self.driver.create_serveridCn_loc,'value'))
		self.assertNotEqual('124567',self.driver.get_attribute(self.driver.create_serveridEn_loc,'value'))

	def test_012(self):
		'''关联类型为空'''
		self.driver.clickaction(self.driver.create_serverassociationCn_loc)
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'关联类型为空')
		self.assertIn('选择关联类型',self.driver.get_about(self.driver.error_serverassociationCn_loc))

	def test_013(self):
		'''关联字段长度为空'''
		self.driver.inputaction(self.driver.create_serverlongCn_loc,'    ')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'关联类型长度为空')
		self.assertIn('输入关联字段长度',self.driver.get_about(self.driver.error_serverlongCn_loc))
		self.assertIn('输入关联字段长度',self.driver.get_about(self.driver.error_serverlongEn_loc))

	def test_014(self):
		'''关联字段长度非数字'''
		self.driver.inputaction(self.driver.create_serverlongCn_loc,'kex')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'关联类型长度非数字')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongCn_loc))
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongEn_loc))

	def test_015(self):
		'''关联字段长度小数或负数'''
		self.driver.inputaction(self.driver.create_serverlongCn_loc,'-1')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'关联类型长度负数')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongCn_loc))
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongEn_loc))
		self.driver.inputaction(self.driver.create_serverlongCn_loc,'0.25')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'关联类型长度小数')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongCn_loc))
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongEn_loc))
		self.driver.inputaction(self.driver.create_serverlongCn_loc,'0')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'关联类型长度小数')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongCn_loc))
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongEn_loc))

	def test_016(self):
		'''关联分段长度为空'''
		self.driver.inputaction(self.driver.create_serverlongCn_loc,'6')
		self.driver.selecttext(self.driver.create_serversectionCn_loc,'2')
		self.driver.clickaction(self.driver.create_serversectionsCn_1_loc)
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'关联分段长度为空')
		self.assertIn('请输入关联字段分段',self.driver.get_about(self.driver.error_serversectionNoCn_loc))

	def test_017(self):
		'''关联分段长度非数字'''
		self.driver.inputaction(self.driver.create_serversectionsCn_1_loc,'kex')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'关联分段长度非整数')
		self.assertIn('输入正整数',self.driver.get_about(self.driver.error_serversectionNoCn_loc))
		self.assertIn('输入关联字段分段',self.driver.get_about(self.driver.error_serversectionNoEn_loc))

	def test_018(self):
		'''分段长度负数'''
		self.driver.inputaction(self.driver.create_serversectionsCn_1_loc,'-1')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'关联分段长度负数')
		self.assertIn('输入正整数',self.driver.get_about(self.driver.error_serversectionNoCn_loc))
		self.assertIn('输入关联字段分段',self.driver.get_about(self.driver.error_serversectionNoEn_loc))

	def test_019(self):
		'''关联字段长度小数'''
		self.driver.inputaction(self.driver.create_serversectionsCn_1_loc,'0.25')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'关联分段长度小数')
		self.assertIn('输入正整数',self.driver.get_about(self.driver.error_serversectionNoCn_loc))
		self.assertIn('输入关联字段分段',self.driver.get_about(self.driver.error_serversectionNoEn_loc))

	def test_020(self):
		'''关联字段长度为0'''
		self.driver.inputaction(self.driver.create_serversectionsCn_1_loc,'0')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'关联分段长度为0')
		self.assertIn('输入正整数',self.driver.get_about(self.driver.error_serversectionNoCn_loc))
		self.assertIn('输入关联字段分段',self.driver.get_about(self.driver.error_serversectionNoEn_loc))

	def test_021(self):
		'''服务说明文件格式错误'''
		self.driver.find_element(self.driver.create_serverfileCnbutton_loc).send_keys(self.file_path+r'\A_006.gif')
		time.sleep(0.25)
		self.assertIn('请上传doc,docx格式文档',self.driver.get_about(self.driver.error_serverfileCn_loc))

	def test_022(self):
		'''服务简介为空'''
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'    ')
		self.driver.inputaction(self.driver.create_servernameCn_loc,'中文简介为空')
		self.assertIn('输入服务简介',self.driver.get_about(self.driver.error_serveraboutCn_loc))

	def test_023(self):
		'''服务名为空-英文'''
		self.driver.refresh()
		time.sleep(0.25)
		self.driver.inputaction(self.driver.create_servernameEn_loc,'    ')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'测试服务名为空')
		self.assertIn('请输入服务名称，内容限',self.driver.get_about(self.driver.error_servernameEn_loc))

	def test_024(self):
		'''服务编码为空-英文'''
		self.driver.inputaction(self.driver.create_serveridEn_loc,'    ')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'测试服务编码为空')
		self.assertIn('获取服务编码',self.driver.get_about(self.driver.error_serveridEn_loc))
		self.assertIn('获取服务编码',self.driver.get_about(self.driver.error_serveridCn_loc))

	def test_025(self):
		'''服务编码重复-英文'''
		self.driver.inputaction(self.driver.create_serveridEn_loc,'000001')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'测试服务编码已存在')
		self.assertIn('务编码已存在',self.driver.get_about(self.driver.error_serveridredoEn_loc))
		self.assertIn('务编码已存在',self.driver.get_about(self.driver.error_serveridredoCn_loc))

	def test_026(self):
		'''服务编码非数字-英文'''
		self.driver.inputaction(self.driver.create_serveridEn_loc,'xhongw')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'测试服务编码非数字')
		self.assertIn('输入六位数字',self.driver.get_about(self.driver.error_serveridEn_loc))
		self.assertIn('输入六位数字',self.driver.get_about(self.driver.error_serveridCn_loc))

	def test_027(self):
		'''服务编码小于6位-英文'''
		self.driver.inputaction(self.driver.create_serveridEn_loc,'1234')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'测试服务编码小于6位')
		self.assertIn('输入六位数字',self.driver.get_about(self.driver.error_serveridEn_loc))
		self.assertIn('输入六位数字',self.driver.get_about(self.driver.error_serveridCn_loc))

	def test_028(self):
		'''关联类型为空'''
		self.driver.clickaction(self.driver.create_serverassociationEn_loc)
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联类型为空')
		self.assertIn('选择关联类型',self.driver.get_about(self.driver.error_serverassociationEn_loc))

	def test_029(self):
		'''关联字段长度为空-英文'''
		self.driver.inputaction(self.driver.create_serverlongEn_loc,'    ')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联类型长度为空')
		self.assertIn('输入关联字段长度',self.driver.get_about(self.driver.error_serverlongCn_loc))
		self.assertIn('输入关联字段长度',self.driver.get_about(self.driver.error_serverlongEn_loc))

	def test_030(self):
		'''关联字段长度非数字-英文'''
		self.driver.inputaction(self.driver.create_serverlongEn_loc,'kex')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联类型长度非数字')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongCn_loc))
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongEn_loc))

	def test_031(self):
		'''关联字段长度负数-英文'''
		self.driver.inputaction(self.driver.create_serverlongEn_loc,'-1')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联类型长度负数')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongCn_loc))
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongEn_loc))

	def test_032(self):
		'''关联字段长度小数-英文'''
		self.driver.inputaction(self.driver.create_serverlongEn_loc,'0.25')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联类型长度小数')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongCn_loc))
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongEn_loc))

	def test_033(self):
		'''关联字段长度0-英文'''
		self.driver.inputaction(self.driver.create_serverlongEn_loc,'0')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联类型长度0')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongCn_loc))
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongEn_loc))

	def test_034(self):
		'''关联分段为空-英文'''
		self.driver.inputaction(self.driver.create_serverlongEn_loc,'6')
		self.driver.selecttext(self.driver.create_serversectionEn_loc,'2')
		self.driver.clickaction(self.driver.create_serversectionsEn_1_loc)
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联分段长度为空')
		self.assertIn('请输入关联字段分段',self.driver.get_about(self.driver.error_serversectionNoEn_loc))

	def test_035(self):
		'''关联分段非数字-英文'''
		self.driver.inputaction(self.driver.create_serversectionsEn_1_loc,'kex')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联分段长度非数字')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serversectionNoEn_loc))
		self.assertIn('请输入关联字段分段',self.driver.get_about(self.driver.error_serversectionNoCn_loc))

	def test_036(self):
		'''关联分段负数-英文'''
		self.driver.inputaction(self.driver.create_serversectionsEn_1_loc,'-1')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联分段长度负数')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serversectionNoEn_loc))
		self.assertIn('请输入关联字段分段',self.driver.get_about(self.driver.error_serversectionNoCn_loc))

	def test_037(self):
		'''关联字段小数-英文'''
		self.driver.inputaction(self.driver.create_serversectionsEn_1_loc,'0.25')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联分段长度小数')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serversectionNoEn_loc))
		self.assertIn('请输入关联字段分段',self.driver.get_about(self.driver.error_serversectionNoCn_loc))

	def test_038(self):
		'''关联分段长度0-英文'''
		self.driver.inputaction(self.driver.create_serversectionsEn_1_loc,'0')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联分段长度0')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serversectionNoEn_loc))
		self.assertIn('请输入关联字段分段',self.driver.get_about(self.driver.error_serversectionNoCn_loc))

	def test_039(self):
		'''服务说明文件格式错误-英文'''
		self.driver.find_element(self.driver.create_serverfileEnbutton_loc).send_keys(self.file_path+r'\A_006.gif')
		time.sleep(0.25)
		self.assertIn('请上传doc,docx格式文档',self.driver.get_about(self.driver.error_serverfileEn_loc))

	def test_040(self):
		'''服务简介为空-英文'''
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'    ')
		self.driver.inputaction(self.driver.create_servernameEn_loc,'英文简介为空')
		self.assertIn('输入服务简介',self.driver.get_about(self.driver.error_serveraboutEn_loc))

	def test_041(self):
		'''服务说明文件为空-中文/英文'''
		self.driver.refresh()
		self.driver.inputaction(self.driver.create_servernameCn_loc,self.servername1)
		self.driver.inputaction(self.driver.create_serveridCn_loc,self.serverid)
		self.driver.clickaction(self.driver.create_serverassocbuttonCn_loc)
		time.sleep(0.25)
		self.driver.clickaction(self.driver.create_serverassocNo1Cn_loc)
		time.sleep(0.25)
		self.assertTrue(self.driver.get_attribute(self.driver.create_serverassociationCn_loc,'value'))
		self.assertTrue(self.driver.get_attribute(self.driver.create_serverassociationEn_loc,'value'))
		self.driver.inputaction(self.driver.create_serverlongCn_loc,'6')
		self.driver.selecttext(self.driver.create_serversectionCn_loc,'2')
		self.driver.inputaction(self.driver.create_serversectionsCn_1_loc,'3')
		self.driver.inputaction(self.driver.create_serversectionsCn_2_loc,'8')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'测试数据')
		self.driver.inputaction(self.driver.create_servernameEn_loc,self.servername1)
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'测试数据En')
		time.sleep(0.25)
		self.driver.clickaction(self.driver.create_serverbutton_loc)
		time.sleep(0.75)
		self.assertIn('请上传服务说明文件',self.driver.get_about(self.driver.error_serverfileCn_loc))
		self.assertIn('请上传服务说明文件',self.driver.get_about(self.driver.error_serverfileEn_loc))

	def test_042(self):
		'''关联分段和不一致'''
		self.driver.find_element(self.driver.create_serverfileCnbutton_loc).send_keys(self.file_path+r'\拟申请关联服务实施计划.doc')
		time.sleep(0.25)
		self.driver.find_element(self.driver.create_serverfileEnbutton_loc).send_keys(self.file_path+r'\拟申请关联服务实施计划.doc')
		time.sleep(0.5)
		self.driver.clickaction(self.driver.create_serverbutton_loc)
		time.sleep(1.5)
		self.assertIn('段数值之和必须等于关联字段项的输入值',self.driver.get_about(self.driver.error_serversectionsumCn_loc))
		self.assertIn('段数值之和必须等于关联字段项的输入值',self.driver.get_about(self.driver.error_serversectionsumEn_loc))

	def test_043(self):
		'''验证关联类型中英文联动'''
		self.driver.refresh()
		self.driver.clickaction(self.driver.create_serverassocbuttonCn_loc)
		time.sleep(0.25)
		self.driver.clickaction(self.driver.create_serverassocNo1Cn_loc)
		Cn_assoc =self.driver.get_attribute(self.driver.create_serverassociationCn_loc,'value')
		En_assoc =self.driver.get_attribute(self.driver.create_serverassociationEn_loc,'value')
		self.assertEqual(Cn_assoc,En_assoc)
		self.driver.refresh()
		time.sleep(0.25)
		self.driver.clickaction(self.driver.create_serverassocbuttonEn_loc)
		time.sleep(0.25)
		self.driver.clickaction(self.driver.create_serverassocNo1En_loc)
		Cn_assoc1 =self.driver.get_attribute(self.driver.create_serverassociationCn_loc,'value')
		En_assoc1 =self.driver.get_attribute(self.driver.create_serverassociationEn_loc,'value')
		self.assertEqual(Cn_assoc1,En_assoc1)

	def test_044(self):
		'''字段长度中英文联动'''
		self.driver.inputaction(self.driver.create_serverlongCn_loc,'6')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'测试')
		time.sleep(0.25)
		Cn_log = self.driver.get_attribute(self.driver.create_serverlongCn_loc,'value')
		En_log = self.driver.get_attribute(self.driver.create_serverlongEn_loc,'value')
		self.assertEqual(Cn_log,En_log)
		self.driver.inputaction(self.driver.create_serverlongEn_loc,'8')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'测试')
		time.sleep(0.25)
		Cn_log1 = self.driver.get_attribute(self.driver.create_serverlongCn_loc,'value')
		En_log1 = self.driver.get_attribute(self.driver.create_serverlongEn_loc,'value')
		self.assertEqual(Cn_log1,En_log1)

	def test_045(self):
		'''连续申请成功'''
		self.driver.refresh()
		time.sleep(0.25)
		self.driver.inputaction(self.driver.create_servernameCn_loc,self.servername1)
		self.driver.inputaction(self.driver.create_serveridCn_loc,self.serverid)
		self.driver.clickaction(self.driver.create_serverassocbuttonCn_loc)
		time.sleep(0.25)
		self.driver.clickaction(self.driver.create_serverassocNo1Cn_loc)
		time.sleep(0.25)
		self.assertTrue(self.driver.get_attribute(self.driver.create_serverassociationCn_loc,'value'))
		self.assertTrue(self.driver.get_attribute(self.driver.create_serverassociationEn_loc,'value'))
		self.driver.inputaction(self.driver.create_serverlongCn_loc,'6')
		self.driver.selecttext(self.driver.create_serversectionCn_loc,'2')
		self.driver.inputaction(self.driver.create_serversectionsCn_1_loc,'3')
		self.driver.inputaction(self.driver.create_serversectionsCn_2_loc,'3')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'测试数据')
		self.driver.inputaction(self.driver.create_servernameEn_loc,self.servername1)
		self.driver.find_element(self.driver.create_serverfileCnbutton_loc).send_keys(self.file_path+r'\拟申请关联服务实施计划.doc')
		time.sleep(0.25)
		self.driver.find_element(self.driver.create_serverfileEnbutton_loc).send_keys(self.file_path+r'\拟申请关联服务实施计划.doc')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'测试数据En')
		time.sleep(1)
		self.driver.clickaction(self.driver.create_serveragain_loc)
		time.sleep(1.5)
		self.assertIn(self.servername1,self.driver.get_about(self.driver.create_againtips_loc))
		self.driver.clickaction(self.driver.create_againbutton_loc)
		time.sleep(1)
		self.assertIn('新增',self.driver.get_about(self.driver.create_servertitle_loc))

	def test_046(self):
		'''服务名称中文重复'''
		self.driver.inputaction(self.driver.create_servernameCn_loc,self.servername1)
		self.driver.inputaction(self.driver.create_servernameEn_loc,self.servername1)
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'测试数据')
		time.sleep(0.25)
		self.assertIn("服务名称已存在",self.driver.get_about(self.driver.error_servernameexistCn_loc))
		self.assertIn("服务名称已存在",self.driver.get_about(self.driver.error_servernameexistEn_loc))

	def test_047(self):
		'''关联类型已存在'''
		self.driver.clickaction(self.driver.create_serverassocbuttonCn_loc)
		time.sleep(0.25)
		self.driver.clickaction(self.driver.create_serverassocNo1Cn_loc)
		time.sleep(0.5)
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'测试数据')
		self.assertIn("关联类型已存在",self.driver.get_about(self.driver.error_serverassocexitCn_loc))
		self.assertIn("关联类型已存在",self.driver.get_about(self.driver.error_serverassocexitEn_loc))

	def test_048(self):
		'''创建成功'''
		self.driver.clickaction(self.driver.server_leftbutton_loc)
		time.sleep(0.5)
		self.assertEqual(self.servername1,self.driver.get_about(self.driver.table_server_loc))

	def test_049(self):
		'''查看功能正常'''
		self.driver.clickaction(self.driver.table_view_loc)
		time.sleep(0.5)
		self.assertEqual('查看',self.driver.get_about(self.driver.view_servertitle_loc))
		self.assertEqual(self.servername1,self.driver.get_about(self.driver.view_servernameCn_loc))
		self.assertEqual(self.servername1,self.driver.get_about(self.driver.view_servernameEn_loc))
		self.assertEqual(self.serverid,self.driver.get_about(self.driver.view_serveridCn_loc))
		self.assertEqual(self.serverid,self.driver.get_about(self.driver.view_serveridEn_loc))
		self.assertEqual('6',self.driver.get_about(self.driver.view_serverlongCn_loc))
		self.assertEqual('6',self.driver.get_about(self.driver.view_serverlongEn_loc))
		self.assertEqual('3+3',self.driver.get_about(self.driver.view_serversectionCn_loc))
		self.assertEqual('3+3',self.driver.get_about(self.driver.view_serversectionEn_loc))

	def test_050(self):
		'''进入修改页面-服务名称为空'''
		self.driver.clickaction(self.driver.view_serveredit_loc)
		time.sleep(0.5)
		self.assertEqual('修改',self.driver.get_about(self.driver.view_servertitle_loc))
		self.driver.inputaction(self.driver.create_servernameCn_loc,'    ')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'测试服务名为空')
		self.assertIn('请输入服务名称，内容限100',self.driver.get_about(self.driver.error_servernameCn_loc))

	def test_051(self):
		'''修改-服务名称已存在'''
		self.driver.inputaction(self.driver.create_servernameCn_loc,'MPR期刊-报纸阅读多媒体复合呈现')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'测试服务名已存在')
		time.sleep(0.25)
		self.assertIn('服务名称已存在',self.driver.get_about(self.driver.error_servernameexistCn_loc))

	def test_052(self):
		'''修改-服务编码为空'''
		self.driver.inputaction(self.driver.create_serveridCn_loc,'    ')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'服务编码为空')
		self.assertIn('请获取服务编码',self.driver.get_about(self.driver.error_serveridCn_loc))
		self.assertIn('请获取服务编码',self.driver.get_about(self.driver.error_serveridEn_loc))

	def test_053(self):
		'''中文服务编码重复'''
		self.driver.inputaction(self.driver.create_serveridCn_loc,'000001')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'服务编码重复')
		self.assertIn('服务编码已存在',self.driver.get_about(self.driver.error_serveridredoCn_loc))
		self.assertIn('服务编码已存在',self.driver.get_about(self.driver.error_serveridredoEn_loc))

	def test_054(self):
		'''修改-服务编码小于6位'''
		self.driver.inputaction(self.driver.create_serveridCn_loc,'0000')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'服务编码小于6位')
		time.sleep(0.25)
		self.assertIn('输入六位数字',self.driver.get_about(self.driver.error_serveridCn_loc))
		self.assertIn('输入六位数字',self.driver.get_about(self.driver.error_serveridEn_loc))

	def test_055(self):
		'''修改-服务编码非数字'''
		self.driver.inputaction(self.driver.create_serveridCn_loc,'12中文2飞')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'服务编码非数字')
		time.sleep(0.25)
		self.assertIn('输入六位数字',self.driver.get_about(self.driver.error_serveridCn_loc))
		self.assertIn('输入六位数字',self.driver.get_about(self.driver.error_serveridEn_loc))

	def test_056(self):
		'''修改-自动获取编码正常-中文'''
		self.driver.clickaction(self.driver.create_serveridbuttonCn_loc)
		time.sleep(0.5)
		self.assertNotEqual('12中文2飞',self.driver.get_attribute(self.driver.create_serveridCn_loc,'value'))
		self.assertNotEqual('12中文2飞',self.driver.get_attribute(self.driver.create_serveridEn_loc,'value'))

	def test_057(self):
		'''修改-自动获取编码正常-英文'''
		self.driver.inputaction(self.driver.create_serveridCn_loc,'124567')
		self.driver.clickaction(self.driver.create_serveridbuttonEn_loc)
		time.sleep(0.5)
		self.assertNotEqual('124567',self.driver.get_attribute(self.driver.create_serveridCn_loc,'value'))
		self.assertNotEqual('124567',self.driver.get_attribute(self.driver.create_serveridEn_loc,'value'))

	def test_058(self):
		'''修改-关联字段长度为空'''
		self.driver.inputaction(self.driver.create_serverlongCn_loc,'    ')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'关联类型长度为空')
		self.assertIn('输入关联字段长度',self.driver.get_about(self.driver.error_serverlongCn_loc))
		self.assertIn('输入关联字段长度',self.driver.get_about(self.driver.error_serverlongEn_loc))

	def test_059(self):
		'''修改-关联字段长度非数字'''
		self.driver.inputaction(self.driver.create_serverlongCn_loc,'kex')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'关联类型长度非数字')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongCn_loc))
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongEn_loc))

	def test_060(self):
		'''关联字段长度小数或负数'''
		self.driver.inputaction(self.driver.create_serverlongCn_loc,'-1')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'关联类型长度负数')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongCn_loc))
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongEn_loc))
		self.driver.inputaction(self.driver.create_serverlongCn_loc,'0.25')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'关联类型长度小数')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongCn_loc))
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongEn_loc))
		self.driver.inputaction(self.driver.create_serverlongCn_loc,'0')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'关联类型长度小数')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongCn_loc))
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongEn_loc))

	def test_061(self):
		'''修改-关联分段非数字'''
		self.driver.inputaction(self.driver.create_serverlongCn_loc,'6')
		self.driver.inputaction(self.driver.create_serversectionsCn_1_loc,'kex')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'关联分段长度非整数')
		self.assertIn('输入正整数',self.driver.get_about(self.driver.error_serversectionNoCn_loc))

	def test_062(self):
		'''修改-分段长度负数'''
		self.driver.inputaction(self.driver.create_serversectionsCn_1_loc,'-1')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'关联分段长度负数')
		self.assertIn('输入正整数',self.driver.get_about(self.driver.error_serversectionNoCn_loc))

	def test_063(self):
		'''修改-关联字段长度小数'''
		self.driver.inputaction(self.driver.create_serversectionsCn_1_loc,'0.25')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'关联分段长度小数')
		self.assertIn('输入正整数',self.driver.get_about(self.driver.error_serversectionNoCn_loc))

	def test_064(self):
		'''修改-关联字段长度为0'''
		self.driver.inputaction(self.driver.create_serversectionsCn_1_loc,'0')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'关联分段长度为0')
		self.assertIn('输入正整数',self.driver.get_about(self.driver.error_serversectionNoCn_loc))

	def test_065(self):
		'''修改-服务说明文件格式错误'''
		self.driver.find_element(self.driver.create_serverfileCnbutton_loc).send_keys(self.file_path+r'\A_006.gif')
		time.sleep(0.25)
		self.assertIn('请上传doc,docx格式文档',self.driver.get_about(self.driver.error_serverfileCn_loc))

	def test_066(self):
		'''修改-服务简介为空'''
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'    ')
		self.driver.inputaction(self.driver.create_servernameCn_loc,'中文简介为空')
		self.assertIn('输入服务简介',self.driver.get_about(self.driver.error_serveraboutCn_loc))

	def test_067(self):
		'''修改-服务名为空-英文'''
		self.driver.refresh()
		time.sleep(0.25)
		self.driver.inputaction(self.driver.create_servernameEn_loc,'    ')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'测试服务名为空')
		self.assertIn('请输入服务名称，内容限',self.driver.get_about(self.driver.error_servernameEn_loc))

	def test_068(self):
		'''修改-服务编码为空-英文'''
		self.driver.inputaction(self.driver.create_serveridEn_loc,'    ')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'测试服务编码为空')
		self.assertIn('获取服务编码',self.driver.get_about(self.driver.error_serveridEn_loc))
		self.assertIn('获取服务编码',self.driver.get_about(self.driver.error_serveridCn_loc))

	def test_069(self):
		'''修改-服务名已存在英文'''
		self.driver.refresh()
		time.sleep(0.25)
		self.driver.inputaction(self.driver.create_servernameEn_loc,'MPR journal - multimedia composite presentation')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'测试服务名已存在')
		time.sleep(0.5)
		self.assertIn('服务名称已存在',self.driver.get_about(self.driver.error_servernameexistEn_loc))

	def test_070(self):
		'''修改-服务编码重复-英文'''
		self.driver.inputaction(self.driver.create_serveridEn_loc,'000001')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'测试服务编码已存在')
		time.sleep(0.25)
		self.assertIn('务编码已存在',self.driver.get_about(self.driver.error_serveridredoEn_loc))
		self.assertIn('务编码已存在',self.driver.get_about(self.driver.error_serveridredoCn_loc))

	def test_080(self):
		'''修改-服务编码非数字-英文'''
		self.driver.inputaction(self.driver.create_serveridEn_loc,'xhongw')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'测试服务编码非数字')
		self.assertIn('输入六位数字',self.driver.get_about(self.driver.error_serveridEn_loc))
		self.assertIn('输入六位数字',self.driver.get_about(self.driver.error_serveridCn_loc))

	def test_081(self):
		'''修改-服务编码小于6位-英文'''
		self.driver.inputaction(self.driver.create_serveridEn_loc,'1234')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'测试服务编码小于6位')
		self.assertIn('输入六位数字',self.driver.get_about(self.driver.error_serveridEn_loc))
		self.assertIn('输入六位数字',self.driver.get_about(self.driver.error_serveridCn_loc))

	def test_082(self):
		'''修改-关联字段长度为空-英文'''
		self.driver.inputaction(self.driver.create_serverlongEn_loc,'    ')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联类型长度为空')
		self.assertIn('输入关联字段长度',self.driver.get_about(self.driver.error_serverlongCn_loc))
		self.assertIn('输入关联字段长度',self.driver.get_about(self.driver.error_serverlongEn_loc))

	def test_083(self):
		'''修改-关联字段长度非数字-英文'''
		self.driver.inputaction(self.driver.create_serverlongEn_loc,'kex')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联类型长度非数字')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongCn_loc))
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongEn_loc))

	def test_084(self):
		'''修改-关联字段长度负数-英文'''
		self.driver.inputaction(self.driver.create_serverlongEn_loc,'-1')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联类型长度负数')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongCn_loc))
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongEn_loc))

	def test_085(self):
		'''修改-关联字段长度小数-英文'''
		self.driver.inputaction(self.driver.create_serverlongEn_loc,'0.25')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联类型长度小数')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongCn_loc))
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongEn_loc))

	def test_086(self):
		'''修改-关联字段长度0-英文'''
		self.driver.inputaction(self.driver.create_serverlongEn_loc,'0')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联类型长度0')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongCn_loc))
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serverlongEn_loc))

	def test_087(self):
		'''修改-联分段为空-英文'''
		self.driver.inputaction(self.driver.create_serverlongEn_loc,'6')
		self.driver.inputaction(self.driver.create_serversectionsEn_1_loc,'    ')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联分段长度为空')
		self.assertIn('请输入关联字段分段',self.driver.get_about(self.driver.error_serversectionNoEn_loc))

	def test_088(self):
		'''修改-关联分段非数字-英文'''
		self.driver.inputaction(self.driver.create_serversectionsEn_1_loc,'kex')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联分段长度非数字')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serversectionNoEn_loc))

	def test_089(self):
		'''修改-关联分段负数-英文'''
		self.driver.inputaction(self.driver.create_serversectionsEn_1_loc,'-1')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联分段长度负数')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serversectionNoEn_loc))

	def test_090(self):
		'''修改-关联分段负数-英文'''
		self.driver.inputaction(self.driver.create_serversectionsEn_1_loc,'0.25')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联分段长度小数')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serversectionNoEn_loc))

	def test_091(self):
		'''修改-关联分段长度0-英文'''
		self.driver.inputaction(self.driver.create_serversectionsEn_1_loc,'0')
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'关联分段长度0')
		self.assertIn('请输入正整数',self.driver.get_about(self.driver.error_serversectionNoEn_loc))

	def test_092(self):
		'''修改-服务说明文件格式错误-英文'''
		self.driver.find_element(self.driver.create_serverfileEnbutton_loc).send_keys(self.file_path+r'\A_006.gif')
		time.sleep(0.25)
		self.assertIn('请上传doc,docx格式文档',self.driver.get_about(self.driver.error_serverfileEn_loc))

	def test_093(self):
		'''服务简介为空-英文'''
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'    ')
		self.driver.inputaction(self.driver.create_servernameEn_loc,'英文简介为空')
		self.assertIn('输入服务简介',self.driver.get_about(self.driver.error_serveraboutEn_loc))

	def test_094(self):
		'''修改-分段和与总数不一致'''
		self.driver.clickaction(self.driver.server_leftbutton_loc)
		time.sleep(0.25)
		self.driver.clickaction(self.driver.table_view_loc)
		time.sleep(0.5)
		self.driver.clickaction(self.driver.view_serveredit_loc)
		time.sleep(0.5)
		self.driver.inputaction(self.driver.create_servernameCn_loc,self.servername2)
		self.driver.inputaction(self.driver.create_serveridCn_loc,str(int(self.serverid)+1))
		time.sleep(0.25)
		self.driver.inputaction(self.driver.create_serverlongCn_loc,'7')
		self.driver.selecttext(self.driver.create_serversectionCn_loc,'2')
		self.driver.inputaction(self.driver.create_serversectionsCn_1_loc,'3')
		self.driver.inputaction(self.driver.create_serversectionsCn_2_loc,'5')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'测试数据')
		self.driver.inputaction(self.driver.create_servernameEn_loc,self.servername2)
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'测试数据En')
		time.sleep(0.5)
		self.driver.clickaction(self.driver.alter_serverbutton_loc)
		time.sleep(0.5)
		self.assertIn('段数值之和必须等于关联字段项的输入值',self.driver.get_about(self.driver.error_serversectionsumCn_loc))
		self.assertIn('段数值之和必须等于关联字段项的输入值',self.driver.get_about(self.driver.error_serversectionsumEn_loc))

	def test_095(self):
		'''修改成功'''
		self.driver.inputaction(self.driver.create_serversectionsCn_2_loc,'4')
		self.driver.clickaction(self.driver.alter_serverbutton_loc)
		time.sleep(1)
		self.assertEqual(self.servername2,self.driver.get_about(self.driver.table_server_loc))

	def test_096(self):
		'''查看修改后结果'''
		self.driver.clickaction(self.driver.table_view_loc)
		time.sleep(0.5)
		self.assertEqual('查看',self.driver.get_about(self.driver.view_servertitle_loc))
		self.assertEqual(self.servername2,self.driver.get_about(self.driver.view_servernameCn_loc))
		self.assertEqual(self.servername2,self.driver.get_about(self.driver.view_servernameEn_loc))
		self.assertEqual(str(int(self.serverid)+1),self.driver.get_about(self.driver.view_serveridCn_loc))
		self.assertEqual(str(int(self.serverid)+1),self.driver.get_about(self.driver.view_serveridEn_loc))
		self.assertEqual('7',self.driver.get_about(self.driver.view_serverlongCn_loc))
		self.assertEqual('7',self.driver.get_about(self.driver.view_serverlongEn_loc))
		self.assertEqual('3+4',self.driver.get_about(self.driver.view_serversectionCn_loc))
		self.assertEqual('3+4',self.driver.get_about(self.driver.view_serversectionEn_loc))

	def test_097(self):
		'''table修改按钮修改成功'''
		self.driver.clickaction(self.driver.server_leftbutton_loc)
		time.sleep(0.5)
		self.driver.clickaction(self.driver.table_edit_loc)
		time.sleep(0.5)
		self.assertEqual('修改',self.driver.get_about(self.driver.view_servertitle_loc))
		self.driver.inputaction(self.driver.create_servernameCn_loc,self.servername1)
		self.driver.inputaction(self.driver.create_serveridCn_loc,self.serverid)
		time.sleep(0.25)
		self.driver.inputaction(self.driver.create_serverlongCn_loc,'6')
		self.driver.selecttext(self.driver.create_serversectionCn_loc,'2')
		self.driver.inputaction(self.driver.create_serversectionsCn_1_loc,'3')
		self.driver.inputaction(self.driver.create_serversectionsCn_2_loc,'3')
		self.driver.inputaction(self.driver.create_serveraboutCn_loc,'测试数据')
		self.driver.inputaction(self.driver.create_servernameEn_loc,self.servername1)
		self.driver.inputaction(self.driver.create_serveraboutEn_loc,'测试数据En')
		time.sleep(0.5)
		self.driver.clickaction(self.driver.alter_serverbutton_loc)
		time.sleep(1)
		self.assertEqual(self.servername1,self.driver.get_about(self.driver.table_server_loc))

	def test_098(self):
		'''查看修改后结果'''
		self.driver.clickaction(self.driver.table_view_loc)
		time.sleep(0.5)
		self.assertEqual('查看',self.driver.get_about(self.driver.view_servertitle_loc))
		self.assertEqual(self.servername1,self.driver.get_about(self.driver.view_servernameCn_loc))
		self.assertEqual(self.servername1,self.driver.get_about(self.driver.view_servernameEn_loc))
		self.assertEqual(self.serverid,self.driver.get_about(self.driver.view_serveridCn_loc))
		self.assertEqual(self.serverid,self.driver.get_about(self.driver.view_serveridEn_loc))
		self.assertEqual('6',self.driver.get_about(self.driver.view_serverlongCn_loc))
		self.assertEqual('6',self.driver.get_about(self.driver.view_serverlongEn_loc))
		self.assertEqual('3+3',self.driver.get_about(self.driver.view_serversectionCn_loc))
		self.assertEqual('3+3',self.driver.get_about(self.driver.view_serversectionEn_loc))



if __name__=="__mian__":
	unittest.main()
