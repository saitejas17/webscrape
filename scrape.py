import requests
from requests.exceptions import HTTPError
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import logging


class WebScrape:
    def __init__(self):
        self.header = []
        self.all_states = []
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s: %(name)s - %(levelname)s - %(message)s',
                            datefmt="%H:%M:%S")
        url = "https://timesofindia.indiatimes.com/coronavirus"
        try:
            page = requests.get(url)
            page.raise_for_status()
        except HTTPError as http_err:
            logging.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            logging.error(f'Other error occurred: {err}')
        else:
            logging.info("web page found, Scrapping process has started")
            chrome_options = Options()
            chrome_options.add_argument("--headless")

            self.driver = webdriver.Chrome(executable_path='C:/web scrape/chromedriver.exe', options=chrome_options)
            self.driver.get(url)

    def covidIndia(self):
        logging.info("Scrapping Covid_19 cases report! INDIA")
        self.driver.find_element_by_class_name("_2kQgJ").click()
        india = self.driver.find_element_by_class_name("_3fPqL")
        covid_india = []

        for row in india.find_elements_by_class_name("_2yreZ"):
            covid_india.append([td.text for td in row.find_elements_by_xpath(".//p")] +
                               [td.text for td in row.find_elements_by_xpath(".//h6")])

        covid_india[-1][0] = covid_india[-1][0].rstrip("\n?")

        logging.info("Finished scrapping Covid_19 cases report! INDIA")
        return covid_india

    def tableScrape(self):
        logging.info("Scrapping Covid_19 cases report table! STATE WISE")
        self.driver.find_element_by_class_name("_2c2s9").click()
        table = self.driver.find_element_by_xpath("//table")
        head = self.driver.find_element_by_xpath("//table[1]/thead")
        self.header = head.text.split(" ")
        self.header.insert(0, "SR.NO")



        for row in table.find_elements_by_xpath(".//tr"):

            if row.text != '':
                self.all_states.append([td.text for td in row.find_elements_by_xpath(".//td")])
            else:
                self.driver.find_element_by_class_name('ps__thumb-y').send_keys(Keys.PAGE_DOWN)
                self.all_states.append([td.text for td in row.find_elements_by_xpath(".//td")])
        logging.info("Finished scrapping Covid_19 cases report table! STATE WISE")
        return self.all_states

    def close_webpage(self):
        self.driver.close()
        logging.info("All done")
