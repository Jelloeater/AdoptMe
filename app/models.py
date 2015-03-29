import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from flask.ext.appbuilder import Model

mindate = datetime.date(datetime.MINYEAR, 1, 1)


class ContactGroup(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

class State(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Vet(Model):
    # TODO Add fields for proper model (take from create_database.py)
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)
    address = Column(String(564), nullable=False)
    address2 = Column(String(564))
    city = Column(String(564), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
    state = relationship("State")
    zipcode = Column(String(20), nullable=False)
    work_phone = Column(String(20), nullable=False)
    fax_number = Column(String(20))
    email = Column(String(564))

    def __repr__(self):
        return self.name

class Person(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)
    address = Column(String(564), nullable=False)
    address2 = Column(String(564))
    city = Column(String(564), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
    state = relationship("State")
    zipcode = Column(String(20), nullable=False)
    home_phone = Column(String(20))
    work_phone = Column(String(20))
    mobile_phone = Column(String(20))
    email = Column(String(564))

    def __repr__(self):
        return self.name