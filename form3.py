#!F:/python/venv/Scripts/python.exe

import cgi
import mysql.connector

form = cgi.FieldStorage()

username = form.getvalue("txtuser")
password = form.getvalue("txtpass")

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello-Second CGI Program</title>")
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
sql="INSERT INTO logintable (username,password) VAlUES(%s,%s)"
val=(username,password)
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted")

print("</body>")
print("</html>")