### Web scraper performance improvement

In order to get web scraping data I moved from using Selenium to BeautifulSoup.

This improved scraping performance by 10 seconds.

Legacy Selenium code:
````python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.utils.date_validator import date_is_supported


def get_web_driver():
    usd_data_source_url = "http://estudiodelamo.com/cotizacion-historica-dolar-peso-argentina"
    options = Options()
    options.add_argument("--headless")  # Used to avoid opening the browser
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(usd_data_source_url)
    return driver


def get_xpath(date):
    year_row = int(date[-4:]) - 2010  # year_row id has this pattern in source table
    month_column = int(date[3:5]) + 2  # month_column id has this pattern in source table
    xpath = "//*[@id=\"tablepress-32\"]/tbody/tr[" + str(year_row) + "]/td[" + str(month_column) + "]"
    return xpath


def scrap_price(driver, price_xpath):
    return WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, price_xpath))).text


def get_usd_historical_price(date):
    if date_is_supported(date):
        driver = get_web_driver()
        price_xpath = get_xpath(date)
        price = scrap_price(driver, price_xpath)
        price = price[1:]  # Remove '$' from price
        price = price.replace(",", ".")
        price = float(price)
        return price
    else:
        return "Date is not supported"

````