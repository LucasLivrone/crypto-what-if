from datetime import datetime, timedelta


# Coingecko free API support dates from May-2013 until present date
# USD to ARS price is available from 2011 until previous month of present date


def date_is_supported(date):
    try:
        day = int(date[:2])
        month = int(date[3:5])
        year = int(date[-4:])
        input_date = datetime(year, month, day)
    except ValueError:
        return False

    present_date = datetime.now()
    last_month_date = present_date.replace(day=1) - timedelta(1)

    if year < 2013:
        return False
    elif year == 2013 and month < 5:
        return False
    elif input_date > last_month_date:
        return False
    else:
        return True


def input_is_valid(ars_quantity, crypto, date):
    if ars_quantity > 0 and len(crypto) > 0 and date_is_supported(date):
        return True
    else:
        return False


def input_failure(ars_quantity, crypto, date):
    failure_message = []
    if ars_quantity <= 0:
        failure_message.append("Argentinian pesos quantity should be greater than 0")
    if not crypto.isalpha():
        failure_message.append("Crypto is not supported")
    if not date_is_supported(date):
        failure_message.append("Date is not supported")
    return failure_message
