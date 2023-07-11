import sqlite3

con = sqlite3.connect('star_wars.sqlite')

cur = con.cursor()


cur.execute(
    'INSERT INTO ships VALUES(?, ?);',
    ('CR90 corvette', '600')
) 

con.commit()
con.close() 