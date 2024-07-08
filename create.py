import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE EMPLOYEE( 
ID INT PRIMARY KEY NOT NULL,
FIRSTNAME TEXT NOT NULL,
LASTNAME TEXT,
AGE INT,
SALARY REAL)
''')

print("Successfully created Employee table")