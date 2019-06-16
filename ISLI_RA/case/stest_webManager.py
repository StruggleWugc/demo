import sys
# sys.path.append("..")
import random,unittest
from common import  variable
from common.function import getChar, lenChar, getCharEx, getDateTime, randomChar, new_window
from page.manager import webManger
from time import sleep


class newsManagerTest(unittest.TestCase):
    '''网站管理'''
    @classmethod
    def setUpClass(cls):
        # cls.logmanage =loginPage()
        cls.new = webManger()
        cls.new.open(webManger.url)
        cls.new.select_language()
        cls.new.user_login('isli', 'aaaaaa', '12')
        # cls.new.click(('id','itop_website'))
        # cls.new.open(webManger.web_url)
        cls.new.click(('css selector','#top_website'))
        cls.naviname = getChar('飞王菲12', 2)
    @classmethod
    def tearDownClass(cls):
        cls.new.close()


    ##新闻管理
    def test_01(self):
        '''发布新闻-必填项为空-发布失败'''
        sleep(1)
        self.new.buttonClick(self.new.addNewsPage_loc)
        sleep(0.5)
        #语种为空
        self.new.lineEdit(self.new.news_title_loc, '新的新闻1')
        self.new.lineEdit(self.new.news_time_loc, getDateTime())
        self.new.comboBox(self.new.news_navi_loc, 1)
        self.new.lineEdit(self.new.news_author_loc, '来源不明')
        self.new.lineEdit(self.new.news_priority_loc, '9')
        self.new.lineEdit(self.new.news_summary_loc, getChar('摘要', 100))
        self.new.news_content(getChar('内容新闻内容', 500))
        self.new.news_submit()
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_news_lang_loc), '请输入内容')
        #标题为空
        self.new.comboBox(self.new.news_lang_loc, random.randint(1, 3))
        self.new.lineEdit(self.new.news_title_loc, '')
        self.new.news_submit()
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_news_title_loc), '请输入内容')
        self.assertEqual(self.new.find_element(self.new.news_title_loc).get_attribute('placeholder'), '请输入新闻标题')
        #时间为空
        self.new.lineEdit(self.new.news_title_loc, '新的新闻1')
        self.new.lineEdit(self.new.news_time_loc, '')
        self.new.news_submit()
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_news_time_loc), '请输入内容')
        #所属栏目为空
        self.new.lineEdit(self.new.news_time_loc, getDateTime())
        self.new.comboBox(self.new.news_navi_loc, 0)
        self.new.news_submit()
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_news_navi_loc), '请输入内容')
        #来源为空
        self.new.comboBox(self.new.news_navi_loc, 1)
        self.new.lineEdit(self.new.news_author_loc, '')
        self.new.news_submit()
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_news_author_loc), '请输入内容')
        self.assertEqual(self.new.find_element(self.new.news_author_loc).get_attribute('placeholder'), '请输入来源')
        #摘要为空
        self.new.lineEdit(self.new.news_author_loc, '未知来源')
        self.new.lineEdit(self.new.news_summary_loc, '')
        self.new.news_submit()
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_news_summary_loc), '请输入内容')
        self.assertEqual(self.new.find_element(self.new.news_summary_loc).get_attribute('placeholder'), '请输入新闻摘要，限200字')
        #内容为空
        self.new.lineEdit(self.new.news_summary_loc, getChar('摘要132d', 50))
        self.new.news_content('')
        sleep(1)
        self.new.news_submit()
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_news_content_loc), '请输入内容')
        # self.assertEqual(new.find_element(*new.hint_news_content_loc).text, '0/30000 字符 ')                #断言错误，空格字符也会减1
        self.new.news_content(getChar('新闻内容发威发违法我', 100))
        
    def test_02(self):
        '''发布新闻-标题输入超过100字符-自动截取100'''
        self.new.lineEdit(self.new.news_title_loc, getChar('新的新闻 1', 101))
        sleep(0.5)
        self.assertEqual(lenChar(self.new,self.new.news_title_loc), 100 )
    
    def stest_03(self):
        '''发布新闻-时间输入错误的格式'''
        self.new.lineEdit(self.new.news_time_loc, '20117--12-12')
        self.new.buttonClick(self.new.news_author_loc)                                                                  #光标离开
        sleep(1)
        self.assertEqual(self.new.switch_to_alert().text, '不合法的日期格式或者日期超出限定范围,需要撤销吗?')
        self.new.switch_to_alert().accept()
        self.assertNotEqual(self.new.find_element(self.new.news_time_loc).get_attribute('value'), '2017--12-12')
        self.new.lineEdit(self.new.news_time_loc, '21425d3')
        self.new.buttonClick(self.new.news_author_loc)                                                                  #光标离开
        self.assertEqual(self.new.switch_to_alert().text, '不合法的日期格式或者日期超出限定范围,需要撤销吗?')
        self.new.switch_to_alert().dismiss()
        self.assertEqual(self.new.find_element(self.new.news_time_loc).get_attribute('value'), '21425d3')
        self.new.lineEdit(self.new.news_time_loc, '21425d3')
        self.new.buttonClick(self.new.news_author_loc)                                                                   #光标离开
        self.assertEqual(self.new.switch_to_alert().text, '不合法的日期格式或者日期超出限定范围,需要撤销吗?')
        self.new.switch_to_alert().accept()
        self.assertNotEqual(self.new.find_element(self.new.news_time_loc).get_attribute('value'), '21425d3')
        
        
    def test_04(self):
        '''发布新闻-来源输入超过100字符-自动截取100'''
        sleep(3)
        self.new.lineEdit(self.new.news_author_loc, getChar('wfwef为发威', 101))
        sleep(0.5)
        self.assertEqual(lenChar(self.new,self.new.news_author_loc), 100)
        
    def test_05(self):
        '''发布新闻-排序输入格式错误-报错提示'''
        sleep(2)
        self.new.lineEdit(self.new.news_priority_loc, '')
        self.assertEqual(self.new.find_element(self.new.news_priority_loc).get_attribute('placeholder'), '请输入排序')
        self.new.lineEdit(self.new.news_priority_loc, '@#')
        self.new.buttonClick(self.new.news_author_loc)                                                                   #光标离开
        self.new.buttonClick(self.new.news_submit_loc)
        sleep(0.5)
        self.assertEqual(lenChar(self.new, self.new.news_priority_loc), 1)
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_news_priority_loc), '请输入0-9的整数')
        self.new.lineEdit(self.new.news_priority_loc, '.')
        self.new.buttonClick(self.new.news_author_loc)                                                                   #光标离开
        sleep(0.5)
        self.assertEqual(lenChar(self.new,self.new.news_priority_loc), 1)
        self.assertEqual(self.new.error_hint(self.new.error_news_priority_loc), '请输入0-9的整数')
        self.new.lineEdit(self.new.news_priority_loc, '10')
        self.new.buttonClick(self.new.news_author_loc)                                                                   #光标离开
        sleep(0.5)
        self.assertEqual(lenChar(self.new,self.new.news_priority_loc), 1)
        
    def test_06(self):
        '''发布新闻-摘要输入超过200字符-自动截取200'''
        self.new.lineEdit(self.new.news_summary_loc, getChar('zfw找发威fw', 201))
        sleep(0.5)
        self.assertEqual(lenChar(self.new,self.new.news_summary_loc), 200)
        
    def test_07(self):
        '''发布新闻-内容超过30000字符-自动截取30000'''
        self.new.news_content_pro('稀饭我新闻内容发2342', 3000)
        sleep(0.5)
        self.new.find_element(('id','reset')).click()

    def test_08(self):
        '''流程-发布新闻并检查其正确性'''
        #new.left_menu(new.left_newsManager_loc)
        sleep(2)
        self.new.buttonClick(self.new.addNewsPage_loc)
        sleep(0.5)
        new1=[random.randint(1, 3), '新闻'+randomChar(2), getDateTime(), 1, '显示', random.randint(0, 9)]
        new2=[random.randint(1, 3), '新闻'+randomChar(2), getDateTime(-30), 2, '隐藏', random.randint(0, 9)]
        
        self.new.comboBox(self.new.news_lang_loc, new1[0])                                                              #语种
        self.new.lineEdit(self.new.news_title_loc,new1[1])                                                              #标题
        self.new.lineEdit(self.new.news_time_loc, new1[2])                                                              #发布时间
        new1[3]=self.new.comboBox(self.new.news_navi_loc, 1)                                                            #所属栏目
        self.new.lineEdit(self.new.news_author_loc, '内部新闻')
        self.new.lineEdit(self.new.news_priority_loc, new1[5])                                                          #排序
        self.new.lineEdit(self.new.news_summary_loc, '无新闻摘要')
        self.new.news_content(getChar('新闻内容', 200))
        self.new.buttonClick(self.new.news_submit_loc)
        sleep(1.5)
        self.new.buttonClick(self.new.addNewsPage_loc)
        sleep(0.5)
        self.new.comboBox(self.new.news_lang_loc, new2[0])                                                              #语种
        self.new.lineEdit(self.new.news_title_loc,new2[1])                                                              #标题
        self.new.lineEdit(self.new.news_time_loc, new2[2])                                                              #发布时间
        new2[3]=self.new.comboBox(self.new.news_navi_loc, 2)                                                            #所属栏目
        self.new.buttonClick(self.new.news_status2_loc)                                                                 #选择隐藏
        self.new.lineEdit(self.new.news_author_loc, '内部新闻')
        self.new.lineEdit(self.new.news_priority_loc, new2[5])                                                          #排序
        self.new.lineEdit(self.new.news_summary_loc, '无新闻摘要')
        self.new.news_content(getChar('新闻内容', 200))
        self.new.buttonClick(self.new.news_submit_loc)
        sleep(1)
        self.new.left_menu(self.new.left_newsManager_loc)
        sleep(1)
        self.new.refresh()
        #先搜索出来
        self.new.news_search(title='新闻')
        sleep(1)
