import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def main():
    # create a connection
    conn = sa.create_engine('sqlite:///zoo.db')

    # define the Zoo class and bind its attributes with db's columns
    Base = declarative_base()

    class Zoo(Base):
        __tablename__ = 'zoo'
        critter = sa.Column('critter', sa.String, primary_key=True)
        count = sa.Column('count', sa.Integer)
        damages = sa.Column('damages', sa.Float)

        def __init__(self, critter, count, damages):
            self.critter = critter
            self.count = count
            self.damages = damages

        def __repr__(self):
            return f"<Zoo({self.critter}, {self.count}, {self.damages})>"

    # create db and table
    Base.metadata.create_all(conn)

    # add date
    first = Zoo('duck', '10', 0.0)
    second = Zoo('bear', 2, 1000.0)
    third = Zoo('weasel', 1, 1000.0)
    print(first)
    print(second)
    print(third)

    # crete a session to connect our ORM with db(zoo.db)
    Session = sessionmaker(bind=conn)
    session = Session()

    # when we create our session, write our objects in db
    session.add(first)
    session.add_all([second, third])
    session.commit()



if __name__ == '__main__':
    main()
