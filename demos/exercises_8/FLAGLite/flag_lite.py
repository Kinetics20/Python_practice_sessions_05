import sqlite3

conn = sqlite3.connect('flag.db')
c = conn.cursor()

c.execute('SELECT character, character_index FROM flag_table GROUP BY character_index ORDER BY character_index')
records = c.fetchall()

conn.close()

flag = ''.join([record[0] for record in records])

print(f"Achieved flag: {flag}")
