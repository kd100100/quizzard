import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


df = pd.read_csv(r'slot2.csv')

print(len(df.axes[0]))


PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://quizzardslot2.pythonanywhere.com/admin')
##driver.get('http://127.0.0.1:5000/admin')

search = driver.find_element_by_name(////////)
search.send_keys(////////)

search.send_keys(Keys.RETURN)

##
for i in range(len(df.axes[0])):
    team_id = df.loc[i]['Unique ID'].lstrip().rstrip()
    password = df.loc[i]['Passcode']
    name = df.loc[i]['Name'].lstrip().rstrip().title()


    # time.sleep(5)

    time.sleep(2)

    search = driver.find_element_by_id('add-team_id')
    search.send_keys(team_id)
    password = str(password)
    search = driver.find_element_by_id('add-password')
    search.send_keys(password)
    
    search = driver.find_element_by_id('add-name1')
    search.send_keys(name)
    
    driver.find_element_by_css_selector("input#add-submit").click()

    # time.sleep(0.3)
