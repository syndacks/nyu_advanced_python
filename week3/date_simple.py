import datetime as dt


def get_date(date_string=None):
    """get_date(): takes an optional string and returns a date object"""
    if not isinstance(date_string, str):
        return dt.date.today()
    date_patterns = [
               '%m/%d/%Y', '%m/%d/%y', '%Y/%m/%d', '%y/%m/%d',
               '%Y-%m-%d', '%y-%m-%d', '%m-%d-%Y', '%m-%d-%y',
               '%d-%b-%y', '%d-%b-%Y', '%d-%B-%Y', '%d-%B-%y'
               ]
    for pattern in date_patterns:
        try:
            formatted_date = dt.datetime.strptime(date_string, pattern).date()
        except ValueError:
            continue
        return formatted_date

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

# Tests
dt1 = get_date('5/5/2016')
assert type(dt1) is dt.date
assert str(dt1) == '2016-05-05'

dt2 = get_date('5-May-16')
assert type(dt2) is dt.date
assert str(dt2) == '2016-05-05'

dt3 = get_date()
assert type(dt3) is dt.date
# print "dt", dt1
# print "dt", dt2
# print "dt", dt3

# dt2 = ds.add_day(dt, -3)
# dt3 = ds.add_day(dt)
# print "dt2", dt2
# print "dt3", dt3

# dt3_add_week = ds.add_week(dt)
# dt3_add_week = ds.add_week(dt,2)
# print "dt3_add_week", dt3_add_week

# dt_format = ds.format_date(dt, 'MM/DD/YYYY')
# dt_format = ds.format_date(dt, 'DD-Mon-YY')
# dt_format = ds.format_date(dt)
# print "dt_format", dt_format
