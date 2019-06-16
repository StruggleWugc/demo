import sys
sys.path.append("..")
from selenium.webdriver.common.keys import Keys
import os,random,configparser
import datetime
from common import variable

def randomChar(n):
    '''获取n个字符'''
    temp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    list = random.sample(temp, n)
    result=''
    for i in list:
        result = result+i
    return result
    
def getDateTime(t=0):
    '''获取日期如：2017-06-12
        默认为当前日期。t>0表示超前t天，t<0表示后退t天'''
    today = datetime.date.today()
    day = datetime.timedelta(days=t)
    return str(today+day)
    
def lenChar(driver, element):
    ##返回输入框数据长度
    ele = driver.find_element(element)
    return len(ele.get_attribute('value'))
    
def lenJudge(driver, element, lenn):
    ##输入框内数据长度判断
    ele = driver.find_element(element)
    lene = len(ele.get_attribute('value'))
    if lene==lenn:
        return True
    else:
        return False
            
def getChar(name, lenn=0):
    #返回指定长度的字符串
    if lenn <=0:
        return name
    else:
        temp = name
        while(len(temp)<lenn):
            temp = temp+name
        result = temp[:lenn]
        return result
   
def getCharEx(ex='all'):
    '''生成特殊字符'''
    charexen = "`~!@#$%^&*()_+-={}[];'\\:\"|,./<>?"
    charexcn = "·~！#￥%……&*（）——+【】；’、：“|，。、《》？"
    if ex=='all':
        charex = charexen + charexcn
        return charex
    elif ex=='en':
        return charexen
    elif ex=='cn':
        return charexcn
        
def insert_img(driver,file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split('test_case')[0]
    file_path = base+'report/image/'+file_name
    driver.get_screenshot_as_file(file_path)

    
def new_window(driver,windowName,url=''):
    '''新建一标签页,如果输入url则打开URL,操作标签即为新建的标签页'''
    allhandles1 = driver.window_handles
    while(1):
        if variable.Driver=="Firefox":
            js='window.open("");'
            driver.execute_script(js)
        elif variable.Driver=="Chrome":
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
        allhandles2 = driver.window_handles
        if len(allhandles2)>len(allhandles1):
            break
    new_window = 'None'
    for new_window in allhandles2:
        for handle in allhandles1:
            if new_window == handle:
                #new_window在allhandles1中，所以不是刚才添加的window
                new_window= 'None'
                break
        if new_window != 'None':
            #找到了刚才添加的window
            break
    driver.switch_to_window(new_window)
    variable.Tabs[windowName] = new_window
    if url!='':
        driver.get(url)

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn : os.path.getmtime(testreport + '\\' + fn))
    file_new = os.path.join(testreport,lists[-1])
    return file_new

def isElementExist(driver,element_loc):
    '''判断元素存在'''
    try:
        driver.find_element(*element_loc)
        return True
    except:
        return False

def read_ini():
    config = configparser.ConfigParser()
    #config.readfp(open('config.ini','wb'))
    conf_file = os.getcwd()+r'\data'
    config.read(conf_file+r'\config.ini')

    variable.Driver = config.get("config","Driver")
    variable.ENVI = config.get("config","RunningEnvironment")
    variable.StartUp_Mode = config.get("config","BootMode")
    variable.UserName = config.get("config","UserName")
    variable.Password = config.get("config","Password")
    variable.PublicationType = config.get("config","PublicationType")
    variable.BookName = config.get("config","BookName")
    variable.BookNum = config.get("config","BookNum")
    
def isbn():
    '''返回一个数组'''
    isbn1 = random.choice([978,979])
    isbn2 = random.randint(1,9)
    isbn3 = random.randint(1000,9999)
    isbn4 = random.randint(1000,9999)
    isbn5 = int(isbn1/100)+int((isbn1%100)/10)*3+isbn1%10+isbn2*3+int(isbn3/1000)+int((isbn3%1000)/100)*3+int((isbn3%100)/10)+(isbn3%10)*3+int(isbn4/1000)+int((isbn4%1000)/100)*3+int((isbn4%100)/10)+(isbn4%10)*3
    isbn5 = isbn5%10
    isbn5 = 10 - isbn5
    if isbn5==10:
        isbn5=0
    isbn=[isbn1,isbn2,isbn3,isbn4,isbn5]
    return isbn

def cn():
    cn1 = str(random.randint(0,9))+str(random.randint(0,9))
    cn2 = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
    cn3 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    cn = [cn1,cn2,cn3]
    return cn

if __name__ == '__main__':
    print(getDateTime())
    print(randomChar(6))
