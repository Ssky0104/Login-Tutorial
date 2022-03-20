#!F:/python/venv/Scripts/python.exe
import cgi

import mysql.connector

form = cgi.FieldStorage()

username = form.getvalue("txtuser")
password = form.getvalue("txtpass")

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<title>Hello -second CGI Program</title>")
print("</head>")
print("<body>")

print("<h2>Hello %s %s</h2>" % (username, password))
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pythonclass"
)
mycursor=mydb.cursor()
sql = "Select * from logintable where username=%s and password=%s"
val = (username,password)
mycursor.execute(sql,val)
myresult=mycursor.fetchall()
if(len(myresult)==1):
    print("login successfully")
else:
    print("login fail")

print("</body>")
print("</html>")