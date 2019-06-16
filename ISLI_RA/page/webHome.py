import sys
sys.path.append("..")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from page.base import Page, web_homePage
from time import sleep
# import win32gui, win32con


class homePage(Page, web_homePage):
    '''官网首页'''
    
    def up_menu(self, loc):
        WebDriverWait(self.driver, 10).until(lambda m:m.find_element(*loc).is_displayed())
        self.find_element(*loc).click()

    def buttonClick(self, loc):
        WebDriverWait(self.driver, 10).until(lambda b:b.find_element(*loc).is_displayed())
        self.find_element(*loc).click()
    
    def lineEdit(self, loc, text):
        WebDriverWait(self.driver, 10).until(lambda l:l.find_element(*loc).is_displayed())
        self.find_element(*loc).click()
        self.find_element(*loc).clear()
        self.find_element(*loc).send_keys(text)
        
    def comboBox(self, element_loc, index):
        '''选择某下拉选项，并返回其值'''
        select = Select(self.find_element(*element_loc))
        select.select_by_index(index)
        selected = select.all_selected_options
        return selected[0].text

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
        return self.find_elements(*element_loc).send_keys(path)

if __name__=="__main__":
    pass