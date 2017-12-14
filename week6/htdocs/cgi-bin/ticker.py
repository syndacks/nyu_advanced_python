#!/usr/bin/env python

import cgi
import datetime as dt
form = cgi.FieldStorage()

def get_price(symbol):
    import urllib2

    apikey = 'demo'

    url = ('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY'
           '&symbol={symbol}&interval=1min&apikey={apikey}'
           '&datatype=csv'.format(symbol=symbol, apikey=apikey))

    try:
        text = urllib2.urlopen(urllib2.Request(url)).read().decode('utf-8')
    except urllib2.URLError:
        exit('\nrequest error:  check internet connection.  \n\n'
             'URL requested:  ' + url)

    try:
        quote = text.splitlines()[1].split(',')[4]
    except IndexError:
        if 'demo purposes' in text:
            exit('\n*** NOTE ***  This demo URL can only be used with MSFT.  '
                 'To obtain live data on other symbols, you must edit your '
                 'program to change "apikey = " variable in this function to '
                 'a user key you can obtain from the "alphavantage" service '
                 'by signing up for a free account.  See error message below: '
                 ' \n\n' + text)

        exit('error parsing response.  Response:  ' + text)

    return quote

ticker_quote = get_price(form["ticker"].value)
date_now = dt.datetime.now()

print "Content-type:  text/html\n"
print "<HEAD> \
    <TITLE>Stock Ticker Request Form</TITLE> \
    <link href='../static/css/bootstrap.min.css' rel='"'stylesheet'"'> \
    <script src='"'../static/js/bootstrap.min.js'"'></script> \
  </HEAD>"
print "<p><strong>ticker</strong>: {}</p>".format(form["ticker"].value)
print "<p><strong>ticker_quote</strong>: {}</p>".format(ticker_quote)
print "<p><em>{}</em></p>".format(date_now)
