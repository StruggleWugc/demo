import sys,time
sys.path.append("..")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from common import base
from time import sleep
from common.function import isElementExist, getChar


class webManger(base.BasePage):
    '''后台管理--登入'''
    url =r'https://172.16.3.53:8443/isli/irms/manage-manager/base/login'
    username_loc = ('css selector', '#username')                                       #用户名
    password_loc = ('css selector', '#password')                                       #密码
    validcode_loc = ('css selector', '#validCode')                                     #验证码
    submit_loc = ('css selector', '.login>input')                                      #登入btn
    language =('id','languageList')
    
    def login_username(self, username):
        '''账号'''
        WebDriverWait(self.driver,20).until(lambda d: d.find_element(*self.username_loc).is_displayed())
        self.find_element(self.username_loc).send_keys(username)
        
    def login_password(self, password):
        '''密码'''
        self.find_element(self.password_loc).send_keys(password)
        
    def login_validcode(self, validcode):
        '''验证码'''
        self.find_element(self.validcode_loc).send_keys(validcode)
        
    def login_submit(self):
        '''提交btn'''
        self.find_element(self.submit_loc).click()
        
    def user_login(self, username='username', password='password', validcode='validcode'):
        '''登录'''
        # self.open()
        sleep(2.5)
        self.login_username(username)
        self.login_password(password)
        self.login_validcode(validcode)
        self.login_submit()
        sleep(0.5)

    def select_language(self):
        '''语种选择'''
        self.select_by_value(self.language,'ZH_CN')
        time.sleep(0.5)

    def user_login_verify(self, username='', password='', validcode=''):
        '''登录'''
        self.user_login(username, password, validcode)
        
    

    '''后台管理系统-网站管理操作'''
    web_url = r'https://172.16.3.53:8443/isli/irms/manage-website/base/news/index'
    left_newsManager_loc = ('css selector', '#left_newsManager>a')                    #新闻管理
    left_navigationsManager_loc = ('css selector', '#left_navigationsManager>a')      #栏目管理
    left_contentManager_loc = ('css selector', '#left_contentManager>a')              #内容管理
    left_pictureManager_loc = ('css selector', '#left_pictureManager>a')              #图片管理
    left_websiteInformation_loc = ('css selector', '#left_websiteInformation>a')      #网站信息管理
    left_feedback_loc = ('css selector', '#left_feedback>a')                          #客户反馈管理
    
    ##新闻管理-搜索栏
    addNewsPage_loc = ('css selector', '.listBar>a')                                   #发布新闻
    search_startTime_loc = ('css selector', '#startTime')                              #发布时间-开始
    search_endTime_loc = ('css selector', '#endTime')                                  #发布时间-结束
    search_newsTitle_loc = ('name', "newsTitle")                                       #新闻标题
    search_langCode_loc = ('name', "langCode")                                         #语种
    search_submit_loc = ('css selector', '.searchButton')                              #搜索btn

    #客户反馈管理
    search_fdk_theme_loc = ('name', 'title')                                           #主题
    search_fdk_status_loc = ('name', 'feedbackStatus')                                 #状态
    search_fdk_type_loc = ('name', 'feedbackTypeId')                                   #类型
    
    ##底部换页栏
    page_loc = ('css selector', '.pageBox>a')                                         #所有页码按钮
    selectedPage_loc = ('css selector', '.pageBox>a.selected')                        #页码一
    allPage_loc = ('css selector', '.pageBox>span>b:nth-child(2)')                    #总页码数
    toPageNo_loc = ('css selector', '#toPageNo')                                      #页码输入框
    
    ##列表
    table_list_loc = '.tableList>tbody'                                                 #数据列表
    table_trn_loc = '.tableList>tbody>tr:nth-child(1)'                                  #第一组数据
    #检查是否有数据。.text=1或者.text=暂无数据
    table_checkDataExist_loc = ('css selector', '.tableList>tbody>tr:nth-child(1)>td:nth-child(1)') #列表序列号
    
    def table_trn_loc_set(self):
        self.table_trn_title_loc = ('css selector', self.table_trn_loc+'>td:nth-child(2)')                 #列表新闻标题
        self.table_trn_navi_loc = ('css selector', self.table_trn_loc+'>td:nth-child(3)')                  #列表所属栏目
        self.table_trn_lang_loc = ('css selector', self.table_trn_loc+'>td:nth-child(4)')                  #列表语种
        self.table_trn_priority_loc = ('css selector', self.table_trn_loc+'>td:nth-child(5)>input')        #列表排序
        self.table_trn_time_loc = ('css selector', self.table_trn_loc+'>td:nth-child(6)')                  #发布时间
        self.table_trn_status_loc = ('css selector', self.table_trn_loc+'>td:nth-child(7)')                #状态
        self.table_trn_operate_loc = self.table_trn_loc+'>td:nth-child(8)'
        self.table_trn_hide_loc = ('css selector', self.table_trn_operate_loc+'>a:nth-child(1)')           #隐藏
        self.table_trn_edit_loc = ('css selector', self.table_trn_operate_loc+'>a:nth-child(2)')           #修改
        self.table_trn_del_loc = ('css selector', self.table_trn_operate_loc+'>a:nth-child(3)')            #删除
        
        self.table_fbk_trn_them_loc = ('css selector', self.table_trn_loc+'>td:nth-child(2)')              #客户反馈列表-主题
        self.table_fbk_trn_content_loc = ('css selector', self.table_trn_loc+'>td:nth-child(3)')           #客户反馈列表-内容
        self.table_fbk_trn_type_loc = ('css selector', self.table_trn_loc+'>td:nth-child(4)')              #客户反馈列表-类型
        self.table_fbk_trn_time_loc = ('css selector', self.table_trn_loc+'>td:nth-child(5)')              #客户反馈列表-反馈时间
        self.table_fbk_trn_status_loc = ('css selector', self.table_trn_loc+'>td:nth-child(6)>span')       #客户反馈列表-状态
        self.table_fbk_trn_dispose_loc = ('css selector', self.table_trn_loc+'>td:nth-child(7)>a:nth-child(2)>img')    #客户反馈列表-处理
    
    ##新闻管理--新增新闻
    news_lang_loc = ('id', 'language')                                                                      #语种
    news_title_loc = ('css selector', '#title[name="title"]')                                                        #标题
    news_time_loc = ('css selector', '#createDateTime')                                                              #时间
    news_navi_loc = ('id', 'navigationId')                                                                  #所属栏目
    news_status2_loc = ('css selector', ".editNews>dl:nth-child(4)>dd>[value='1']")                                         #状态-隐藏
    news_author_loc = ('id', 'authorName')                                                                  #来源
    news_priority_loc = ('id', 'priorityLevel')                                                             #排序
    news_summary_loc = ('id', 'newsSummary')                                                                #摘要
    news_iframe_loc = ('css selector', 'iframe#baidu_editor_0')                                                      #内容iframe
    news_content_loc = ('css selector', '.view>body')                                                                #内容
    news_submit_loc = ('css selector', '#submit')                                                                    #提交
    
    #新增新闻--报错信息
    error_news_lang_loc = ('css selector', '.error[for="language"]')                                       #语种错误提示信息
    error_news_title_loc = ('css selector', '.error[for="title"]')                                         #标题错误提示信息
    error_news_time_loc = ('css selector', '.error[for="createDateTime"]')                                 #时间错误提示信息
    error_news_navi_loc = ('css selector', '.error[for="navigationId"]')                                   #所属栏目错误提示
    error_news_author_loc = ('css selector', '.error[for="authorName"]')                                   #来源错误提示
    error_news_priority_loc = ('css selector', '.error[for="priorityLevel"]')                              #排序错误提示
    error_news_summary_loc = ('css selector', '.error[for="newsSummary"]')                                 #摘要错误提示
    error_news_content_loc = ('id', 'edui1_elementpath')                                                   #内容错误提示
    hint_news_content_loc = ('id', 'edui1_wordcount')                                                      #内容字数显示

    ##栏目管理
    navi_iframe_loc = ('css selector', 'iframe#mainFrame')                                                 #设置弹窗
    navi_menuType_loc = ('id', 'menuType_')                                                                #导航类型
    navi_navNameCN_loc = ('id', 'navName_ZH_CN')                                                           #导航名称中文
    navi_navDescCN_loc = ('id', 'navDesc_ZH_CN')                                                           #导航描述中文
    navi_navNameUS_loc = ('id', 'navName_EN_US')                                                           #导航名称英文
    navi_navDescUS_loc = ('id', 'navDesc_EN_US')                                                           #导航描述英文
    navi_navNameTW_loc = ('id', 'navName_ZH_TW')                                                           #导航名称-中文繁体
    navi_navDescTW_loc = ('id', 'navDesc_ZH_TW')                                                           #导航描述-中文繁体
    navi_submit_loc = ('id', 'submit')                                                                     #提交按钮
    navi_reset_loc = ('css selector', '.mt15 >input.reset')                                                #取消btn
    
    #报错提示
    error_navi_navNameCN_loc = ('css selector', '.error[for="navName_ZH_CN"]')                             #导航名称-中文错误提示
    error_navi_navNameUS_loc = ('css selector', '.error[for="navName_EN_US"]')                             #导航名称-英文错误提示
    error_navi_navNameTW_loc = ('css selector', '.error[for="navName_ZH_TW"]')                             #导航名称-中文繁体错误提示
    
    #删除提示弹窗
    navi_submitNon_loc = ('css selector', '.submitNon')                                                    #删除确认btn
    del_navi_reset_loc = ('css selector', '.centerButton>input.reset')                                     #删除取消btn

    ##反馈管理
    ##弹窗
    fbk_dealOpinion_loc = ('id', 'dealOpinion')                                                            #处理结果
    fbk_dealError_loc = ('id', 'dealError')                                                                #处理错误提示
    fbk_dealSubmit_loc = ('css selector','.submit' )                                                       #处理确定btn
    fbk_dealClose_loc = ('css selector', '#dealClose')                                                     #关闭处理窗口
    def left_menu(self, loc):
        '''点击菜单操作'''
        self.find_element(loc).click()
        sleep(1)
        
    def buttonClick(self, loc):
        '''点击btn操作'''
        self.find_element(loc).click()
        
    def lineEdit(self, loc, text):
        '''输入操作、参数text=None时，表示不对该输入框操作'''
        if text !='None':
            self.find_element(loc).click()
            self.find_element(loc).clear()
            self.find_element(loc).send_keys(text)
        
    def comboBox(self, loc, index):
        '''选择某下拉选项，并返回其值'''
        select = Select(self.find_element(loc))
        if index>=0:
            select.select_by_index(index)
        selected = select.all_selected_options
        return selected[0].text
        
    def news_submit(self):
        '''新闻管理新增提交操作'''
        self.find_element(self.news_submit_loc).click()

    def iframe(self,iframe):
        #切换iframe
        return self.driver.switch_to_frame(iframe)

    def parent_frame(self):
        #iframe
        return self.driver.switch_to.parent_frame()

    def switch_to_alert(self):
        #弹窗
        return self.driver.switch_to_alert()

    def news_content(self, text):
        '''新闻新增--内容输入'''
        frame2 = self.find_element(self.news_iframe_loc)
        self.iframe(frame2)
        self.lineEdit(self.news_content_loc, text)
        self.parent_frame()
        
    def news_content_pro(self, content, num):
        '''输入超过500字符可以'''
        frame2 = self.find_element(self.news_iframe_loc)
        self.iframe(frame2)
        self.find_element(self.news_content_loc).click()
        self.find_element(self.news_content_loc).clear()
        temp = getChar(content, 500)
        n=500
        while(n<=num):
            self.find_element(self.news_content_loc).send_keys(temp)
            temp = getChar(content, 500)
            n = n+500
        temp = getChar(content, num-n)
        self.find_element(self.news_content_loc).send_keys(temp)
        self.parent_frame()
        
        
    def news_search(self, starttime='None', endtime='None', title='', lang=-1):
        '''新闻管理搜索输入框'''
        self.lineEdit(self.search_startTime_loc, starttime)
        self.lineEdit(self.search_endTime_loc, endtime)
        self.lineEdit(self.search_newsTitle_loc, title)
        self.comboBox(self.search_langCode_loc, lang)
        self.buttonClick(self.search_submit_loc)
        
    def feedbk_search(self, starttime='None', endtime='None', title='', status=-1, type=-1):
        '''客户反馈管理搜索输入框'''
        self.lineEdit(self.search_startTime_loc, starttime)
        self.lineEdit(self.search_endTime_loc, endtime)
        self.lineEdit(self.search_fdk_theme_loc, title)
        self.comboBox(self.search_fdk_status_loc, status)
        self.comboBox(self.search_fdk_type_loc, type)
        self.buttonClick(self.search_submit_loc)
        
    def operate_table(self, title, priority='n', operate=''):
        """通过标题来获取各按钮"""
        '''只获取列表中靠前的一项'''
        sleep(0.7)
        for i in range(1, 50):
            self.table_trn_loc = self.table_list_loc+'>tr:nth-child('+str(i)+')'
            self.table_trn_loc_set()
            if isElementExist(self.driver, self.table_trn_title_loc):
                if self.find_element(self.table_trn_title_loc).get_attribute('title')==title:
                    #找到了该标题
                    if priority !='n':
                        self.lineEdit(self.table_trn_priority_loc, priority)                #排序
                    if operate=='hide':
                        self.buttonClick(self.table_trn_hide_loc)                           #隐藏
                    elif operate=='edit':
                        self.buttonClick(self.table_trn_edit_loc)                           #修改
                    elif operate=='del':
                        self.buttonClick(self.table_trn_del_loc)                            #删除
                    elif operate=='dispose':
                        self.buttonClick(self.table_fbk_trn_dispose_loc)                    #客户反馈--处理
                    break
            elif i==49:
                print('未查询到该内容')
                
    def info_table(self, title, info='', check=''):
        """通过标题，获取新闻信息"""
        '''只获取列表中靠前的一项,如果check=all,则获取每一项信息,并保存在数组中'''
        sleep(0.8)
        if check=='':
            for i in range(1, 50):
                self.table_trn_loc = self.table_list_loc+'>tr:nth-child('+str(i)+')'
                self.table_trn_loc_set()
                if isElementExist(self.driver, self.table_trn_title_loc):
                    if self.find_element(self.table_trn_title_loc).get_attribute('title')==title:
                        #查找到该标题,执行以下步骤
                        if info =='所属栏目':
                            return self.find_element(self.table_trn_navi_loc).get_attribute('title')
                        elif info =='语种':
                            return self.find_element(self.table_trn_lang_loc).get_attribute('title')
                        elif info =='排序':
                            return self.find_element(self.table_trn_priority_loc).get_attribute('value')
                        elif info =='发布时间':
                            return self.find_element(self.table_trn_time_loc).text
                        elif info =='状态':
                            if isElementExist(self.driver, self.table_fbk_trn_status_loc):
                                #客户反馈状态
                                return self.find_element(self.table_fbk_trn_status_loc).text
                            else:
                                #新闻状态
                                return self.find_element(self.table_trn_status_loc).text
                        elif info =='内容':
                            return self.find_element(self.table_fbk_trn_content_loc).text
                        elif info =='类型':
                            return self.find_element(self.table_fbk_trn_type_loc).text
                        elif info =='反馈时间':
                            return self.find_element(self.table_fbk_trn_time_loc).text
                elif i==49:
                    print('未查询到该标题')
                    return '未查询到该标题'            #？？？
        else:
            #返回数组的内容：主题、类型、反馈时间、状态
            tinfo=[]
            self.table_trn_loc = self.table_list_loc+'>tr'
            addr_loc = ('css selector', self.table_trn_loc)
            checklist = self.find_elements(addr_loc)
            for n in range(1, len(checklist)+1):
                self.table_trn_loc = self.table_list_loc +'>tr:nth-child('+str(n)+')'
                self.table_trn_loc_set()
                temp=[]
                temp.append(self.find_element(self.table_fbk_trn_them_loc).get_attribute('title'))
                temp.append(self.find_element(self.table_fbk_trn_type_loc).text)
                temp.append(self.find_element(self.table_fbk_trn_time_loc).text)
                temp.append(self.find_element(self.table_fbk_trn_status_loc).text)
                tinfo.append(temp)
            return tinfo
            
    def page(self, text=''):
        '''通过输入页码来到达页面,返回当前页、总页数'''
        sleep(0.7)
        if text !='':
            pages = self.find_elements(self.page_loc)                  #所有页码操作
            for page in pages:
                if page.text==text:
                    page.click()
                    break
        else:
            #不输入则返回当前页、总页数
            return int(self.find_element(self.selectedPage_loc).text), int(self.find_element(self.allPage_loc).text)
    
    def navi_naviExist(self, text):
        '''用来判断栏目是否存在'''
        element_loc = ('link text', text)
        sleep(1)
        if isElementExist(self.driver, element_loc):
            return True
        return False
    
    def navi_addbutton(self, text):
        '''新增栏目'''
        element_loc = ('link text', text)
        sleep(2)
        if isElementExist(self.driver, element_loc):                        #判断栏目存在
            id = self.find_element(element_loc).get_attribute('id')
            id = 'addBtn_'+id[:16]
            add_loc = ('id', id)
            #self.perform(element_loc)
            self.buttonClick(element_loc)
            sleep(1)
            self.buttonClick(add_loc)
            sleep(0.5)
            
    def navi_editbutton(self, text):
        '''编辑栏目'''
        element_loc = ('link text', text)
        sleep(2)
        if isElementExist(self.driver, element_loc):
            id = self.find_element(element_loc).get_attribute('id')
            id = 'editBtn_'+id[:16]
            add_loc = ('id', id)
            #self.perform(element_loc)
            self.buttonClick(element_loc)
            sleep(1)
            self.buttonClick(add_loc)
            sleep(0.5)
    
    def navi_removebutton(self, text):
        '''删除栏目'''
        element_loc = ('link text', text)
        sleep(2)
        if isElementExist(self.driver, element_loc):
            id = self.find_element(element_loc).get_attribute('id')
            id = id[:16]+'_remove'
            remove_loc = ('id', id)
            self.buttonClick(element_loc)
            sleep(1)
            self.buttonClick(remove_loc)
            sleep(0.5)
            
    def error_hint(self, error_loc):
        '''获取错误提示信息'''
        if isElementExist(self.driver, error_loc):
            return self.find_element(error_loc).text
        else:
            return 'NonElement'
    
    def placeholder(self, loc):
        '''获取输入框提示信息'''
        return self.find_element(loc).get_attribute('placeholder')
    

    '''官网首页'''
    home_url = r'http://172.16.3.52:8080/irap/web/navigation/toNavigationPage/1'
    home_loc = ('css selector', '.lifirst [navid="1"]')                                      #首页
    about_loc = ('css selector', '.lifirst [navid="2"]')                                     #关于isli
    application_loc = ('css selector', '.lifirst [navid="3"]')                               #资源中心
    source_loc = ('css selector', '.lifirst [navid="4"]')                                    #应用isli
    message_loc = ('css selector', '.lifirst [navid="5"]')                                   #动态信息
    
    ##底部按钮栏
    feedback_loc = ('css selector', '.linkmap>a:nth-child(3)')                               #客户反馈入口
    
    ##客户反馈界面

    fdk_title_loc = ('css selector', '#_title')                                               #主题
    fdk_name_loc = ('css selector', '#_userName')                                             #姓名
    fdk_email_loc = ('css selector', '#userEmail')                                            #常用邮箱
    fdk_type_loc = ('css selector', '#_feedbackTypeId')                                       #类型
    fdk_mobile_loc = ('css selector', '#_userMobile')                                         #联系手机
    fdk_addfile_loc = ('css selector', '.addfile')                                            #上传文件
    fdk_content_loc = ('css selector', '#_feedbackContent')                                   #内容
    fdk_submit_loc = ('css selector', '.submit')                                             #提交
    
    #弹窗
    fdk_submit_ok_loc = ('css selector', '.submit.e-close')                                  #提交后确认弹窗
    
    def up_menu(self, loc):
        self.find_element(loc).click()

    # def buttonClick(self, loc):
    #     self.find_element(loc).click()
    #
    # def lineEdit(self, loc, text):
    #     self.find_element(loc).click()
    #     self.find_element(loc).clear()
    #     self.find_element(loc).send_keys(text)
        
    # def comboBox(self, element_loc, index):
    #     '''选择某下拉选项，并返回其值'''
    #     select = Select(self.find_element(element_loc))
    #     select.select_by_index(index)
    #     selected = select.all_selected_options
    #     return selected[0].text

    # def reg_uploadFile(self, element_loc, path):
    #     self.find_element(*element_loc).click()
    #     sleep(1)
    #     dialog = win32gui.FindWindow('#32770','文件上传')  #对话框
    #     ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    #     ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    #     Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
    #     button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
    #     sleep(1)
    #     win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, path)  #往输入框输入文件的绝对地址
    #     win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button) #按下button按钮
    #     sleep(1)
    def send_file(self,element_loc, path):
        '''文件上传操作'''
        return self.find_elements(element_loc).send_keys(path)

if __name__ =="__main__":
    pass