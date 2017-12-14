#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()



page = """<HTML>
  <HEAD><TITLE>Welcome</TITLE>
  <BODY>
    <H1>Hi!!</H1>
    Well, hello there!  Welcome to my page.  <A HREF="http://zombo.com">You can do anything here</A>.
  </BODY>
</HTML>"""

print('Content-type:  text/html\n')
print "<p>ticker: {}</p>".format(form["ticker"].value)


# print(page)
