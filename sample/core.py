from selenium import webdriver
from env import *
import time
from selenium.webdriver.firefox.options import Options

def image_name():
    # t = time.localtime()
    current_time = time.strftime("%Y%m%d%H%M%S")
    return current_time + ".png"
    
options = Options()
browser = webdriver.Remote(SELENIUM_REMOTE_URL,options=options)
browser.set_window_size(1920,1080)
browser.get(REMOTE_LINK)
while browser.find_element("xpath",'//*[contains(@class, "chart-gui-wrapper")]'):
    try:
        # Give only one class name, if you want to check multiple classes then 'and' will be use in XPATH
        # e.g //*[contains(@class, "class_name") and contains(@class, "second_class_name")]
        # /html/body/div[2]/div[5]/div[2]/div[1]
        ele = browser.find_element("xpath",'//*[contains(@class, "chart-container-border")]')
        scrrenshot = ele.screenshot_as_png
        with open(IMAGE_PATH + image_name(), 'wb') as f:
            f.write(scrrenshot)
        browser.quit()
        break
    except Exception as e:
        print(str(e))



