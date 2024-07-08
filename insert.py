import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEE VALUES (1,'MARY', 'kAMAU', 45, 34000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (2,'JAMES', 'WEKESA', 28, 134000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (3,'ANN', 'NDUTA', 36, 57000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (4,'JOE', 'WERE', 67, 120000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (5,'JANE', 'NDUTA', 36, 57000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (6,'EVERLYN', 'MURIITHI', 23, 600000.00)")
conn.commit()

print("Successfully added records")
conn.close()