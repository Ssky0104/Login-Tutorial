#!F:/python/venv/Scripts/python.exe
import cgi

#create instance of fieldstorage
form=cgi.FieldStorage()

#Get Data from fields
username=form.getvalue('txtuser')
password=form.getvalue('txtpass')

print("Contents-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello=JOSHNA JAIN</title>")
print("</head>")
print("<body>")

print("<h2>Hello %s %s</h2> % (username,password)")
if(username==password):
    print("Login successfull")
else:
    print("Login fail")

print("</body>")
print("</html>")
