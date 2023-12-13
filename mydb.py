import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    passwd='password123',
    port=3306,
    user='root',
)

cursor = db.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS todo_db')

print('Created todo')