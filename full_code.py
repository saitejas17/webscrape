import requests
from requests.exceptions import HTTPError
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import logging
import csv


def write_csv(data, file_name):
    try:
        logging.info("Stated Writing in india_report.csv file")
        with open(file_name, 'w+', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)

    except IOError:
        logging.error("Writing is unsuccessful")

    finally:
        f.close()
        logging.info("Finished Writing")


def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        left_list = dataset[:mid]
        right_list = dataset[mid:]

        mergesort(left_list)
        mergesort(right_list)
        i = 0
        j = 0
        k = 0

        # while both arrays have content
        while i < len(left_list) and j < len(right_list):
            if left_list[i][1] < right_list[j][1]:
                dataset[k] = left_list[i]
                i += 1
            else:
                dataset[k] = right_list[j]
                j += 1
            k += 1

        # if the left array still has values, add them
        while i < len(left_list):
            dataset[k] = left_list[i]
            i += 1
            k += 1

        # if the right array still has values, add them
        while j < len(right_list):
            dataset[k] = right_list[j]
            j += 1
            k += 1
    return dataset


def scrape():
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

        driver = webdriver.Chrome(executable_path='C:/web scrape/chromedriver.exe', options=chrome_options)
        driver.get(url)

        logging.info("Scrapping Covid_19 cases report! INDIA")
        driver.find_element_by_class_name("_2kQgJ").click()
        india = driver.find_element_by_class_name("_3fPqL")
        covid_india = []

        for row in india.find_elements_by_class_name("_2yreZ"):
            covid_india.append([td.text for td in row.find_elements_by_xpath(".//p")] +
                               [td.text for td in row.find_elements_by_xpath(".//h6")])

        covid_india[-1][0] = covid_india[-1][0].rstrip("\n?")

        logging.info("Finished scrapping Covid_19 cases report! INDIA")

        write_csv(covid_india, "india_report.csv")

        logging.info("Scrapping Covid_19 cases report table! STATE WISE")
        driver.find_element_by_class_name("_2c2s9").click()
        table = driver.find_element_by_xpath("//table")
        head = driver.find_element_by_xpath("//table[1]/thead")
        header = head.text.split(" ")
        header.insert(0, "SR.NO")

        all_states = []

        for row in table.find_elements_by_xpath(".//tr"):

            if row.text != '':
                all_states.append([td.text for td in row.find_elements_by_xpath(".//td")])
            else:
                driver.find_element_by_class_name('ps__thumb-y').send_keys(Keys.PAGE_DOWN)
                all_states.append([td.text for td in row.find_elements_by_xpath(".//td")])
        logging.info("Finished scrapping Covid_19 cases report table! STATE WISE")
        # adding index to each row
        for n, row in enumerate(all_states[1:]):
            row.insert(0, n + 1)
        # sorting in alphabetical order
        # sorted_list = sorted(all_states[1:], key=lambda x: x[1])
        logging.info("Sorting the States in alphabetical order")
        sorted_list = mergesort(all_states[1:])
        logging.info("Finished sorting")
        sorted_list.insert(0, header)

        write_csv(sorted_list, "state_wise_table.csv")

        driver.quit()
        logging.info("All done")


if __name__ == "__main__":
    scrape()
