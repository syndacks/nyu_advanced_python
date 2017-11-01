import datetime as dt


def get_date(*argv):
    if argv:
        str_date = str(*argv)
        date_patterns = ['%Y-%m-%d', '%d-%b-%y', '%d/%m/%Y']
        for pattern in date_patterns:
            try:
                return dt.datetime.strptime(str_date, pattern)
            except:
                pass
    else:
        return dt.datetime.now()
