import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

def id_data(iid):
    driver.get(f'https://summerofcode.withgoogle.com/organizations/{iid}/?sp-page=2')
    time.sleep(5) # sleep 5 seconds per page
    id_soup = BeautifulSoup(driver.page_source, 'lxml')
    data_dict ={}
    
    data_dict['name'] = id_soup.find('h1', class_ = 'banner__title').text

    tech = id_soup.find_all('li', class_ = 'organization__tag organization__tag--technology')
    data_dict['tech'] = [x.text.strip() for x in tech]
    
    data_dict['org_type'] = id_soup.find('li', class_ = 'organization__tag organization__tag--category').text.strip()
    
    topic = id_soup.find_all('li', class_ = 'organization__tag organization__tag--topic')
    data_dict['org_topics'] = [x.text.strip() for x in topic]
    
    students = []
    count = 0
    for student in id_soup.find_all('div', class_ = 'pos-rel'):
        if student.find('h2') == None:
            continue
        project = student.find('a', class_ = 'md-soc-theme')
        count += 1
        students.append([student.find('h2').text, 
                         project.text,
                         project.get('ng-href')])
        
    data_dict['num_students'] = count
    data_dict['students'] = students
    
    return data_dict   