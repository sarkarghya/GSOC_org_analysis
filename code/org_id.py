import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install()) #to just make it work anywhere

def org_ids(url):
    driver.get(url)
 #   time.sleep(20) #if you want to wait 15 seconds for the main page to load
    
    soup = BeautifulSoup(driver.page_source, 'lxml')
    orgs = soup.find_all('md-card', class_ = 'organization-card _md md-soc-theme flex') #find returns list, attrs returns dict
    return [data.attrs['data-id'] for data in orgs]