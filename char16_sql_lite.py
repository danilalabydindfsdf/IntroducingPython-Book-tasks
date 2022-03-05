import sqlite3


def main():
    # connect to db
    conn = sqlite3.connect('enterprise.db')

    # create an cursor object to work with db query
    curs = conn.cursor()

    # create a simple table
    curs.execute('''CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)''')

if __name__ == '__main__':
    main()
