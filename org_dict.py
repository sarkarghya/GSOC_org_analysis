import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from data_dict import id_data

driver = webdriver.Chrome(ChromeDriverManager().install()) #to just make it work anywhere

def org_dict(url):
    driver.get(url)
    time.sleep(15) #if you want to wait 15 seconds for the main page to load
    
    soup = BeautifulSoup(driver.page_source, 'lxml')
    orgs = soup.find_all('md-card', class_ = 'organization-card _md md-soc-theme flex') #find returns list, attrs returns dict
    return [id_data(data.attrs['data-id']) for data in orgs]