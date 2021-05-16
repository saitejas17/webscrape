import logging
from scrape import WebScrape
import write_to_csv
import marge_sort


def mainfunction():
    ws = WebScrape()
    covid_india = ws.covidIndia()
    write_to_csv.write_csv(covid_india, "india_report.csv")
    state_wise = ws.tableScrape()
    header = ws.header
    for n, row in enumerate(state_wise[1:]):
        row.insert(0, n + 1)
    logging.info("Sorting the States in alphabetical order")
    sorted_list = marge_sort.mergesort(state_wise[1:])
    logging.info("Finished sorting")
    sorted_list.insert(0, header)
    write_to_csv.write_csv(sorted_list, "state_wise_table.csv")
    ws.close_webpage()


if __name__ == "__main__":
    mainfunction()
