from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium import  webdriver

class Page(object):
    index_url = 'http://172.16.3.52:8080'


    def __init__(self):
        # self.base_url = base_url
        # self.driver = selenium_driver
        # self.timeout = 20
        # self.parent = parent
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
    # def _open(self,url):
    #     url = self.base_url + url
    #     try:
    #         self.driver.get(url)
    #     except:
    #         pass
    #     assert self.on_page(),'Did not land on %s'%url
        
    def open(self, url, t='', timeout=10):
        '''
        使用get打开url后，最大化窗口，判断title符合预期
        '''
        self.driver.get(url)
        self.driver.maximize_window()
        try:
            WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(t))
        except TimeoutError as msg:
            print("open %s title error" % url)
        except Exception as msg:
            print("Error:%s" % msg)


    # def on_page(self):
    #     #返回1为失败，返回0为成功 判断打开网址
    #     return self.driver.current_url == (self.base_url+self.url)

    def find_element(self,loc,timeout=10):
        #查找元素
        element = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(loc))
        return element
        # return self.driver.find_element(*loc)


    def find_elements(self,loc):
        #元素组
        return self.driver.find_elements(loc)

    def send_keys(self,loc,text):
        element = self.driver.find_element(loc)
        return element.send_keys(text)

    def script(self,src):
        #界面左右移动 js
        return self.driver.execute_script(src)

    def iframe(self,iframe):
        #切换iframe
        return self.driver.switch_to_frame(iframe)
    
    def parent_frame(self):
        #iframe
        return self.driver.switch_to.parent_frame()
        
    def refresh(self):
        #刷新
        self.driver.refresh()
    
    def switch_to_alert(self):
        #弹窗
        return self.driver.switch_to_alert()
        
    def perform(self, loc):
        #鼠标悬停
        element = self.find_element(*loc)
        ActionChains(self.driver).move_to_element(element).perform()
        sleep(1)

    def quit(self):
        self.driver.quit()
        
    # def enter_keys(self, *loc, keys):
    #     #键盘
    #     if keys=='tab':
    #         return self.driver.find_element(*loc).send_keys(Keys.TAB)
    #     elif keys=='enter':
    #         return self.driver.find_element(*loc).send_keys(Keys.ENTER)
    #     elif keys=='ctrl+a':
    #         return self.driver.find_element(*loc).send_keys(Keys.CONTROL, 'a')
    #     elif keys=='ctrl+x':
    #         return self.driver.find_element(*loc).send_keys(Keys.CONTROL, 'x')
    #     elif keys=='ctrl+c':
    #         return self.driver.find_element(*loc).send_keys(Keys.CONTROL, 'c')
    #     elif keys=='ctrl+v':
    #         return self.driver.find_element(*loc).send_keys(Keys.CONTROL, 'v')

class web_homePage():
    """官网首页"""

    url=r'/irap/web/navigation/toNavigationPage/1'
    
    ##顶部菜单栏
    home_loc = (By.CSS_SELECTOR, '.lifirst [navid="1"]')                #首页
    about_loc = (By.CSS_SELECTOR, '.lifirst [navid="2"]')               #关于isli
    application_loc = (By.CSS_SELECTOR, '.lifirst [navid="3"]')         #资源中心
    source_loc = (By.CSS_SELECTOR, '.lifirst [navid="4"]')              #应用isli
    message_loc = (By.CSS_SELECTOR, '.lifirst [navid="5"]')             #动态信息
    
    ##底部按钮栏
    feedback_loc = (By.CSS_SELECTOR, '.linkmap>a:nth-child(3)')         #客户反馈入口
    
    ##客户反馈界面

    fdk_title_loc = (By.CSS_SELECTOR, '#_title')            #主题
    fdk_name_loc = (By.CSS_SELECTOR, '#_userName')          #姓名
    fdk_email_loc = (By.CSS_SELECTOR, '#userEmail')         #常用邮箱
    fdk_type_loc = (By.CSS_SELECTOR, '#_feedbackTypeId')    #类型
    fdk_mobile_loc = (By.CSS_SELECTOR, '#_userMobile')      #联系手机
    fdk_addfile_loc = (By.CSS_SELECTOR, '.addfile')         #上传文件
    fdk_content_loc = (By.CSS_SELECTOR, '#_feedbackContent')        #内容
    fdk_submit_loc = (By.CSS_SELECTOR, '.submit')             #提交
    
    #弹窗
    fdk_submit_ok_loc = (By.CSS_SELECTOR, '.submit.e-close')            #提交后确认弹窗
    
