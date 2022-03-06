import sqlite3


def main():
    # connect to db
    conn = sqlite3.connect('enterprise.db')

    # create an cursor object to work with db query
    curs = conn.cursor()

    # create a simple table
    # curs.execute('''CREATE TABLE zoo1 (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)''')

    # add some dates
    ins = 'INSERT INTO zoo1 (critter, count, damages) VALUES(?, ?, ?)'
    curs.execute(ins, ('duck', 5, 0.0))
    curs.execute(ins, ('bear', 2, 1000.0))
    curs.execute(ins, ('weasel', 1, 2000.0))

    curs.execute('SELECT * FROM zoo1')
    rows = curs.fetchall()
    print(rows)

    curs.execute('SELECT * FROM zoo1 ORDER BY count')
    rows = curs.fetchall()
    print(rows)

    curs.execute('SELECT * FROM zoo1 ORDER BY count DESC')
    rows = curs.fetchall()
    print(rows)

    curs.execute('SELECT * FROM zoo1 WHERE damages = (SELECT MAX(damages) FROM zoo1)')
    rows = curs.fetchall()
    print(rows)

    curs.close()
    conn.close()


if __name__ == '__main__':
    main()
