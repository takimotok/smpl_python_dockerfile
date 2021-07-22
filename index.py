import sqlite3

# create DB as a file
# conn = sqlite3.connect('test_sqlite.db')
conn = sqlite3.connect(':memory:')

cursor = conn.cursor()

# create table
sql_create_table = """
create table persons(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name STRING
)
"""
cursor.execute(sql_create_table)
conn.commit()

# insert datum
sql_insert_datum = """
INSERT INTO persons (name) VALUES
('james'),
('ann'),
('catharin')
"""
cursor.execute(sql_insert_datum)
conn.commit()
sql_select = """
SELECT * FROM persons
"""
cursor.execute(sql_select)
print(cursor.fetchall()) # [(1, 'james'), (2, 'ann'), (3, 'catharin')]

# update datum
sql_udpate = """
UPDATE persons SET name = 'FOO' WHERE id = 1
"""
cursor.execute(sql_udpate)
conn.commit()
print(cursor.fetchall()) # [(1, 'Foo'), (2, 'ann'), (3, 'catharin')]

# delete
sql_delete = """
DELETE FROM persons WHERE id = 2
"""
cursor.execute(sql_delete)
conn.commit()
print(cursor.fetchall()) # [(1, 'Foo'), (3, 'catharin')]

cursor.close()
conn.close()
