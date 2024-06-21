#!/usr/bin/python3
"""Lists all the objects in the State table within the
hbtn_0e_6_usa database using SQLalchemy.
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

    # If table empty
    if session.query(State).count() == 0:
        print("Nothing")
    else:
        first_row = session.query(State).first()
        print("{}: {}".format(first_row.id, first_row.name))
