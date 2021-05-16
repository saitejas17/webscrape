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
