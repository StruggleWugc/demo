import sys,time
sys.path.append("..")
import random,os
from  common.function import getChar, lenJudge, getCharEx
from page.registerModular import registerModular
from time import sleep
import unittest
import run_all

class web_SPRegisterTest(unittest.TestCase):
    '''SP账户注册'''
    @classmethod
    def setUpClass(cls):
        cls.sp = registerModular()
    # variable.CurrentTest.append('web_SPRegisterTest')
        cls.file_path = os.path.join(run_all.fppath,'date')
        cls.sp.open(registerModular.url)
        time.sleep(0.5)
        cls.sp.select_language()

    @classmethod
    def tearDownClass(cls):
        cls.sp.quit()

    def test_001(self):
        '''机构必填项为空'''
        self.sp.clickaction(self.sp.submit_loc)
        sleep(1)
        self.assertIn("选择所属区域",self.sp.get_about(self.sp.error_areaId_loc))
        self.assertIn("输入机构名称",self.sp.get_about(self.sp.error_orgName_loc))
        self.assertIn("上传文件",self.sp.get_about(self.sp.error_logoText_loc))
        self.assertIn("输入注册地址",self.sp.get_about(self.sp.error_orgAddress_loc))
        self.assertIn("输入统一社会信用代码",self.sp.get_about(self.sp.error_idNumber_loc))
        self.assertIn("上传文件",self.sp.get_about(self.sp.error_scanCodeText_loc))
        self.assertIn("请输入联系人姓名",self.sp.get_about(self.sp.error_linkman_loc))
        self.assertIn("请输入手机号",self.sp.get_about(self.sp.error_mobile_loc))
        self.assertIn("请输入联系邮箱",self.sp.get_about(self.sp.error_linkmanEmail_loc))
        self.assertIn("请输入通讯地址",self.sp.get_about(self.sp.error_linkmanContact_loc))
        self.assertIn("请输入用户名",self.sp.get_about(self.sp.error_email_loc))
        self.assertIn("请输入邮箱验证码",self.sp.get_about(self.sp.error_emailValidateCode_loc))

    def ttest_01(self):
        '''必填项-输入框/下拉框为空-注册失败'''
        ##基本信息
        #注册用户类型为空
        self.sp.select_by_index(self.sp.registerTypeId_loc, 0)
        self.sp.select_by_index(self.sp.areaId_loc, random.randint(1, 176))
        self.sp.reg_lineEdit(self.sp.orgName_loc,'测试部落')
        sleep(1)
        self.sp.find_element(self.sp.logo_btn_loc).send_keys(self.file_path+r'\A_016.jpg')
        # self.sp.find_element(self.sp.logo_btn_loc).send_keys(self.file_path+r'\A_016.jpg')                            #上传机构logo
        self.sp.reg_lineEdit(self.sp.orgAddress_loc, '深圳')
        self.sp.reg_lineEdit(self.sp.idNumber_loc, '111111111111111')
        self.sp.find_element(self.sp.scanCodeFile_loc).send_keys(self.file_path+r'\A_016.jpg')                          #上传组织代码扫描件
        # sp.reg_uploadFile(sp.scanCodeFile_loc,'C:\\Users\\shigx1219\\Pictures\\test\\A_016.jpg')
        self.sp.reg_lineEdit(self.sp.orgWebsite_loc, 'www.baidu.com')
        ##联系人信息
        self.sp.reg_lineEdit(self.sp.linkman_loc, 'shi')
        self.sp.select_by_index(self.sp.phoneType_loc, random.randint(0, 3))
        self.sp.reg_lineEdit(self.sp.phoneArea_loc, '0755')
        self.sp.reg_lineEdit(self.sp.phone_loc, '8485666')
        self.sp.reg_lineEdit(self.sp.phoneExt_loc, '755')
        self.sp.select_by_index(self.sp.mobileType_loc, random.randint(0, 3))
        self.sp.reg_lineEdit(self.sp.mobile_loc, '15900000051')
        self.sp.reg_lineEdit(self.sp.linkmanPosition_loc, '总监')
        self.sp.reg_lineEdit(self.sp.linkmanEmail_loc, 'xitesta01@163.com')
        self.sp.reg_lineEdit(self.sp.linkmanContact_loc, '深圳')
        self.sp.reg_lineEdit(self.sp.linkmanZip_loc, '518000')
        ##拟申请关联服务信息
        self.sp.reg_lineEdit(self.sp.serviceName_loc, 'MMM')
        self.sp.find_element(self.sp.p_file_btn_loc).send_keys(self.file_path+r'\拟申请关联服务实施计划.doc')
        self.sp.find_element(self.sp.s_file_btn_loc).send_keys(self.file_path+r'\拟申请关联服务实施计划.doc')
        # sp.reg_uploadFile(sp.p_file_btn_loc,'C:\\Users\\shigx1219\\Pictures\\test\\拟申请关联服务实施计划.doc')
        # sp.reg_uploadFile(sp.s_file_btn_loc,'C:\\Users\\shigx1219\\Pictures\\test\\拟申请关联服务实施说明.doc')
        ##账户信息
        self.sp.reg_lineEdit(self.sp.email_loc, 'xitest090@163.com')
        # sp.reg_button(sp.send_email_btn_loc)                                                                          #发送邮件
        # sp.reg_waitForCode()
        
        self.sp.reg_submit()
        sleep(1)
        self.assertEqual(self.sp.error_hint(self.sp.error_registerTypeId_loc), '请选择')
        #所属区域为空
        self.sp.select_by_index(self.sp.registerTypeId_loc, 1)
        self.sp.select_by_index(self.sp.areaId_loc, 0)
        self.sp.reg_submit()
        sleep(1)
        self.assertEqual(self.sp.error_hint(self.sp.error_areaId_loc), '请选择')
        #机构名称为空
        self.sp.select_by_index(self.sp.areaId_loc, random.randint(1, 176))
        self.sp.reg_lineEdit(self.sp.orgName_loc,'')
        self.sp.reg_submit()
        sleep(1)
        self.assertEqual(self.sp.error_hint(self.sp.error_orgName_loc), '请输入内容')
        #注册地址为空
        self.sp.reg_lineEdit(self.sp.orgName_loc,'测试部落')
        self.sp.reg_lineEdit(self.sp.orgAddress_loc, '')
        self.sp.reg_submit()
        sleep(1)
        self.assertEqual(self.sp.error_hint(self.sp.error_orgAddress_loc), '请输入内容')
        #统一社会信用代码为空
        self.sp.reg_lineEdit(self.sp.orgAddress_loc, '深圳')
        self.sp.reg_lineEdit(self.sp.idNumber_loc, '')
        self.sp.reg_submit()
        sleep(1)
        self.assertEqual(self.sp.error_hint(self.sp.error_idNumber_loc), '请输入内容')
        #联系人姓名为空
        self.sp.reg_lineEdit(self.sp.idNumber_loc, '121212121212121212')
        self.sp.reg_lineEdit(self.sp.linkman_loc, '')
        self.sp.reg_submit()
        sleep(1)
        self.assertEqual(self.sp.error_hint(self.sp.error_linkman_loc), '请输入内容')
        #联系人电话（手机）为空
        self.sp.reg_lineEdit(self.sp.linkman_loc, 'shi')
        self.sp.reg_lineEdit(self.sp.mobile_loc, '')
        self.sp.reg_submit()
        sleep(1)
        self.assertEqual(self.sp.error_hint(self.sp.error_mobile_loc), '请输入内容')
        #电子邮件为空
        self.sp.reg_lineEdit(self.sp.mobile_loc, '15100000050')
        self.sp.reg_lineEdit(self.sp.linkmanEmail_loc, '')
        self.sp.reg_submit()
        sleep(1)
        self.assertEqual(self.sp.error_hint(self.sp.error_linkmanEmail_loc), '请输入内容')
        #通讯地址为空
        self.sp.reg_lineEdit(self.sp.linkmanEmail_loc, 'xitest050@163.com')
        self.sp.reg_lineEdit(self.sp.linkmanContact_loc, '')
        self.sp.reg_submit()
        sleep(1)
        self.assertEqual(self.sp.error_hint(self.sp.error_linkmanContact_loc), '请输入内容')
        #服务为空
        self.sp.reg_lineEdit(self.sp.linkmanContact_loc, '深圳')
        self.sp.reg_lineEdit(self.sp.serviceName_loc, '')
        self.sp.reg_submit()
        sleep(1)
        self.assertEqual(self.sp.error_hint(self.sp.error_serviceName_loc), '请输入内容')
        #用户名为空
        self.sp.reg_lineEdit(self.sp.serviceName_loc, '89F')
        self.sp.reg_lineEdit(self.sp.email_loc, '')
        self.sp.reg_submit()
        sleep(1)
        self.assertEqual(self.sp.error_hint(self.sp.error_email_loc), '请输入内容')
        #邮箱验证码为空
        self.sp.reg_lineEdit(self.sp.email_loc, 'xitesta050@163.com')
        self.sp.reg_lineEdit(self.sp.emailValidateCode_loc, '')
        self.sp.reg_submit()
        sleep(1)
        self.assertEqual(self.sp.error_hint(self.sp.error_emailValidateCode_loc), '请输入内容')


    def test_002(self):
        '''必填项-机构名称已经存在-注册失败'''
        self.sp.inputaction(self.sp.orgName_loc,'12132213')
        self.sp.clickaction(self.sp.submit_loc)
        self.assertIn("机构名称已存在",self.sp.get_about(self.sp.error_orgName_loc))

    def test_003(self):
        '''必填项-机构名称长度101-自动截取100长度'''
        self.sp.reg_lineEdit(self.sp.orgName_loc,getChar('机构名称100', 101))
        sleep(1)
        self.assertEqual(lenJudge(self.sp, self.sp.orgName_loc, 100), True)
        
    def test_004(self):
        '''必填项-统一社会信用代码为19位-自动截取'''
        self.sp.reg_lineEdit(self.sp.orgName_loc,'机构名称1')
        self.sp.reg_lineEdit(self.sp.idNumber_loc,getChar('12', 19))
        sleep(0.5)
        long= len(self.sp.find_element(self.sp.idNumber_loc).get_attribute('value'))
        self.assertEqual(long,int(18))

    ###功能暂未实现
    def test_005(self):
        '''必填项-统一社会信用代码为14位-注册失败'''
        self.sp.reg_lineEdit(self.sp.idNumber_loc,getChar('12', 14))
        self.sp.reg_submit()
        sleep(1)
        self.assertEqual(self.sp.error_hint(self.sp.error_idNumber_loc), '请输入15~18位数字和字母')
        
    def test_006(self):
        '''必填项-统一社会信用代码含汉字特殊字符-注册失败'''
        self.sp.reg_lineEdit(self.sp.idNumber_loc,getChar('12；是', 15))
        self.sp.reg_submit()
        sleep(1)
        self.assertEqual(self.sp.error_hint(self.sp.error_idNumber_loc), '请输入15~18位数字和字母')


    def test_007(self):
        '''官方网址输入错误格式-注册失败'''
        self.sp.reg_lineEdit(self.sp.idNumber_loc,getChar('12', 15))
        self.sp.reg_lineEdit(self.sp.orgWebsite_loc,getChar('12', 14))
        self.sp.reg_submit()
        self.assertEqual(self.sp.error_hint(self.sp.error_orgWebsite_loc), '请输入合法的网址')

    def test_008(self):
        '''个人用户必填项为空'''
        self.sp.clickaction(self.sp.orgTypeId2_loc)
        sleep(0.5)
        self.sp.clickaction(self.sp.submit_loc)
        self.assertIn('输入姓名全称',self.sp.get_about(self.sp.error_personagename_loc))
        self.assertIn('请输入您的住址',self.sp.get_about(self.sp.error_personageadd_loc))
        self.assertIn('输入您的身份证号码',self.sp.get_about(self.sp.error_personageid_loc))
        self.assertIn('请上传文件',self.sp.get_about(self.sp.error_personageidimage_loc))

    def test_009(self):
        '''个人用户身份证非数字'''
        self.sp.inputaction(self.sp.personage_ID_loc,"#$##5")
        self.sp.clickaction(self.sp.submit_loc)
        self.assertIn('身份证格式错误',self.sp.get_about(self.sp.error_personageid_loc))

    def test_010(self):
        '''个人身份证非18位'''
        self.sp.inputaction(self.sp.personage_ID_loc,"123")
        self.sp.clickaction(self.sp.submit_loc)
        self.assertIn('身份证格式错误',self.sp.get_about(self.sp.error_personageid_loc))

    def test_011(self):
        '''个人身份证输入非身份证'''
        self.sp.inputaction(self.sp.personage_ID_loc,"123456789012345678")
        self.sp.clickaction(self.sp.submit_loc)
        self.assertIn('身份证格式错误',self.sp.get_about(self.sp.error_personageid_loc))

    def test_012(self):
        '''个人身份证上传格式错误'''
        self.sp.find_element(self.sp.personage_imagebuton_loc).send_keys(self.file_path+r'\A_006.gif')
        sleep(0.5)
        self.assertIn('请上传jpg/jpeg/png/bmp格式图片',self.sp.get_about(self.sp.error_personageidimage_loc))

    def test_013(self):
        '''分支机构必填项为空'''
        self.sp.refresh()
        self.sp.clickaction(self.sp.branchControl1_loc)
        sleep(0.5)
        self.sp.clickaction(self.sp.submit_loc)
        self.assertIn('请输入分支机构名称',self.sp.get_about(self.sp.error_branchname_loc))
        self.assertIn('请选择所属区域',self.sp.get_about(self.sp.error_brancharea_loc))
        self.assertIn('输入分支机构地址',self.sp.get_about(self.sp.error_branchadd_loc))
        self.assertIn('请输入联系人姓名',self.sp.get_about(self.sp.error_branchusname_loc))
        self.assertIn('请输入手机号',self.sp.get_about(self.sp.error_branchphone_loc))
        self.assertIn('请输入联系邮箱',self.sp.get_about(self.sp.error_branchemail_loc))

    def test_014(self):
        '''分支机构邮编长度或类型错误'''
        self.sp.inputaction(self.sp.branchpscode_loc,'11')
        self.sp.clickaction(self.sp.submit_loc)
        self.assertIn("政编码格式错误",self.sp.get_about(self.sp.error_branchzip_loc))
        self.sp.inputaction(self.sp.branchpscode_loc,'$%^')
        self.sp.clickaction(self.sp.submit_loc)
        self.assertIn("政编码格式错误",self.sp.get_about(self.sp.error_branchzip_loc))

    def test_015(self):
        '''分支机构-网址错误'''
        self.sp.inputaction(self.sp.branchwebsite_loc,'11')
        self.sp.clickaction(self.sp.submit_loc)
        self.assertIn("输入合法的网址",self.sp.get_about(self.sp.error_branchwebsite_loc))

    def test_016(self):
        '''分支机构联系邮箱格式错误'''
        self.sp.inputaction(self.sp.branchemail_loc,'liuhongliang01@')
        self.sp.clickaction(self.sp.submit_loc)
        self.assertIn("输入正确的邮箱",self.sp.get_about(self.sp.error_branchemail_loc))

    def test_017(self):
        '''添加多个分支机构功能正常'''
        self.assertFalse(self.sp.is_visibility(self.sp.branchdelbutton_loc))
        self.sp.clickaction(self.sp.branchbutton_loc)
        sleep(0.5)
        self.assertTrue(self.sp.is_visibility(self.sp.branchname1_loc))


    def test_018(self):
        '''必填项-联系人长度26字符-自动截取'''
        self.sp.refresh()
        self.sp.reg_lineEdit(self.sp.orgWebsite_loc,'http://www.baidu.com')
        self.sp.reg_lineEdit(self.sp.linkman_loc,getChar('shi', 26))
        sleep(0.5)
        self.assertEqual(lenJudge(self.sp, self.sp.linkman_loc, 25), True)

    def test_019(self):
        '''必填项-联系人电话-手机号长度12位-自动截取'''
        self.sp.reg_lineEdit(self.sp.mobile_loc,getChar('131', 12))
        sleep(0.5)
        self.assertEqual(lenJudge(self.sp, self.sp.mobile_loc, 11), True)
        
    def test_020(self):
        '''必填项-联系人电话-手机号含非数字-注册失败'''
        self.sp.reg_lineEdit(self.sp.mobile_loc,getChar('1aa1', 11))
        self.sp.reg_submit()
        sleep(0.5)
        self.assertEqual(self.sp.error_hint(self.sp.error_mobile_loc), '手机号码格式错误')
        
    def test_021(self):
        '''职位长度26位-自动截取'''
        self.sp.reg_lineEdit(self.sp.mobile_loc,getChar('131', 11))
        self.sp.reg_lineEdit(self.sp.linkmanPosition_loc,getChar('131', 26))
        sleep(0.5)
        self.assertEqual(lenJudge(self.sp, self.sp.linkmanPosition_loc, 25), True)
        
    def test_022(self):
        '''必填项-电子邮箱格式错误-注册失败'''
        self.sp.reg_lineEdit(self.sp.linkmanPosition_loc,'总监')
        self.sp.reg_lineEdit(self.sp.linkmanEmail_loc,'12@@12.com')
        self.sp.reg_submit()
        sleep(0.5)
        self.assertEqual(self.sp.error_hint(self.sp.error_linkmanEmail_loc), '请输入正确的邮箱')
        
    def test_023(self):
        '''邮编输入非数字--注册失败'''
        self.sp.reg_lineEdit(self.sp.linkmanEmail_loc,'12@12.com')
        self.sp.reg_lineEdit(self.sp.linkmanZip_loc,'12@as1')
        self.sp.reg_submit()
        sleep(0.5)
        self.assertEqual(self.sp.error_hint(self.sp.error_linkmanZip_loc), '邮政编码格式错误')
        
    def test_024(self):
        '''邮编输入5位数字--注册失败'''
        self.sp.reg_lineEdit(self.sp.linkmanZip_loc,getChar('131', 5))
        self.sp.reg_submit()
        sleep(0.5)
        self.assertEqual(self.sp.error_hint(self.sp.error_linkmanZip_loc), '邮政编码格式错误')
        
    def test_025(self):
        '''邮编输入7位数字-自动截取'''
        self.sp.reg_lineEdit(self.sp.linkmanZip_loc,getChar('131', 7))
        sleep(0.5)
        self.assertEqual(lenJudge(self.sp, self.sp.linkmanZip_loc, 6), True)
        
    def test_026(self):
        '''必填项-用户名格式错误-注册失败'''
        self.sp.reg_lineEdit(self.sp.linkmanZip_loc,getChar('131', 6))
        self.sp.reg_lineEdit(self.sp.email_loc,'12@@12.com')
        self.sp.reg_submit()
        sleep(0.5)
        self.assertEqual(self.sp.error_hint(self.sp.error_email_loc), '请输入正确的邮箱')
        
    def test_027(self):
        '''必填项-邮箱验证码格式错误-注册失败'''
        self.sp.reg_lineEdit(self.sp.email_loc,'xitest090@163.com')
        time.sleep(0.5)
        self.sp.reg_lineEdit(self.sp.emailValidateCode_loc,'123')
        self.sp.reg_submit()
        sleep(0.5)
        self.assertEqual(self.sp.error_hint(self.sp.error_emailValidateCode_loc), '验证码格式错误')

    def test_028(self):
        '''用户名已注册'''
        self.sp.reg_lineEdit(self.sp.email_loc,'xitest013@163.com')
        self.sp.clickaction(self.sp.send_email_btn_loc)
        sleep(0.5)
        self.assertEqual(self.sp.error_hint(self.sp.error_email_loc), '该邮箱已注册')

    def test_029(self):
        '''用户名已提交申请，待审核'''
        self.sp.reg_lineEdit(self.sp.email_loc,'13@qq.com')
        self.sp.clickaction(self.sp.send_email_btn_loc)
        sleep(0.5)
        self.assertEqual(self.sp.error_hint(self.sp.error_email_loc), '该邮箱已提交申请')

    def test_030(self):
        '''必填项-机构LOGO格式错误-注册失败'''
        self.sp.find_element(self.sp.logo_btn_loc).send_keys(self.file_path+r'\A_006.gif')
        sleep(1)
        self.assertEqual(self.sp.error_hint(self.sp.error_logoText_loc), '请上传jpg/jpeg/png/bmp格式图片')

    def test_031(self):
        '''必填项-机构扫描件格式错误-注册失败'''
        self.sp.find_element(self.sp.scanCodeFile_loc).send_keys(self.file_path+r'\A_006.gif')
        sleep(1)
        self.assertEqual(self.sp.error_hint(self.sp.error_scanCodeText_loc), '请上传jpg/jpeg/png/bmp格式图片')

    def test_032(self):
        '''机构用户正常填写注册信息'''
        self.sp.select_by_value(self.sp.areaId_loc,'1')
        self.sp.inputaction(self.sp.orgName_loc,"自动化测试用组织")
        self.sp.find_element(self.sp.logo_btn_loc).send_keys(self.file_path+r'\A_016.jpg')
        sleep(0.5)
        self.sp.inputaction(self.sp.orgAddress_loc,"深圳")
        self.sp.inputaction(self.sp.idNumber_loc,"123456789012345")
        self.sp.find_element(self.sp.scanCodeFile_loc).send_keys(self.file_path+r'\A_016.jpg')
        sleep(0.5)
        self.sp.inputaction(self.sp.orgWebsite_loc,"www.baidu.com")
        self.sp.inputaction(self.sp.linkman_loc,"测试-刘红亮")
        self.sp.inputaction(self.sp.mobile_loc,"13125485241")
        self.sp.inputaction(self.sp.linkmanPosition_loc,"测试数据")
        self.sp.inputaction(self.sp.linkmanEmail_loc,"12345678@163.com")
        self.sp.inputaction(self.sp.linkmanContact_loc,"深圳")
        self.sp.inputaction(self.sp.linkmanZip_loc,"518000")
        time.sleep(0.5)
        self.sp.inputaction(self.sp.email_loc,r"beta_mpr@163.com")
        self.sp.clickaction(self.sp.send_email_btn_loc)
        sleep(0.5)
        self.assertTrue(self.sp.is_visibility(self.sp.error_emailValidateCode_loc))
        self.sp.inputaction(self.sp.emailValidateCode_loc,'1234')
        self.sp.clickaction(self.sp.submit_loc)
        sleep(0.5)
        self.assertIn("验证码错误",self.sp.get_about(self.sp.error_emailcode_loc))

    def test_033(self):
        '''个人用户正常注册'''
        self.sp.refresh()
        self.sp.select_by_value(self.sp.areaId_loc,'1')
        self.sp.clickaction(self.sp.orgTypeId2_loc)
        self.sp.inputaction(self.sp.personage_name_loc,'测试数据-H')
        self.sp.inputaction(self.sp.personage_add_loc,'深圳')
        self.sp.inputaction(self.sp.personage_ID_loc,'362421199307193811')
        self.sp.find_element(self.sp.personage_imagebuton_loc).send_keys(self.file_path+r'\A_016.jpg')
        sleep(0.5)
        self.sp.inputaction(self.sp.linkman_loc,"测试-刘红亮")
        self.sp.inputaction(self.sp.mobile_loc,"13125485241")
        self.sp.inputaction(self.sp.linkmanPosition_loc,"测试数据")
        self.sp.inputaction(self.sp.linkmanEmail_loc,"12345678@163.com")
        self.sp.inputaction(self.sp.linkmanContact_loc,"深圳")
        self.sp.inputaction(self.sp.linkmanZip_loc,"518000")
        self.sp.inputaction(self.sp.email_loc,r"beta_mpr@163.com")
        self.sp.clickaction(self.sp.send_email_btn_loc)
        sleep(0.5)
        self.assertTrue(self.sp.is_visibility(self.sp.error_emailValidateTip_loc))
        self.sp.inputaction(self.sp.emailValidateCode_loc,'1234')
        self.sp.clickaction(self.sp.submit_loc)
        sleep(1)
        self.assertIn("验证码错误",self.sp.get_about(self.sp.error_emailcode_loc))



    def test_034(self):
        '''机构用户添加分支机构'''
        self.sp.refresh()
        self.sp.select_by_value(self.sp.areaId_loc,'1')
        self.sp.inputaction(self.sp.orgName_loc,"自动化测试用组织")
        self.sp.find_element(self.sp.logo_btn_loc).send_keys(self.file_path+r'\A_016.jpg')
        sleep(0.5)
        self.sp.inputaction(self.sp.orgAddress_loc,"深圳")
        self.sp.inputaction(self.sp.idNumber_loc,"123456789012345")
        self.sp.find_element(self.sp.scanCodeFile_loc).send_keys(self.file_path+r'\A_016.jpg')
        sleep(0.5)
        self.sp.inputaction(self.sp.orgWebsite_loc,"www.baidu.com")
        self.sp.clickaction(self.sp.branchControl1_loc)
        sleep(0.5)
        #分支机构信息
        self.sp.inputaction(self.sp.branchname_loc,"测试分支机构")
        self.sp.select_by_value(self.sp.branchareaId_loc,'1')
        self.sp.inputaction(self.sp.branchaddress_loc,"分支-深圳")
        self.sp.inputaction(self.sp.branchpscode_loc,"518000")
        self.sp.inputaction(self.sp.branchwebsite_loc,"www.baidu.com")
        self.sp.inputaction(self.sp.branchusername_loc,"测试-HLLiu")
        sleep(0.5)
        self.sp.inputaction(self.sp.branchpost_loc,"测试")
        self.sp.inputaction(self.sp.branchphone_2_loc,"15180106199")
        self.sp.inputaction(self.sp.branchemail_loc,"123456789@163.com")

        self.sp.inputaction(self.sp.linkman_loc,"测试-刘红亮")
        self.sp.inputaction(self.sp.mobile_loc,"13125485241")
        self.sp.inputaction(self.sp.linkmanPosition_loc,"测试数据")
        self.sp.inputaction(self.sp.linkmanEmail_loc,"12345678@163.com")
        self.sp.inputaction(self.sp.linkmanContact_loc,"深圳")
        self.sp.inputaction(self.sp.linkmanZip_loc,"518000")
        self.sp.inputaction(self.sp.email_loc,r"beta_mpr@163.com")
        self.sp.clickaction(self.sp.send_email_btn_loc)
        sleep(0.5)
        self.assertTrue(self.sp.is_visibility(self.sp.error_emailValidateTip_loc))
        self.sp.inputaction(self.sp.emailValidateCode_loc,'1234')
        self.sp.clickaction(self.sp.submit_loc)
        sleep(0.5)
        self.assertIn("验证码错误",self.sp.get_about(self.sp.error_emailcode_loc))




if __name__=="__main__":
    unittest.main()