#        self.assertEqual(new.info_table(new1[1], info='所属栏目'), new1[3])
#        self.assertEqual(new.info_table(new1[1], info='语种'), new1[0])
        self.assertEqual(self.new.info_table(new1[1], info='排序'), str(new1[5]))
        self.assertEqual(self.new.info_table(new1[1], info='发布时间'), new1[2])
        self.assertEqual(self.new.info_table(new1[1], info='状态'), new1[4])
#       self.assertEqual(new.info_table(new2[1], info='所属栏目'), new2[3])
#       self.assertEqual(new.info_table(new2[1], info='语种'), new2[0])
        self.new.news_search(title=new2[1])
        self.assertEqual(self.new.info_table(new2[1], info='排序'), str(new2[5]))
        self.assertEqual(self.new.info_table(new2[1], info='发布时间'), new2[2])
        self.assertEqual(self.new.info_table(new2[1], info='状态'), new2[4])
        

    '''栏目管理'''
    def test_09(self):
        '''新增栏目-输入已经存在的导航名称-报错提示'''
        self.new.parent_frame()
        self.new.left_menu(self.new.left_navigationsManager_loc)
        self.new.navi_addbutton('关于ISLI')
        sleep(0.5)
        frame_add = self.new.find_element(self.new.navi_iframe_loc)
        self.new.iframe(frame_add)
        self.new.comboBox(self.new.navi_menuType_loc, 1)
        self.new.lineEdit(self.new.navi_navNameCN_loc, 'ISLI介绍')
        self.new.buttonClick(self.new.navi_navDescCN_loc)
        self.new.buttonClick(self.new.navi_submit_loc)
        sleep(1)
        self.assertEqual(self.new.error_hint(self.new.error_navi_navNameCN_loc), '导航名称已经被使用')
        self.new.lineEdit(self.new.navi_navNameUS_loc, 'Introduction')
        self.new.buttonClick(self.new.navi_navDescUS_loc)
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_navi_navNameUS_loc), '导航名称已经被使用')
        self.new.lineEdit(self.new.navi_navNameTW_loc, 'ISLI介紹')
        self.new.buttonClick(self.new.navi_navDescTW_loc)
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_navi_navNameTW_loc), '导航名称已经被使用')
        self.new.parent_frame()
        
    def test_10(self):
        '''新增栏目-必填项为空-报错提示-新增失败'''
        self.new.parent_frame()
        self.new.left_menu(self.new.left_navigationsManager_loc)
        self.new.navi_addbutton('关于ISLI')
        frame_add = self.new.find_element(self.new.navi_iframe_loc)
        self.new.iframe(frame_add)
        #导航名称为空-中文
        self.new.lineEdit(self.new.navi_navNameUS_loc, 'Introduction123')
        self.new.lineEdit(self.new.navi_navNameTW_loc, 'ISLI介紹123')
        self.new.buttonClick(self.new.navi_submit_loc)
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_navi_navNameCN_loc), '请输入导航名称')
        self.new.lineEdit(self.new.navi_navNameCN_loc, 'islifw导航')
        #导航名称为空-英文
        self.new.lineEdit(self.new.navi_navNameUS_loc, '')
        self.new.buttonClick(self.new.navi_submit_loc)
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_navi_navNameUS_loc), '请输入导航名称')
        self.new.lineEdit(self.new.navi_navNameUS_loc, 'Introduction123')
        #导航名称为空-繁体
        self.new.lineEdit(self.new.navi_navNameTW_loc, '')
        self.new.buttonClick(self.new.navi_submit_loc)
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_navi_navNameTW_loc), '请输入导航名称')
        self.new.lineEdit(self.new.navi_navNameTW_loc, 'ISLI介紹123')
        self.new.buttonClick(self.new.navi_reset_loc)
        self.new.parent_frame()
        
    def test_11(self):
        '''新增栏目-导航名称输入41字符-自动截取40'''
        self.new.parent_frame()
        self.new.left_menu(self.new.left_navigationsManager_loc)
        self.new.navi_addbutton('关于ISLI')
        frame_add = self.new.find_element(self.new.navi_iframe_loc)
        self.new.iframe(frame_add)
        #ZH
        self.new.lineEdit(self.new.navi_navNameCN_loc, getChar('飞王菲12', 41))
        self.new.buttonClick(self.new.navi_navDescCN_loc)
        self.assertEqual(lenChar(self.new, self.new.navi_navNameCN_loc), 40)
        #EN
        self.new.lineEdit(self.new.navi_navNameUS_loc, getChar('13FOWIF FW', 41))
        self.new.buttonClick(self.new.navi_navDescUS_loc)
        self.assertEqual(lenChar(self.new, self.new.navi_navNameUS_loc), 40)
        #TW
        self.new.lineEdit(self.new.navi_navNameTW_loc, getChar('介紹 解釋', 41))
        self.new.buttonClick(self.new.navi_navDescTW_loc)
        self.assertEqual(lenChar(self.new, self.new.navi_navNameTW_loc), 40)
        self.new.parent_frame()
        
    def test_12(self):
        '''新增栏目-导航名称输入最短字符-1'''
        self.new.parent_frame()
        self.new.left_menu(self.new.left_navigationsManager_loc)
        self.new.navi_addbutton('关于ISLI')
        frame_add = self.new.find_element(self.new.navi_iframe_loc)
        self.new.iframe(frame_add)
        #导航名称-中文
        self.new.lineEdit(self.new.navi_navNameCN_loc, '介')
        self.new.lineEdit(self.new.navi_navNameUS_loc, 'Introduction123')
        self.new.lineEdit(self.new.navi_navNameTW_loc, 'ISLI介紹123')
        self.new.buttonClick(self.new.navi_submit_loc)
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_navi_navNameCN_loc), '请输入2~40个字符')
        self.new.lineEdit(self.new.navi_navNameCN_loc, 'islifw导航')
        #导航名称-英文
        self.new.lineEdit(self.new.navi_navNameUS_loc, 'I')
        self.new.lineEdit(self.new.navi_navDescUS_loc,'DESC')
        self.new.buttonClick(self.new.navi_submit_loc)
        sleep(0.25)
        self.assertEqual(self.new.error_hint(self.new.error_navi_navNameUS_loc), '请输入2~40个字符')
        self.new.lineEdit(self.new.navi_navNameUS_loc, 'Introduction123')
        #导航名称-繁体
        self.new.lineEdit(self.new.navi_navNameTW_loc, '紹')
        self.new.buttonClick(self.new.navi_submit_loc)
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_navi_navNameTW_loc), '请输入2~40个字符')
        self.new.lineEdit(self.new.navi_navNameTW_loc, 'ISLI介紹123')
        self.new.buttonClick(self.new.navi_reset_loc)
        self.new.parent_frame()
        
    def test_13(self):
        '''新增栏目-导航描述输入101字符-自动截取100'''
        self.new.parent_frame()
        self.new.left_menu(self.new.left_navigationsManager_loc)
        self.new.navi_addbutton('关于ISLI')
        frame_add = self.new.find_element(self.new.navi_iframe_loc)
        self.new.iframe(frame_add)
        #ZH
        self.new.lineEdit(self.new.navi_navDescCN_loc, getChar('飞王菲12', 101))
        self.new.buttonClick(self.new.navi_navNameCN_loc)
        self.assertEqual(lenChar(self.new, self.new.navi_navDescCN_loc), 100)
        #EN
        self.new.lineEdit(self.new.navi_navDescUS_loc, getChar('13FOWIF FW', 101))
        self.new.buttonClick(self.new.navi_navNameUS_loc)
        self.assertEqual(lenChar(self.new, self.new.navi_navDescUS_loc), 100)
        #TW
        self.new.lineEdit(self.new.navi_navDescTW_loc, getChar('介紹 解釋', 101))
        self.new.buttonClick(self.new.navi_navNameTW_loc)
        self.assertEqual(lenChar(self.new, self.new.navi_navDescTW_loc), 100)
        self.new.parent_frame()
        
    def test_14(self):
        '''新增栏目-各项输入最长字符-成功新增'''
        self.new.parent_frame()
        self.new.left_menu(self.new.left_navigationsManager_loc)
        self.new.navi_addbutton('关于ISLI')
        frame_add = self.new.find_element(self.new.navi_iframe_loc)
        self.new.iframe(frame_add)
        self.new.comboBox(self.new.navi_menuType_loc, 1)
        naviname = getChar('飞王菲12', 40)
        #ZH
        self.new.lineEdit(self.new.navi_navNameCN_loc, naviname)
        self.new.lineEdit(self.new.navi_navDescCN_loc, getChar('飞王菲12', 100))
        #EN
        self.new.lineEdit(self.new.navi_navNameUS_loc, getChar('13FOWIF FW', 40))
        self.new.lineEdit(self.new.navi_navDescUS_loc, getChar('13FOWIF FW', 100))
        #TW
        self.new.lineEdit(self.new.navi_navNameTW_loc, getChar('介紹 解釋', 40))
        self.new.lineEdit(self.new.navi_navDescTW_loc, getChar('介紹 解釋', 100))
        #提交
        self.new.buttonClick(self.new.navi_submit_loc)
        self.new.parent_frame()
        sleep(0.5)
        self.assertTrue(self.new.navi_naviExist(naviname))
        #删除该栏目
        self.new.navi_removebutton(naviname)
        sleep(0.5)
        self.new.buttonClick(self.new.navi_submitNon_loc)
        
    def test_15(self):
        '''新增栏目-各项输入最短字符-成功新增'''
        self.new.parent_frame()
        self.new.left_menu(self.new.left_navigationsManager_loc)
        self.new.navi_addbutton('关于ISLI')
        frame_add = self.new.find_element(self.new.navi_iframe_loc)
        self.new.iframe(frame_add)
        self.new.comboBox(self.new.navi_menuType_loc, 1)
        # naviname = getChar('飞王菲12', 2)
        #ZH
        self.new.lineEdit(self.new.navi_navNameCN_loc, self.naviname)
        self.new.lineEdit(self.new.navi_navDescCN_loc, getChar('飞王菲12', 100))
        #EN
        self.new.lineEdit(self.new.navi_navNameUS_loc, getChar('13FOWIF FW', 2))
        self.new.lineEdit(self.new.navi_navDescUS_loc, getChar('13FOWIF FW', 100))
        #TW
        self.new.lineEdit(self.new.navi_navNameTW_loc, getChar('介紹 解釋', 2))
        self.new.lineEdit(self.new.navi_navDescTW_loc, getChar('介紹 解釋', 100))
        #提交
        self.new.buttonClick(self.new.navi_submit_loc)
        self.new.parent_frame()
        sleep(1)
        self.assertTrue(self.new.navi_naviExist(self.naviname))
        self.new.open(r'http://172.16.3.52:8080/irap/web/navigation/toNavigationPage/1')
        self.new.move_to_element(('css selector','[navid="2"]'))
        self.assertTrue(self.new.navi_naviExist(self.naviname))
        self.new.open(r'https://172.16.3.53:8443/isli/irms/manage-website/base/news/index')
        self.new.parent_frame()
        self.new.left_menu(self.new.left_navigationsManager_loc)
        # self.new.navi_addbutton('关于ISLI')
        #删除该栏目
        # navi.navi_removebutton(self.naviname)
        # sleep(0.5)
        # navi.buttonClick(navi.navi_submitNon_loc)

    def test_16(self):
        '''修改栏目-导航名称已存在'''
        self.new.parent_frame()
        self.new.left_menu(self.new.left_navigationsManager_loc)
        sleep(0.5)
        self.new.navi_editbutton(self.naviname)
        sleep(0.5)
        frame_edit = self.new.find_element(self.new.navi_iframe_loc)
        self.new.iframe(frame_edit)
        # navi.comboBox(navi.navi_menuType_loc, 1)
        self.new.lineEdit(self.new.navi_navNameCN_loc, '常见问题解答')
        self.new.buttonClick(self.new.navi_navDescCN_loc)
        sleep(0.75)
        self.assertEqual(self.new.error_hint(self.new.error_navi_navNameCN_loc), '导航名称已经被使用')
        self.new.lineEdit(self.new.navi_navNameUS_loc, 'FAQs')
        sleep(0.5)
        self.new.buttonClick(self.new.navi_navDescUS_loc)
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_navi_navNameUS_loc), '导航名称已经被使用')
        self.new.lineEdit(self.new.navi_navNameTW_loc, '常見問題答疑')
        self.new.buttonClick(self.new.navi_navDescTW_loc)
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_navi_navNameTW_loc), '导航名称已经被使用')
        self.new.parent_frame()

    def test_17(self):
        '''修改栏目-必填项为空'''
        self.new.parent_frame()
        self.new.left_menu(self.new.left_navigationsManager_loc)
        self.new.navi_editbutton(self.naviname)
        frame_add = self.new.find_element(self.new.navi_iframe_loc)
        self.new.iframe(frame_add)
        #导航名称为空-中文
        self.new.lineEdit(self.new.navi_navNameCN_loc,'')
        self.new.lineEdit(self.new.navi_navNameUS_loc, 'Introduction123')
        self.new.lineEdit(self.new.navi_navNameTW_loc, 'ISLI介紹123')
        self.new.buttonClick(self.new.navi_submit_loc)
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_navi_navNameCN_loc), '请输入导航名称')
        self.new.lineEdit(self.new.navi_navNameCN_loc, 'islifw导航')
        #导航名称为空-英文
        self.new.lineEdit(self.new.navi_navNameUS_loc, '')
        self.new.buttonClick(self.new.navi_submit_loc)
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_navi_navNameUS_loc), '请输入导航名称')
        self.new.lineEdit(self.new.navi_navNameUS_loc, 'Introduction123')
        #导航名称为空-繁体
        self.new.lineEdit(self.new.navi_navNameTW_loc, '')
        self.new.buttonClick(self.new.navi_submit_loc)
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_navi_navNameTW_loc), '请输入导航名称')
        self.new.lineEdit(self.new.navi_navNameTW_loc, 'ISLI介紹123')
        self.new.buttonClick(self.new.navi_reset_loc)
        self.new.parent_frame()

    def test_18(self):
        '''修改栏目-导航名称输入41字符-自动截取40'''
        self.new.parent_frame()
        self.new.left_menu(self.new.left_navigationsManager_loc)
        self.new.navi_editbutton(self.naviname)
        frame_add = self.new.find_element(self.new.navi_iframe_loc)
        self.new.iframe(frame_add)
        #ZH
        self.new.lineEdit(self.new.navi_navNameCN_loc, getChar('飞王菲12', 41))
        self.new.buttonClick(self.new.navi_navDescCN_loc)
        self.assertEqual(lenChar(self.new, self.new.navi_navNameCN_loc), 40)
        #EN
        self.new.lineEdit(self.new.navi_navNameUS_loc, getChar('13FOWIF FW', 41))
        self.new.buttonClick(self.new.navi_navDescUS_loc)
        self.assertEqual(lenChar(self.new, self.new.navi_navNameUS_loc), 40)
        #TW
        self.new.lineEdit(self.new.navi_navNameTW_loc, getChar('介紹 解釋', 41))
        self.new.buttonClick(self.new.navi_navDescTW_loc)
        self.assertEqual(lenChar(self.new, self.new.navi_navNameTW_loc), 40)
        self.new.parent_frame()

    def test_19(self):
        '''修改栏目-导航名称输入最短字符-1'''
        self.new.parent_frame()
        self.new.left_menu(self.new.left_navigationsManager_loc)
        self.new.navi_editbutton(self.naviname)
        frame_add = self.new.find_element(self.new.navi_iframe_loc)
        self.new.iframe(frame_add)
        #导航名称-中文
        self.new.lineEdit(self.new.navi_navNameCN_loc, '介')
        self.new.lineEdit(self.new.navi_navNameUS_loc, 'Introduction123')
        self.new.lineEdit(self.new.navi_navNameTW_loc, 'ISLI介紹123')
        self.new.buttonClick(self.new.navi_submit_loc)
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_navi_navNameCN_loc), '请输入2~40个字符')
        self.new.lineEdit(self.new.navi_navNameCN_loc, 'islifw导航')
        #导航名称-英文
        self.new.lineEdit(self.new.navi_navNameUS_loc, 'I')
        self.new.buttonClick(self.new.navi_submit_loc)
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_navi_navNameUS_loc), '请输入2~40个字符')
        self.new.lineEdit(self.new.navi_navNameUS_loc, 'Introduction123')
        #导航名称-繁体
        self.new.lineEdit(self.new.navi_navNameTW_loc, '紹')
        self.new.buttonClick(self.new.navi_submit_loc)
        sleep(0.5)
        self.assertEqual(self.new.error_hint(self.new.error_navi_navNameTW_loc), '请输入2~40个字符')
        self.new.lineEdit(self.new.navi_navNameTW_loc, 'ISLI介紹123')
        self.new.buttonClick(self.new.navi_reset_loc)
        self.new.parent_frame()

    def test_20(self):
        '''修改栏目-导航描述输入101字符-自动截取100'''
        self.new.parent_frame()
        self.new.left_menu(self.new.left_navigationsManager_loc)
        self.new.navi_editbutton(self.naviname)
        frame_add = self.new.find_element(self.new.navi_iframe_loc)
        self.new.iframe(frame_add)
        #ZH
        self.new.lineEdit(self.new.navi_navDescCN_loc, getChar('飞王菲12', 101))
        self.new.buttonClick(self.new.navi_navNameCN_loc)
        self.assertEqual(lenChar(self.new, self.new.navi_navDescCN_loc), 100)
        #EN
        self.new.lineEdit(self.new.navi_navDescUS_loc, getChar('13FOWIF FW', 101))
        self.new.buttonClick(self.new.navi_navNameUS_loc)
        self.assertEqual(lenChar(self.new, self.new.navi_navDescUS_loc), 100)
        #TW
        self.new.lineEdit(self.new.navi_navDescTW_loc, getChar('介紹 解釋', 101))
        self.new.buttonClick(self.new.navi_navNameTW_loc)
        self.assertEqual(lenChar(self.new, self.new.navi_navDescTW_loc), 100)
        # navi.parent_frame()
        self.new.buttonClick(self.new.navi_submit_loc)
        self.new.parent_frame()
        self.assertTrue(self.new.navi_naviExist(self.naviname))
        #删除新增栏目
        self.new.navi_removebutton(self.naviname)
        sleep(0.5)
        self.new.buttonClick(self.new.navi_submitNon_loc)

    '''客户反馈'''
    def test_21(self):
        '''客户反馈-处理反馈时不填处理结果-报错提示'''
        self.new.open(self.new.home_url)
        #提交的反馈内容
        variable.newFbk = ['反馈'+randomChar(2), 'shi', 'xitest050@163.com', random.randint(1, 3), '18900001111', getChar('建议 1b', 10)]
        #新增反馈
        self.new.buttonClick(self.new.feedback_loc)
        sleep(1)
        self.new.lineEdit(self.new.fdk_title_loc, variable.newFbk[0])
        self.new.lineEdit(self.new.fdk_name_loc, variable.newFbk[1])
        self.new.lineEdit(self.new.fdk_email_loc, variable.newFbk[2])
        variable.newFbk[3]=self.new.comboBox(self.new.fdk_type_loc, variable.newFbk[3])
        self.new.lineEdit(self.new.fdk_mobile_loc, variable.newFbk[4])
        self.new.lineEdit(self.new.fdk_content_loc, variable.newFbk[5])
        self.new.buttonClick(self.new.fdk_submit_loc)
        # self.new.buttonClick(self.new.fdk_submit_ok_loc)
        #处理反馈
        self.new.open(self.new.url)
        self.new.user_login('isli', 'aaaaaa', '12')
        self.new.open(webManger.web_url)
        self.new.max_window()
        self.new.left_menu(self.new.left_feedback_loc)
        self.new.feedbk_search(title=variable.newFbk[0])
        sleep(1)
        self.assertEqual(self.new.info_table(title=variable.newFbk[0], info='类型'), variable.newFbk[3])
        self.assertEqual(self.new.info_table(title=variable.newFbk[0], info='反馈时间'), getDateTime())
        self.assertEqual(self.new.info_table(title=variable.newFbk[0], info='状态'), '未处理')
        self.new.operate_table(title=variable.newFbk[0], operate='dispose')
        sleep(1)
        self.new.buttonClick(self.new.fbk_dealSubmit_loc)                                                               #直接点击确定按钮
        self.assertEqual(self.new.error_hint(self.new.fbk_dealError_loc), '处理结果不能为空')
        self.new.buttonClick(self.new.fbk_dealClose_loc)                                                                #关闭弹窗
        
    def test_22(self):
        '''客户反馈-处理反馈输入内容后点击关闭'''
        self.new.operate_table(title=variable.newFbk[0], operate='dispose')
        sleep(1)
        self.new.lineEdit(self.new.fbk_dealOpinion_loc, getChar('自动处理 12dfa', 20))
        self.new.buttonClick(self.new.fbk_dealClose_loc)
        self.assertEqual(self.new.info_table(title=variable.newFbk[0], info='状态'), '未处理')
        
    def test_23(self):
        '''客户反馈-处理反馈输入201字符-自动截取200-成功提交'''
        self.new.operate_table(title=variable.newFbk[0], operate='dispose')
        sleep(1)
        self.new.lineEdit(self.new.fbk_dealOpinion_loc, getChar('自动处理 12dfa', 201))
        self.assertEqual(lenChar(self.new, self.new.fbk_dealOpinion_loc), 200)
        self.new.buttonClick(self.new.fbk_dealSubmit_loc)
        sleep(0.5)
        self.assertEqual(self.new.info_table(title=variable.newFbk[0], info='状态'), '已处理')
        
    def stest_24(self):
        '''客户反馈-主题输入21字符-自动截取20字符'''
        self.new.left_menu(self.new.left_feedback_loc)
        self.new.lineEdit(self.new.search_fdk_theme_loc, getChar('zfwzu地图', 21))
        self.new.buttonClick(self.new.search_submit_loc)                                                                #光标离开
        sleep(1)
        self.assertEqual(lenChar(self.new, self.new.search_fdk_theme_loc), 21)
        
    def test_25(self):
        '''客户反馈-主题输入框文字提示'''
        sleep(1)
        self.new.left_menu(self.new.left_feedback_loc)
        self.assertEqual(self.new.placeholder(self.new.search_fdk_theme_loc), '请输入主题或者关键字')
        
    def test_26(self):
        '''客户反馈-根据搜索条件检查结果列表'''
        sleep(1)
        searchdata = ['', getDateTime(), '', 1, 1]
        self.new.left_menu(self.new.left_feedback_loc)
        searchdata[3]=self.new.comboBox(self.new.search_fdk_status_loc, searchdata[3])
        searchdata[4]=self.new.comboBox(self.new.search_fdk_type_loc, searchdata[4])
        self.new.feedbk_search(starttime=searchdata[0], endtime=searchdata[1], title=searchdata[2])
        sleep(1)
        self.assertNotEqual(self.new.find_element(self.new.table_checkDataExist_loc).text, '暂无数据')                  #查询到数据则往下执行
        pagenum = self.new.page()                                                                                       #获取页数
        while(pagenum[0]<=pagenum[1]):
            tableList = self.new.info_table(searchdata[2], check='all')
            for tableline in tableList:
                if searchdata[2] !='':
                    self.assertIn(searchdata[2], tableline[0])                                                          #主题
                if searchdata[4] !='-全部-':
                    self.assertEqual(searchdata[4], tableline[1])                                                       #类型
                if searchdata[1]!='':                                                                                   #都不为空或endtime不为空
                    self.assertTrue(tableline[2]>=searchdata[0] and tableline[2]<=searchdata[1])                        #反馈时间
                elif searchdata[0]!='' and searchdata[1]=='':                                                          #只有starttime
                    self.assertTrue(tableline[2]>=searchdata[0])                                                        #反馈时间
                if searchdata[3] !='-全部-':
                    self.assertEqual(searchdata[3], tableline[3])                                                       #状态
            if pagenum[1]>1 and pagenum[0]<pagenum[1] and pagenum[0]<3:                                                #有超过1页，只检查前3页
                self.new.page('下一页')
                sleep(0.5)
            else:
                break
            pagenum = self.new.page()                                                                                   #获取页数
    
    def test_27(self):
        '''输入页码为范围内的页码-成功跳转'''
        sleep(1)
        self.new.left_menu(self.new.left_feedback_loc)
        pagenum = self.new.page()
        self.assertNotEqual(pagenum[1], 1)                                                                              #如果只有一页则报错提示
        if pagenum[1]<=11:
            pageNo = random.randint(1, pagenum[1])
        else:
            pageNo = 10
        self.new.lineEdit(self.new.toPageNo_loc, str(pageNo))
        self.new.page('跳转')
        sleep(0.5)
        pagenum = self.new.page()
        sleep(0.5)
        self.assertEqual(pagenum[0], pageNo)
        
    def test_28(self):
        '''输入页码小于1-跳转到第一页'''
        sleep(1)
        self.new.left_menu(self.new.left_feedback_loc)
        self.new.lineEdit(self.new.toPageNo_loc, '0')
        self.new.page('跳转')
        sleep(0.5)
        pagenum = self.new.page()
        self.assertEqual(pagenum[0], 1)
        self.new.lineEdit(self.new.toPageNo_loc, '-2')
        self.new.page('跳转')
        sleep(0.5)
        pagenum = self.new.page()
        self.assertEqual(pagenum[0], 1)
        
    def test_29(self):
        '''输入页码大于最大页码-跳转到最大页码'''
        sleep(1)
        self.new.left_menu(self.new.left_feedback_loc)
        pagenum = self.new.page()
        self.new.lineEdit(self.new.toPageNo_loc, str(pagenum[1]+1))
        self.new.page('跳转')
        sleep(0.5)
        pagenum = self.new.page()
        self.assertEqual(pagenum[0], pagenum[1])
        
    def test_30(self):
        '''输入页码为字母-跳转到第一页'''
        sleep(1)
        self.new.left_menu(self.new.left_feedback_loc)
        self.new.lineEdit(self.new.toPageNo_loc, 'ab')
        self.new.page('跳转')
        sleep(0.5)
        pagenum = self.new.page()
        self.assertEqual(pagenum[0], 1)
        
    def test_31(self):
        '''输入页码为特殊字符-跳转到第一页'''
        sleep(1)
        self.new.left_menu(self.new.left_feedback_loc)
        self.new.lineEdit(self.new.toPageNo_loc, '‘*')
        self.new.page('跳转')
        sleep(0.5)
        pagenum = self.new.page()
        self.assertEqual(pagenum[0], 1)

if __name__=="__main__":
    unittest.main()