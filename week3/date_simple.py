import datetime as dt


def get_date(*date_obj):
    """get_date(): takes an optional string and returns a date object"""
    if date_obj:
        str_date = str(*date_obj)
        date_patterns = ['%Y-%m-%d', '%d-%b-%y', '%d/%m/%Y']
        for pattern in date_patterns:
            try:
                return dt.datetime.strptime(str_date, pattern)
            except:
                pass
    else:
        return dt.datetime.now()


def add_day(date_obj, *days_to_delta):
    """add_day(): takes a date object and an optional integer and returns a date object"""
    if days_to_delta:
        time_delta = dt.timedelta(int(*days_to_delta))
        new_date_obj = date_obj + time_delta
    else:
        time_delta = dt.timedelta(1)
        new_date_obj = date_obj + time_delta
    return new_date_obj


def add_week(date_obj, *weeks_to_delta):
    """add_week(): same as add_day() but adding days * 7"""
    if weeks_to_delta:
        time_delta = dt.timedelta(int(*weeks_to_delta))
        week_delta = time_delta * 7
        new_date_obj = date_obj + week_delta
    else:
        time_delta = dt.timedelta(1)
        week_delta = time_delta * 7
        new_date_obj = date_obj + week_delta
    return new_date_obj


def format_date(date_obj, *out_format):
    """format_date(): takes a date object and an optional string and returns a string"""
    if out_format:
        format_dict = {
            'MM/DD/YYYY': '%m/%d/%Y',
            'DD-Mon-YY':'%d/%a/%y'
            }
        date_pattern = format_dict[str(*out_format)]
    else:
        date_pattern = '%d/%m/%Y'

    formated_string = date_obj.strftime(date_pattern)
    return formated_string
