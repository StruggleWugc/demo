import sys,time
# sys.path.append("..")
from selenium.webdriver.support.ui import Select
from page.base import Page
from common import base
from time import sleep
# import win32com
# from win32 import test_win32gui,test_win32con
# from win32.lib import win32con,win32gui_struct
from common.function import isElementExist

class registerModular(base.BasePage):
    ##基本信息
    url = r'http://172.16.3.53:8080/isli/irms/workbench-provider/base/provider/toRegiste?loginUrl=http://172.16.3.52:8080/irap/web/navigation/toLogin'
    # registerTypeId_loc = ('name', 'registerTypeId')                                               #注册用户类型
    language_loc = ('css selector','[onchange="switchLanguage(this)"]')                                      #语种
    areaId_loc = ("css selector", '.select[name="areaId"]')                                       #所属区域
    orgTypeId1_loc = ("css selector", '#orgType_1')                                               #用户性质-机构
    orgTypeId2_loc = ("css selector", '#orgType_2')                                               #用户性质-个人
    orgName_loc = ("css selector", '[name="orgName"]')                                            #机构名称
    logo_loc = ("css selector", '#swfLogo>p')                                                     #机构logo显示框
    logo_btn_loc = ("css selector", '#logo_file')                                                 #机构log上传btn
    orgAddress_loc = ('css selector', '[name="orgAddress"]')                                      #注册地址
    idNumber_loc = ('name', 'idNumber')                                                           #组织机构代码证号
    scanCode_loc = ("css selector", '#swf_scanCode>p')                                            #组织结构代码扫描件输入框
    scanCodeFile_loc = ("css selector", '#scan_code_file')                                        #组织机构扫描件上传btn
    scanCodeFileImg_loc = ('id', 'scan_code_file_img')                                            #组织机构代码扫描件示例btn
    orgWebsite_loc = ('name', 'orgWebsite')                                                       #官网
    branchControl1_loc = ('css selector', '[value="Y"]')                                          #分支机构-有
    branchControl2_loc = ('css selector', '[value="N"]')                                          #分支机构-无

    #用户性质个人
    personage_name_loc=('css selector','[name="per_name"]')                                       #个人姓名
    personage_add_loc = ('css selector','[name="per_address"]')                                   #个人地址
    personage_ID_loc =('css selector','[name="per_idNumber"]')                                    #个人ID
    personage_image_loc = ('css selector','#per_id_scanCode>p')                                   #个人image
    personage_imagebuton_loc = ('css selector','#per_id_scanCode_file')                           #个人button


    #分支机构
    branchname_loc = ('css selector','[dataname="branchName"]')                                 #分支机构名称
    branchareaId_loc =('css selector','[dataname="b_areaId"]')                                  #分支机构区域
    branchaddress_loc = ('css selector','[name="branchAddr"]')                                 #分支机构地址
    branchpscode_loc =('css selector','[name="branchZip"]')                                    #分支机构邮编
    branchwebsite_loc = ('css selector','[name="branchMainSite"]')                             #分支机构网址
    branchusername_loc = ('css selector','[name="branchLinkman"]')                             #分支机构联系人
    branchpost_loc =('css selector','[name="branchPosition"]')                                 #分支机构联系人职位
    branchTel_1_loc = ('css selector','[name="branchTelType"]')                                 #分支机构固话国际区号
    branchTel_2_loc = ('css selector','[name="branchTelArea"]')                                #分支机构固话区号
    branchTel_3_loc = ('css selector','[name="branchPhone"]')                                  #分支机构固话号码
    branchTel_4_loc = ('css selector','[name="branchTelExt"]')                                 #分支机构固话分机号
    branchphone_1_loc = ('css selector','[name="branchMobileType"]')                            #分支机构手机区号
    branchphone_2_loc = ('css selector','[name="branchTelNumber"]')                            #分支机构手机号
    branchemail_loc = ('css selector','[name="branchEmail"]')                                   #分支机构邮箱
    branchbutton_loc = ('css selector','#addBranchBtn')                                         #继续添加分支按钮
    branchdelbutton_loc = ('css selector','#type_org>div:first-child>.active')                  #删除分支机构地按钮
    branchname1_loc = ('css selector','[name="branchName1"]')

    ##联系人信息
    linkman_loc = ('name', 'linkman')                                                            #联系人
    phoneType_loc = ('id', 'phoneType')                                                          #固话-国际区号
    phoneArea_loc = ('name', 'phoneArea')                                                        #固话-区号
    phone_loc = ('name', 'phone')                                                                #固话-号码
    phoneExt_loc = ('name', 'phoneExt')                                                          #固话-分机号
    mobileType_loc = ('id', 'mobileType')                                                        #手机国际区号
    mobile_loc = ('name', 'mobile')                                                              #手机号
    linkmanPosition_loc = ('name', 'linkmanPosition')                                            #职位
    linkmanEmail_loc = ('name', 'linkmanEmail')                                                  #联系邮箱
    linkmanContact_loc = ('name', 'linkmanContact')                                              #地址
    linkmanZip_loc = ('name', 'linkmanZip')                                                      #邮编

    ##账户信息
    email_loc = ('name', 'email')                                                                          #用户名-邮箱
    send_email_btn_loc = ('id', 'send_validate_email')                                                     #发送验证码btn
    emailValidateCode_loc = ('name', 'emailValidateCode')                                                  #邮箱验证码输入框

    ##提交
    submit_loc = ('id', 'submit')                                                                          #提交btn
    reset_loc = ("css selector", '.reset')                                                                 #返回上一页btn

   ##提示语
    error_areaId_loc = ("css selector", '.error[for="areaId"]')                             #选择区域
    error_orgName_loc = ("css selector", '.error[for="orgName"]')                           #机构名称
    error_logoText_loc = ('id', 'logo_error_text')                                          #机构Logo
    error_orgAddress_loc = ("css selector", '.error[for="orgAddress"]')                     #注册机构地址
    error_idNumber_loc = ("css selector", '.error[for="idNumber"]')                         #信用代码
    error_scanCodeText_loc = ('id', 'scanCode_error_text')                                  #信用代码image
    error_orgWebsite_loc = ("css selector"," [for='orgWebsite']")                           #website
    error_linkman_loc = ("css selector", '.error[for="linkman"]')                           #联系人姓名
    error_phone_loc = ("css selector", '.error[for="phone"]')
    error_mobile_loc = ("css selector", '.error[for="mobile"]')                             #联系人手机
    error_linkmanEmail_loc = ("css selector", '.error[for="linkmanEmail"]')                 #联系人邮箱
    error_linkmanContact_loc = ("css selector", '.error[for="linkmanContact"]')             #联系人地址
    error_linkmanZip_loc = ("css selector", '.error[for="linkmanZip"]')                     #联系人邮编
    error_email_loc = ("css selector", '.error[for="email"]')                               #用户名
    error_emailValidateCode_loc = ("css selector", '.error[for="emailValidateCode"]')       #验证码
    error_emailcode_loc = ('id','email_validate_span_id')                                   #验证码错误
    error_emailValidateTip_loc = ('id', 'emailValidate_tip')                                #60s提示
    error_personagename_loc = ("css selector",'[for="per_name"]')                           #个人姓名报错
    error_personageadd_loc =("css selector",'[for="per_address"]')                          #个人地址报错
    error_personageid_loc = ("css selector",'[for="per_idNumber"]')                         #个人身份证报错
    error_personageidimage_loc=("css selector",'#per_id_error_text')                        #个人身份证图片报错
    error_branchname_loc =("css selector",'[for="branchName"]')                             #分支机构名称错误
    error_brancharea_loc = ("css selector",'[for="b_areaId"]')                              #分支机构区域错误
    error_branchadd_loc = ("css selector",'[for="branchAddr"]')                             #分支机构地址错误
    error_branchzip_loc = ("css selector",'[for="branchZip"]')                              #分支机构邮编错误
    error_branchwebsite_loc = ("css selector",'[for="branchMainSite"]')                     #分支机构网址错误
    error_branchusname_loc = ("css selector",'[for="branchLinkman"]')                       #分支机构联系人错误
    error_branchphone_loc = ("css selector",'[for="branchTelNumber"]')                      #分支机构手机错误
    error_branchemail_loc = ("css selector",'[for="branchEmail"]')                          #分支机构邮箱错误

    def select_language(self):
        self.select_by_value(self.language_loc,'ZH_CN')
        time.sleep(1)


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

    def reg_lineEdit(self, element_loc, name):
        self.find_element(element_loc).click()
        self.find_element(element_loc).clear()
        self.find_element(element_loc).send_keys(name)
    
    def reg_comboBox(self, element_loc, index):
        '''选择某下拉选项，并返回其值'''
        select = Select(self.find_element(*element_loc))
        select.select_by_index(index)
        selected = select.all_selected_options
        return selected[0].text
    
    def reg_button(self, element_loc):
        self.find_element(element_loc).click()
        
    #n为1或者2
    def reg_orgTypeId(self, n):
        '''选择用户性质  1--机构   2--个人'''
        if n==1:
            self.find_element(self.orgTypeId1_loc).click()
        else:
            self.find_element(self.orgTypeId2_loc).click()
            
    def reg_waitForCode(self):
        '''等待输入验证码'''
        code = self.find_element(self.emailValidateCode_loc)
        while not (code.get_attribute('value')):
            sleep(5)

    #python 3.4无对应版本
    '''
    def reg_uploadFile(self, element_loc, path):
        self.find_element(*element_loc).click()
        sleep(1)
        dialog = win32gui.FindWindow('#32770','文件上传')  #对话框
        ComboBoxEx32 = win32gui_struct.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui_struct.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui_struct.FindWindowEx(ComboBox, 0, 'Edit', None)
        button = win32gui_struct.FindWindowEx(dialog, 0, 'Button', None)
        sleep(1)
        win32gui_struct.SendMessage(Edit, win32con.WM_SETTEXT, None, path)  #往输入框输入文件的绝对地址
        win32gui_struct.SendMessage(dialog, win32con.WM_COMMAND, 1, button) #按下button按钮
        sleep(1)

    '''

    def reg_submit(self):
        self.find_element(self.submit_loc).click()

    ##提示语
    def error_hint(self, error_loc):
        '''获取错误提示'''
        if isElementExist(self.driver, error_loc):
            return self.find_element(error_loc).text
        else:
            return 'NonElement'
    


if __name__ =="__main__":
    pass