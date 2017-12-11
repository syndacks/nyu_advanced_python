import date_simple as ds

"""The functions we'll create convert strings to dates, or dates to strings. Each
function either returns a datetime.date object (noted below as dt) or returns a
string that represents a date. """

dt = ds.get_date('2016-05-05')
# dt1 = ds.get_date('5/5/2016')
# dt2 = ds.get_date('5-May-16')
# dt3 = ds.get_date()

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
dt_format = ds.format_date(dt)
print "dt_format", dt_format
