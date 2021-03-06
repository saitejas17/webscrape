import marge_sort
from scrape import WebScrape
import pytest


@pytest.fixture
def scrape_table_data():
    return [[], ['MH', '5226710', '78007', '4600196'], ['KA', '2053191', '20368', '1440621'],
            ['KL', '2010934', '6053', '1571738'], ['UP', '1563235', '16369', '1340251'],
            ['TN', '1468864', '16471', '1279658'], ['DL', '1361986', '20310', '1258951'],
            ['ANDHRA', '1344386', '8988', '1138028'], ['WB', '1053117', '12728', '911705'],
            ['CG', '883210', '11094', '749318'], ['RJ', '805658', '6158', '590390'],
            ['GJ', '714611', '8731', '578397'], ['MP', '700202', '6679', '583595'],
            ['HR', '652742', '6075', '539609'], ['BR', '622433', '3503', '519306'],
            ['OR', '565648', '2232', '473680'], ['TG', '511711', '2834', '449744'],
            ['PB', '467539', '11111', '376465'], ['AS', '310086', '1909', '265860'],
            ['JH', '301257', '4182', '246608'], ['UK', '264683', '4123', '183478'],
            ['JK', '229407', '2912', '174953'], ['HP', '145736', '2068', '104714'],
            ['GA', '127639', '1874', '92974'], ['PY', '77031', '1045', '60424'],
            ['CH', '52633', '599', '43506'], ['TR', '39054', '424', '34946'],
            ['MN', '37036', '526', '31238'], ['ML', '20985', '250', '17354'],
            ['AR', '20854', '69', '18691'], ['NL', '16890', '165', '13428'],
            ['LADAKH', '15807', '158', '14102'], ['SK', '10392', '183', '7343'],
            ['DADRA AND NAGAR HAVELI AND DAMAN AND DIU', '9150', '4', '8086'],
            ['MZ', '8176', '23', '6120'], ['AN', '6470', '81', '6175'], ['LD', '4202', '11', '3171']
            ]


def test_merge(scrape_table_data):
    assert marge_sort.mergesort(scrape_table_data[1:]) == sorted(scrape_table_data[1:], key=lambda x: x[1])


def test_table():
    ws = WebScrape()
    assert ws.covidIndia() == [["Confirmed Cases", "23,703,665"], ["Total Deaths", "258,317"],
                               ["Total Recovered", "19,734,823"], ["Active Cases", "3,710,525"]]

    assert ws.tableScrape() == [[], ['MH', '5226710', '78007', '4600196'], ['KA', '2053191', '20368', '1440621'],
                                ['KL', '2010934', '6053', '1571738'], ['UP', '1563235', '16369', '1340251'],
                                ['TN', '1468864', '16471', '1279658'], ['DL', '1361986', '20310', '1258951'],
                                ['ANDHRA', '1344386', '8988', '1138028'], ['WB', '1053117', '12728', '911705'],
                                ['CG', '883210', '11094', '749318'], ['RJ', '805658', '6158', '590390'],
                                ['GJ', '714611', '8731', '578397'], ['MP', '700202', '6679', '583595'],
                                ['HR', '652742', '6075', '539609'], ['BR', '622433', '3503', '519306'],
                                ['OR', '565648', '2232', '473680'], ['TG', '511711', '2834', '449744'],
                                ['PB', '467539', '11111', '376465'], ['AS', '310086', '1909', '265860'],
                                ['JH', '301257', '4182', '246608'], ['UK', '264683', '4123', '183478'],
                                ['JK', '229407', '2912', '174953'], ['HP', '145736', '2068', '104714'],
                                ['GA', '127639', '1874', '92974'], ['PY', '77031', '1045', '60424'],
                                ['CH', '52633', '599', '43506'], ['TR', '39054', '424', '34946'],
                                ['MN', '37036', '526', '31238'], ['ML', '20985', '250', '17354'],
                                ['AR', '20854', '69', '18691'], ['NL', '16890', '165', '13428'],
                                ['LADAKH', '15807', '158', '14102'], ['SK', '10392', '183', '7343'],
                                ['DADRA AND NAGAR HAVELI AND DAMAN AND DIU', '9150', '4', '8086'],
                                ['MZ', '8176', '23', '6120'], ['AN', '6470', '81', '6175'], ['LD', '4202', '11', '3171']
                                ]
    ws.close_webpage()
