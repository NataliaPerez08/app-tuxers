#!/usr/bin/python3
import cgi

print ("Content-type: text/html")
print ("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Iniciar Sesión</title>
    <link rel="stylesheet" href="/css/styles.css">
</head>
<body>
    <div id="login-container">
""")
form=cgi.FieldStorage()
print ("<h2>user:", form["user"].value)
print ("<h2>pass:", form["pass"].value)

print("""
    </div>
    <img src="/images/eevee.gif" alt="Logo" />
</body>
</html>
""")

#form=cgi.FieldStorage()
#print ("<p>user:", form["user"].value)
#print ("<p>pass:", form["pass"].value)

