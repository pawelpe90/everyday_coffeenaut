import sqlite3

connection = sqlite3.connect('./coffeenaut_db.db')

query = """
CREATE TABLE "cafes" (
    "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
    "name"	TEXT NOT NULL,
    "address"	TEXT,
    "score"	TEXT,
    "short_desc"    TEXT,
    "id_int"    TEXT,
    "lat"   REAL,
    "lon"   REAL
);
"""

connection.execute(query)

connection.commit()
connection.close()
