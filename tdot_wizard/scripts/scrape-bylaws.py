from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://www.toronto.ca/legdocs/bylaws/lawlists.htm')

query = '/html/body/div[2]/div[2]/div[1]/div[3]/div/table/tbody/tr/td[1]/form/div/div/table/tbody/tr[2]/td[1]/font/a'
query = '/html/body/div[3]/div[2]/div[1]/div[3]/div/table/tbody/tr/td[1]/div/table[1]/tbody/tr[3]/td[1]/a'

query = '/html/body/div[3]/div[2]/div[1]/div[3]/div/table/tbody/tr/td[1]/*/a'
browser.find_elements(By.XPATH, query)

# nav_list = browser.find_elements(By.XPATH, query)


# print(nav.text)
print(nav_list[0].text)
# nav_list[0].get_property('href')
