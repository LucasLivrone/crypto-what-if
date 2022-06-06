from lxml import etree  # Support for XPATH
from bs4 import BeautifulSoup
import requests
from src.utils.date_validator import date_is_supported


def get_xpath(date):
    year_row = int(date[-4:]) - 2010  # year_row id has this pattern in source table
    month_column = int(date[3:5]) + 2  # month_column id has this pattern in source table
    xpath = "//*[@id=\"tablepress-32\"]/tbody/tr[" + str(year_row) + "]/td[" + str(month_column) + "]"
    return xpath


def scrap_price(date):
    usd_data_source_url = "http://estudiodelamo.com/cotizacion-historica-dolar-peso-argentina"
    webpage = requests.get(usd_data_source_url)
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))
    price = dom.xpath(get_xpath(date) + "/text()")[0]  # /text() will return the data value inside a list
    return price


def get_usd_historical_price(date):
    if date_is_supported(date):
        price = scrap_price(date)
        price = price[1:]  # Remove '$' from price
        price = price.replace(",", ".")
        price = float(price)
        return price
    else:
        return "Date is not supported"
