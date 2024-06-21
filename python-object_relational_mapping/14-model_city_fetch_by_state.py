#!/usr/bin/python3
"""Lists all the objects in the City table within the
hbtn_0e_6_usa database using SQLalchemy.
"""

import sys
from model_city import City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State). \
        join(State, City.state_id == State.id). \
        order_by(City.id).all()

    for row in query:
        print("{}: ({}) {}".format(row.State.name, row.City.id, row.City.name))
