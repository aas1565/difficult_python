import sqlite3

conn = sqlite3.connect('example.db')

cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS actors (
        act_id INTEGER PRIMARY KEY,
        act_first_name varchar(50),
        act_last_name varchar(50),
        act_gender varchar(1)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS movie (
        mov_id INTEGER PRIMARY KEY,
        mov_title varchar(50)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS director (
        dir_id INTEGER PRIMARY KEY,
        dir_first_name varchar(50),
        dir_last_name varchar(50) 
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS movie_cast (
        act_id INTEGER,
        mov_id INTEGER,
        role varchar(50),
        FOREIGN KEY (act_id) REFERENCES actors(act_id),
        FOREIGN KEY (mov_id) REFERENCES movie(mov_id)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS oscar_awarded (
        award_id INTEGER PRIMARY KEY,
        mov_id INTEGER,
        FOREIGN KEY (mov_id) REFERENCES movie(mov_id)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS movie_direction (
        dir_id INTEGER,
        mov_id INTEGER,
        FOREIGN KEY (dir_id) REFERENCES director(dir_id)
    )
''')

conn.commit()

conn.close()

print('База данных и таблица успешно созданы!')