class web_loginPage():
    '''官网登入'''
    ##调用open函数时，会自动读取该条URL，接到baseURL后面
    url=r'/irap/web/navigation/toLogin'
    
    username_loc = (By.CSS_SELECTOR,'#username')
    password_loc = (By.CSS_SELECTOR,'#password')
    codecon_loc = (By.CSS_SELECTOR,'#vcode')            #验证码
    refreshCode_loc = (By.CSS_SELECTOR, '#image[onclick="refreshCode();"]')             #刷新验证码
    login_btn_loc = (By.CLASS_NAME,'btn')

    ##请输入您的用户名/邮箱/ID
    ##帐号不存在
    ##请输入密码
    ##密码错误
    ##请输入4位验证码
    ##验证码不正确
    error_hint_loc = (By.CSS_SELECTOR,'#error')             #登入错误提示
    login_success_loc = (By.CSS_SELECTOR, '')
    
class web_registerPage():
    '''注册服务提供商'''

    url = r'/isli/irms/workbench-provider/base/provider/toRegiste?loginUrl=http://172.16.3.52:8080/irap/web/navigation/toLogin'

    ##基本信息
    registerTypeId_loc = (By.NAME, 'registerTypeId')                                                        #注册用户类型
    areaId_loc = (By.CSS_SELECTOR, '.select[name="areaId"]')                                                #所属区域
    orgTypeId1_loc = (By.CSS_SELECTOR, '#orgType_1')                                                        #用户性质-机构
    orgTypeId2_loc = (By.CSS_SELECTOR, '#orgType_2')                                                        #用户性质-个人
    orgName_loc = (By.CSS_SELECTOR, '#type_org>dl>dd>input')                                                #机构名称
    logo_loc = (By.CSS_SELECTOR, '#swfLogo>p')                                                              #机构logo显示框
    logo_btn_loc = (By.CSS_SELECTOR, '#logo_file')                                                          #机构log上传btn
    orgAddress_loc = (By.XPATH, ".//*[@id='type_org']/dl[3]/dd/input")                                      #注册地址
    idNumber_loc = (By.NAME, 'idNumber')                                                                    #组织机构代码证号
    scanCode_loc = (By.CSS_SELECTOR, '#swf_scanCode>p')                                                     #组织结构代码扫描件输入框
    scanCodeFile_loc = (By.CSS_SELECTOR, '#scan_code_file')                                                 #组织机构扫描件上传btn
    scanCodeFileImg_loc = (By.ID, 'scan_code_file_img')                                                     #组织机构代码扫描件示例btn
    orgWebsite_loc = (By.NAME, 'orgWebsite')                                                                #官网
    branchControl1_loc = (By.ID, 'spregister.page.regbox.yes')                                              #分支机构-有
    branchControl2_loc = (By.ID, 'spregister.page.regbox.no')                                               #分支机构-无
    
    ##联系人信息
    linkman_loc = (By.NAME, 'linkman')                                                                      #联系人
    phoneType_loc = (By.ID, 'phoneType')                                                                    #固话-国际区号
    phoneArea_loc = (By.NAME, 'phoneArea')                                                                  #固话-区号
    phone_loc = (By.NAME, 'phone')                                                                          #固话-号码
    phoneExt_loc = (By.NAME, 'phoneExt')                                                                    #固话-分机号
    mobileType_loc = (By.ID, 'mobileType')                                                                  #手机国际区号
    mobile_loc = (By.NAME, 'mobile')                                                                        #手机号
    linkmanPosition_loc = (By.NAME, 'linkmanPosition')                                                      #职位
    linkmanEmail_loc = (By.NAME, 'linkmanEmail')                                                            #联系邮箱
    linkmanContact_loc = (By.NAME, 'linkmanContact')                                                        #地址
    linkmanZip_loc = (By.NAME, 'linkmanZip')                                                                #邮编
    
    ##拟申请关联服务（SC编码）信息
    serviceName_loc = (By.NAME, 'serviceName')                                                              #服务
    p_file_text_loc = (By.XPATH, ".//*[@id='p_swfPlan']/p")                                                 #实施计划输入框
    p_file_btn_loc = (By.XPATH, ".//*[@id='p_file']")                                                       #实施计划上传btn
    p_download_loc = (By.XPATH, ".//*[@id='p_swfPlan']/input[4]")                                           #实施计划下载btn
    s_file_text_loc = (By.XPATH, ".//*[@id='s_swfPlan']/p")                                                 #服务说明输入框
    s_file_btn_loc = (By.XPATH, ".//*[@id='s_file']")                                                       #服务说明上传btn
    s_download_loc = (By.XPATH, ".//*[@id='s_swfPlan']/input[4]")                                           #服务说明下载btn
    
    
    ##账户信息
    email_loc = (By.NAME, 'email')                                                                          #用户名-邮箱
    send_email_btn_loc = (By.ID, 'send_validate_email')                                                     #发送验证码btn
    emailValidateCode_loc = (By.NAME, 'emailValidateCode')                                                  #邮箱验证码输入框
    
    ##提交
    submit_loc = (By.ID, 'submit')                                                                          #提交btn
    reset_loc = (By.CLASS_NAME, 'reset')                                                                    #返回上一页btn
    
   ##提示语
    error_registerTypeId_loc = (By.CSS_SELECTOR, '.error[for="registerTypeId"]')
    error_areaId_loc = (By.CSS_SELECTOR, '.error[for="areaId"]')
    error_orgName_loc = (By.CSS_SELECTOR, '.error[for="orgName"]')
    error_logoText_loc = (By.ID, 'logo_error_text')
    error_orgAddress_loc = (By.CSS_SELECTOR, '.error[for="orgAddress"]')
    error_idNumber_loc = (By.CSS_SELECTOR, '.error[for="idNumber"]')
    error_scanCodeText_loc = (By.ID, 'scanCode_error_text')
    error_orgWebsite_loc = (By.CSS_SELECTOR," [for='orgWebsite']")
    error_linkman_loc = (By.CSS_SELECTOR, '.error[for="linkman"]')
    error_phone_loc = (By.CSS_SELECTOR, '.error[for="phone"]')
    error_mobile_loc = (By.CSS_SELECTOR, '.error[for="mobile"]')
    error_linkmanEmail_loc = (By.CSS_SELECTOR, '.error[for="linkmanEmail"]')
    error_linkmanContact_loc = (By.CSS_SELECTOR, '.error[for="linkmanContact"]')
    error_linkmanZip_loc = (By.CSS_SELECTOR, '.error[for="linkmanZip"]')
    error_serviceName_loc = (By.CSS_SELECTOR, '.error[for="serviceName"]')
    error_pText_loc = (By.ID, 'p_error_text')
    error_sText_loc = (By.ID, 's_error_text')
    error_email_loc = (By.CSS_SELECTOR, '.error[for="email"]')
    error_emailValidateCode_loc = (By.CSS_SELECTOR, '.error[for="emailValidateCode"]')
    error_emailValidateTip_loc = (By.ID, 'emailValidate_tip') #60s提示


