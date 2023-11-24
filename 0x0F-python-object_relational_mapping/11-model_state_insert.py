#!/usr/bin/python3
"""
    Query using SQL alchemy
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    lsn = State(name="Louisiana")
    session.add(lsn)
    session.commit()
    print(lsn.id)
    session.close()
