import sqlalchemy as sa


def main():
    # create a connection
    conn = sa.create_engine('sqlite:///:memory:simple_db.db')

    # create a table
    #conn.execute('''CREATE TABLE zoo2 (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)''')

    #ins = 'INSERT INTO zoo2 (critter, count, damages) VALUES(?, ?, ?)'
    #conn.execute(ins, 'duck', 10, 0.0)
    #conn.execute(ins, 'bear', 2, 1000.0)
    #conn.execute(ins, 'weasel', 1, 2000.0)

    # rows is a special object called ResultProxy, you can iterate over it to display the data
    rows = conn.execute('SELECT * FROM zoo2')
    print(rows)
    for row in rows:
        print(row)

    # you can create a table and add data in more python way
    meta = sa.MetaData()
    zoo3 = sa.Table('zoo3', meta,
                    sa.Column('critter', sa.String, primary_key=True),
                    sa.Column('count', sa.Integer),
                    sa.Column('damages', sa.Float)
                    )
    meta.create_all(conn)

    conn.execute(zoo3.insert(('bear', 2, 1000.0)))
    conn.execute(zoo3.insert(('duck', 10, 0)))
    conn.execute(zoo3.insert(('weasel', 1, 2000.0)))

    result = conn.execute(zoo3.select())
    rows = result.fetchall()
    print(rows)


if __name__ == '__main__':
    main()
