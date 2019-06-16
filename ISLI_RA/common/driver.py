from selenium import webdriver

def browser(mydriver):
    if mydriver=="Chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
        driver = webdriver.Chrome(chrome_options=options)
    elif mydriver=="Firefox":
        # profileDir = "C:\\Users\\shigx1219\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\phugd9za.default"
        # profile = webdriver.FirefoxProfile(profileDir)
        #driver = webdriver.Firefox(profile)
        driver = webdriver.Firefox()
    else:
        raise ValueError('Driver error')
    return driver
