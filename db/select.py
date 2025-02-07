import sqlite3

connection = sqlite3.connect('coffeenaut_db.db')
cursor = connection.cursor()

query = """
SELECT * FROM "cafes";
"""

cursor.execute(query)

for row in cursor:
    print(row)

connection.close()
