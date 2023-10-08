#!/usr/bin/python3
import cgi
import psycopg2

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

try:
    connection = psycopg2.connect(user = "admin",
                                  password = "Tuxers2612",
                                  host = "10.0.0.6",
                                  port = "5432",
                                  database = "proyecto1")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    #print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    #print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)



print("""
    </div>
    <img src="/images/eevee.gif" alt="Logo" />
</body>
</html>
""")

#form=cgi.FieldStorage()
#print ("<p>user:", form["user"].value)
#print ("<p>pass:", form["pass"].value)

