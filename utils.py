
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException     
from selenium.webdriver.support.ui import Select

from time import sleep
import os

def getLinks(page):
     ''' Get links from webpage '''
     # Instance of chrome:
     driver = webdriver.Chrome(executable_path='/Users/robertodelprete/Downloads/COSMO-SkyMed/chromedriver')
     # Go to website
     pageFine=page.split('//')[-1]
     username, password = "ITA-2482", "Murphy_CSK3"
     webpage=f'https://{username}:{password}@'+pageFine

     driver.get(webpage)

     elems = driver.find_elements_by_xpath("//a[@href]")
     Links = []
     for elem in elems:
          link = elem.get_attribute("href")
          # print(link)
          Links.append(link)

     driver.quit()
     return Links


def saveLinks(prod_number, parentLinks):
     cwd = os.getcwd()
     outdir=cwd+f'/{prod_number}'
     os.makedirs(outdir, exist_ok=True)


     allLinks = []
     for page in parentLinks:
          Links = getLinks(page)
          allLinks += Links


     if outdir.endswith('/'):
          pass
     else:
          outdir+='/'


     with open(outdir+'Links.txt', 'w') as f:
          for link in allLinks:
               f.write(link)
               f.write('\n')

def main():
     print("Starting main")


if __name__ == "__main__":
     main()