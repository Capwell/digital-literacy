import sqlite3

con = sqlite3.connect('star_wars.sqlite')
cur = con.cursor()

# Дорогой SQL, верни все столбцы всех записей из таблицы movies;
# символ * после SELECT означает "верни все поля найденных записей".
cur.execute('''
    SELECT *
    FROM ships;
''')

# Python превращает результирующую выборку в итерируемый объект, 
# который можно перебрать циклом:
for result in cur:
    print(result)

# Только те, у которых нет пассажиров
cur.execute('''
    SELECT name
    FROM ships
    WHERE passenger = '0' OR passenger = 'n/a';
''')


    
cur.execute('''
    SELECT name
    FROM ships
    WHERE passenger = '0' OR passenger = 'n/a'
    ORDER BY name DESC;
''')
for result in cur:
    print(result)

# При получении данных из таблицы коммит не нужен.
con.close()