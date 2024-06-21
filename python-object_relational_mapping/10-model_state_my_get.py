#!/usr/bin/python3
"""
Lists the state.id object in the State table with the State name
that is passed as an argument within the hbtn_0e_6_usa database.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    arg_name = sys.argv[4]

    states = session.query(State).where(State.name == arg_name)

    # If state name arg doesnt exist
    if states.count() == 0:
        print("Not found")
    else:
        for row in states:
            print("{}".format(row.id))
