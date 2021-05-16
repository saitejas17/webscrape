from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path='C:/web scrape/chromedriver.exe', options=chrome_options)
driver.get("https://timesofindia.indiatimes.com/coronavirus")
clickindia = driver.find_element_by_class_name("_2kQgJ").click()
#total_case = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/h6")
total_case = driver.find_element_by_class_name("_3fPqL")
covid_india = []
for row in total_case.find_elements_by_class_name("_2yreZ"):

    covid_india.append([td.text for td in row.find_elements_by_xpath(".//p")]+
                       [td.text for td in row.find_elements_by_xpath(".//h6")])






print(all_states)