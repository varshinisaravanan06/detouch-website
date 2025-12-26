import sqlite3

con = sqlite3.connect("detouch.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE booking(
name TEXT,
phone TEXT,
email TEXT,
service TEXT,
date TEXT,
time TEXT
)
""")

cur.execute("""
CREATE TABLE contact(
name TEXT,
email TEXT,
message TEXT
)
""")

con.commit()
con.close()

print("Database created successfully")
