import os
from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
from selenium.webdriver.chrome.options import Options
import time



class GnomadAPI():
    def __init__(self):
        print(os.getcwd())
        self.prefs = {"download.default_directory" : os.getcwd()};
        option = Options()
        option.add_experimental_option("prefs",self.prefs)
        option.add_argument("--headless")
        self.option=option
        self.StartDriver()
        self.GetRegion()
#option.add_argument("--disable-infobars")
#option.add_argument("start-maximized")
#option.add_argument("--disable-extensions")


#option.add_argument('--window-size=1920,1080')
#option.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 1 })
    def StartDriver(self):

        self.driver = webdriver.Chrome(options=self.option)
        
    def GetRegion(self):    
        self.driver.get("https://gnomad.broadinstitute.org/region/17-7560097-7590856?dataset=gnomad_r2_1")
        time.sleep(5)
        a=self.driver.find_elements_by_xpath("//*[contains(text(), 'Export variants to CSV')]")
        
        time.sleep(5)
        a[0].click()
        time.sleep(2)

#time.sleep(5)


#driver.quit()
