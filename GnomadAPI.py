import os
from re import A
from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
from selenium.webdriver.chrome.options import Options
import time



class GnomadAPI():
    def __init__(self,gene=None,version=None,tmp='.tmp'):
        self.geneofinterest=gene
        self.gnomadversion=version
        self.tmpDir=tmp
        self.QueryGnomad()



    def QueryGnomad(self):
        self.SetOptions()
        self.StartDriver()
        time.sleep(2)
        self.GetGene()
        self.GetRegion()
        time.sleep(2)
        self.DownloadRegion()
        time.sleep(2)
    def SetOptions(self):
        cwkdir=os.getcwd()+f'/{self.tmpDir}'
        self.prefs = {"download.default_directory" : cwkdir};
        option = Options()
        option.add_experimental_option("prefs",self.prefs)
        #option.add_argument("--headless")
        self.option=option

    def StartDriver(self):
        self.driver = webdriver.Chrome(options=self.option)
        
    def GetGene(self):    
        self.driver.get(f"https://gnomad.broadinstitute.org/gene/{self.geneofinterest}?dataset={self.gnomadversion}")


    def tryFind(self,keySTR):
        while True:
            a=self.driver.find_elements_by_xpath(f"//*[contains(text(), '{keySTR}')]")
            print(a)
            if len(a)>0:
                return a
            else:
                time.sleep(3)

    def GetRegion(self):
        a=self.tryFind('region view')
        a[0].click()


    def DownloadRegion(self):
        a=self.tryFind('Export variants to CSV')

       # a=self.driver.find_elements_by_xpath("//*[contains(text(), 'Export variants to CSV')]")
        a[0].click()
        time.sleep(2)



#time.sleep(5)


#driver.quit()
