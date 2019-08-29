import sqlite3

conn = sqlite3.connect('myquotes.db')
corr = conn.cursor()

# corr.execute("""create table quotes_tb(
#                     title text,
#                     author text,
#                     tag text
#                 )""")

corr.execute(
    """insert into quotes_tb values ('Python is awesome!', 'buildwithpython','python')""")

conn.commit()
conn.close()