class m_loginPae():
    '''后台管理系统登入'''
    url = '/isli/irms/manage-manager/base/login'
    
    username_loc = (By.CSS_SELECTOR, '#username')                                       #用户名
    password_loc = (By.CSS_SELECTOR, '#password')                                       #密码
    validcode_loc = (By.CSS_SELECTOR, '#validCode')                                     #验证码
    submit_loc = (By.CSS_SELECTOR, '.login>input')                                      #登入
    
class m_webManagerPage():
    '''后台管理-网站管理'''
    url = '/isli/irms/manage-website/base/news/index'
    
    ##左侧菜单栏
    left_newsManager_loc = (By.CSS_SELECTOR, '#left_newsManager>a')                    #新闻管理
    left_navigationsManager_loc = (By.CSS_SELECTOR, '#left_navigationsManager>a')      #栏目管理
    left_contentManager_loc = (By.CSS_SELECTOR, '#left_contentManager>a')              #内容管理
    left_pictureManager_loc = (By.CSS_SELECTOR, '#left_pictureManager>a')              #图片管理
    left_websiteInformation_loc = (By.CSS_SELECTOR, '#left_websiteInformation>a')      #网站信息管理
    left_feedback_loc = (By.CSS_SELECTOR, '#left_feedback>a')                          #客户反馈管理
    
    ##新闻管理-搜索栏
    addNewsPage_loc = (By.CSS_SELECTOR, '.listBar>a')                                   #发布新闻
    search_startTime_loc = (By.CSS_SELECTOR, '#startTime')                              #发布时间-开始
    search_endTime_loc = (By.CSS_SELECTOR, '#endTime')                                  #发布时间-结束
    search_newsTitle_loc = (By.NAME, "newsTitle")                                       #新闻标题
    search_langCode_loc = (By.NAME, "langCode")                                         #语种
    search_submit_loc = (By.CSS_SELECTOR, '.searchButton')                              #搜索btn

    #客户反馈管理
    search_fdk_theme_loc = (By.NAME, 'title')                                           #主题
    search_fdk_status_loc = (By.NAME, 'feedbackStatus')                                 #状态
    search_fdk_type_loc = (By.NAME, 'feedbackTypeId')                                   #类型
    
    ##底部换页栏
    page_loc = (By.CSS_SELECTOR, '.pageBox>a')                                         #所有页码按钮
    selectedPage_loc = (By.CSS_SELECTOR, '.pageBox>a.selected')                        #页码一
    allPage_loc = (By.CSS_SELECTOR, '.pageBox>span>b:nth-child(2)')                    #总页码数
    toPageNo_loc = (By.CSS_SELECTOR, '#toPageNo')                                      #页码输入框
    
    ##列表
    table_list_loc = '.tableList>tbody'                                                 #数据列表
    table_trn_loc = '.tableList>tbody>tr:nth-child(1)'                                  #第一组数据
    #检查是否有数据。.text=1或者.text=暂无数据
    table_checkDataExist_loc = (By.CSS_SELECTOR, '.tableList>tbody>tr:nth-child(1)>td:nth-child(1)') #列表序列号
    
    def table_trn_loc_set(self):
        self.table_trn_title_loc = (By.CSS_SELECTOR, self.table_trn_loc+'>td:nth-child(2)')                 #列表新闻标题
        self.table_trn_navi_loc = (By.CSS_SELECTOR, self.table_trn_loc+'>td:nth-child(3)')                  #列表所属栏目
        self.table_trn_lang_loc = (By.CSS_SELECTOR, self.table_trn_loc+'>td:nth-child(4)')                  #列表语种
        self.table_trn_priority_loc = (By.CSS_SELECTOR, self.table_trn_loc+'>td:nth-child(5)>input')        #列表排序
        self.table_trn_time_loc = (By.CSS_SELECTOR, self.table_trn_loc+'>td:nth-child(6)')                  #发布时间
        self.table_trn_status_loc = (By.CSS_SELECTOR, self.table_trn_loc+'>td:nth-child(7)')                #状态
        self.table_trn_operate_loc = self.table_trn_loc+'>td:nth-child(8)'
        self.table_trn_hide_loc = (By.CSS_SELECTOR, self.table_trn_operate_loc+'>a:nth-child(1)')           #隐藏
        self.table_trn_edit_loc = (By.CSS_SELECTOR, self.table_trn_operate_loc+'>a:nth-child(2)')           #修改
        self.table_trn_del_loc = (By.CSS_SELECTOR, self.table_trn_operate_loc+'>a:nth-child(3)')            #删除
        
        self.table_fbk_trn_them_loc = (By.CSS_SELECTOR, self.table_trn_loc+'>td:nth-child(2)')              #客户反馈列表-主题
        self.table_fbk_trn_content_loc = (By.CSS_SELECTOR, self.table_trn_loc+'>td:nth-child(3)')           #客户反馈列表-内容
        self.table_fbk_trn_type_loc = (By.CSS_SELECTOR, self.table_trn_loc+'>td:nth-child(4)')              #客户反馈列表-类型
        self.table_fbk_trn_time_loc = (By.CSS_SELECTOR, self.table_trn_loc+'>td:nth-child(5)')              #客户反馈列表-反馈时间
        self.table_fbk_trn_status_loc = (By.CSS_SELECTOR, self.table_trn_loc+'>td:nth-child(6)>span')       #客户反馈列表-状态
        self.table_fbk_trn_dispose_loc = (By.CSS_SELECTOR, self.table_trn_loc+'>td:nth-child(7)>a:nth-child(2)>img')    #客户反馈列表-处理
    
    ##新闻管理--新增新闻
    news_lang_loc = (By.ID, 'language')                                                                     #语种
    news_title_loc = (By.CSS_SELECTOR, '#title[name="title"]')                                              #标题
    news_time_loc = (By.CSS_SELECTOR, '#createDateTime')                                                    #时间
    news_navi_loc = (By.ID, 'navigationId')                                                                 #所属栏目
    news_status2_loc = (By.XPATH, ".//*[@id='lang']/dl[4]/dd/input[2]")                                     #状态-隐藏
    news_author_loc = (By.ID, 'authorName')                                                                 #来源
    news_priority_loc = (By.ID, 'priorityLevel')                                                            #排序
    news_summary_loc = (By.ID, 'newsSummary')                                                               #摘要
    news_iframe_loc = (By.CSS_SELECTOR, 'iframe#baidu_editor_0')                                            #内容iframe
    news_content_loc = (By.CSS_SELECTOR, '.view>body')                                                      #内容
    news_submit_loc = (By.CSS_SELECTOR, '#submit')                                                          #提交
    
    #新增新闻--报错信息
    error_news_lang_loc = (By.CSS_SELECTOR, '.error[for="language"]')                                       #语种错误提示信息
    error_news_title_loc = (By.CSS_SELECTOR, '.error[for="title"]')                                         #标题错误提示信息
    error_news_time_loc = (By.CSS_SELECTOR, '.error[for="createDateTime"]')                                 #时间错误提示信息
    error_news_navi_loc = (By.CSS_SELECTOR, '.error[for="navigationId"]')                                   #所属栏目错误提示
    error_news_author_loc = (By.CSS_SELECTOR, '.error[for="authorName"]')                                   #来源错误提示
    error_news_priority_loc = (By.CSS_SELECTOR, '.error[for="priorityLevel"]')                              #排序错误提示
    error_news_summary_loc = (By.CSS_SELECTOR, '.error[for="newsSummary"]')                                 #摘要错误提示
    error_news_content_loc = (By.ID, 'edui1_elementpath')                                                   #内容错误提示
    hint_news_content_loc = (By.ID, 'edui1_wordcount')                                                      #内容字数显示

    ##栏目管理
    navi_iframe_loc = (By.CSS_SELECTOR, 'iframe#mainFrame')                                                 #设置弹窗
    navi_menuType_loc = (By.ID, 'menuType_')                                                                #导航类型
    navi_navNameCN_loc = (By.ID, 'navName_ZH_CN')                                                           #导航名称中文
    navi_navDescCN_loc = (By.ID, 'navDesc_ZH_CN')                                                           #导航描述中文
    navi_navNameUS_loc = (By.ID, 'navName_EN_US')                                                           #导航名称英文
    navi_navDescUS_loc = (By.ID, 'navDesc_EN_US')                                                           #导航描述英文
    navi_navNameTW_loc = (By.ID, 'navName_ZH_TW')                                                           #导航名称-中文繁体
    navi_navDescTW_loc = (By.ID, 'navDesc_ZH_TW')                                                           #导航描述-中文繁体
    navi_submit_loc = (By.ID, 'submit')                                                                     #提交按钮
    navi_reset_loc = (By.CSS_SELECTOR, '.mt15 >input.reset')                                                #取消btn
    
    #报错提示
    error_navi_navNameCN_loc = (By.CSS_SELECTOR, '.error[for="navName_ZH_CN"]')                             #导航名称-中文错误提示
    error_navi_navNameUS_loc = (By.CSS_SELECTOR, '.error[for="navName_EN_US"]')                             #导航名称-英文错误提示
    error_navi_navNameTW_loc = (By.CSS_SELECTOR, '.error[for="navName_ZH_TW"]')                             #导航名称-中文繁体错误提示
    
    #删除提示弹窗
    navi_submitNon_loc = (By.CSS_SELECTOR, '.submitNon')                                                    #删除确认btn
    del_navi_reset_loc = (By.CSS_SELECTOR, '.centerButton>input.reset')                                     #删除取消btn

    ##反馈管理
    ##弹窗
    fbk_dealOpinion_loc = (By.ID, 'dealOpinion')                                                            #处理结果
    fbk_dealError_loc = (By.ID, 'dealError')                                                                #处理错误提示
    fbk_dealSubmit_loc = (By.CSS_SELECTOR,'.submit' )                                                       #处理确定btn
    fbk_dealClose_loc = (By.CSS_SELECTOR, '#dealClose')                                                     #关闭处理窗口
    
