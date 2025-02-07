import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_drop_and_create.py`

connection = sqlite3.connect('coffeenaut_db.db')

query = """
INSERT INTO "cafes" VALUES (1, 'Owoce Warzywa', 'Gen. Romualda Traugutta 9, 90-106 Łódź, Poland', '8/10', 
'Hipster place with speciality coffee, food, cakes and alcohol.', 'owoce-warzywa-traugutta-lodz-pol', 
51.768887, 19.459594)
"""

connection.execute(query)

connection.commit()
connection.close()
