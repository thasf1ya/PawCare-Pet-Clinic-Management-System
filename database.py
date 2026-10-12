import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="p4wc4re",
    database="pawcare"
)

cursor = connection.cursor()

print("Connected to MySQL successfully!")