from datetime import datetime


# Coingecko free API support dates from May-2013 until present date


def date_is_supported(date):
    day = int(date[:2])
    month = int(date[3:5])
    year = int(date[-4:])

    present_date = datetime.now()
    input_date = datetime(year, month, day)

    if year < 2013:
        return False
    elif year == 2013 and month < 5:
        return False
    elif input_date > present_date:
        return False
    else:
        return True
