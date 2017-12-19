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

def add_day(date_obj, days_to_delta=None):
    """add_day(): takes a date object and an optional integer and returns a date object"""
    if days_to_delta:
        time_delta = dt.timedelta(int(days_to_delta))
        new_date_obj = date_obj + time_delta
    else:
        time_delta = dt.timedelta(1)
        new_date_obj = date_obj + time_delta
    return new_date_obj


def add_week(date_obj, weeks_to_delta=None):
    """add_week(): same as add_day() but adding days * 7"""
    if weeks_to_delta:
        time_delta = dt.timedelta(int(weeks_to_delta))
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

# Tests for get_date
gd1 = get_date('5/5/2016')
assert type(gd1) is dt.date
assert str(gd1) == '2016-05-05'

gd2 = get_date('5-May-16')
assert type(gd2) is dt.date
assert str(gd2) == '2016-05-05'

gd3 = get_date('2016-05-05')
assert type(gd3) is dt.date
assert str(gd3) == '2016-05-05'

# test to see that passing no date string returns Today
gd4 = get_date()
assert type(gd4) is dt.date


#Tests for add_day
print "original: ", gd4
ad1 = add_day(gd4)
print "add a day to original"
print "ad1: ", ad1

ad2 = add_day(gd4, days_to_delta=-3)
print "subtract 3 from original"
print "ad2", ad2


# Test for add_week
aw1 = add_week(gd4) # same as add_day but adds 7 days
print "aw1: ", aw1
aw2 = add_week(gd4, weeks_to_delta=2) # same as add_day but adds 14 days
print "aw2: ", aw2


# dt_format = ds.format_date(dt, 'MM/DD/YYYY')
# dt_format = ds.format_date(dt, 'DD-Mon-YY')
# dt_format = ds.format_date(dt)
# print "dt_format", dt_format
