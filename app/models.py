import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, Numeric
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


class PaymentType(Model):
    id = Column(Integer, primary_key=True)
    payment_type = Column(String(50), unique=True, nullable=False)
    is_credit_card = Column(Boolean, nullable=False)

    def __repr__(self):
        return self.payment_type # Needs to return a field


class Payment(Model):
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'), nullable=False)
    person = relationship("Person")

    payment_type_id = Column(Integer, ForeignKey('payment_type.id'), nullable=False)
    # Logical SQL name, won't always match
    payment_type = relationship("PaymentType")  # Class name
    date = Column(Date, nullable=True)
    amount = Column(Integer, nullable=True)
    adoption_id = Column(Integer, ForeignKey('adoption.id'), nullable=True)
    adoption = relationship("Adoption")
    memo = Column(String(564))

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
    memo = Column(String(564))

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
    memo = Column(String(564))

    def __repr__(self):
        return self.name


class AnimalType(Model):
    id = Column(Integer, primary_key=True)
    animal_type = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.animal_type


class Breed(Model):
    id = Column(Integer, primary_key=True)
    breed = Column(String(64), unique=True, nullable=False)
    type_id = Column(Integer, ForeignKey('animal_type.id'), nullable=False)
    animal_type = relationship("AnimalType")

    def __repr__(self):
        return self.breed


class Animal(Model):
    id = Column(Integer, primary_key=True)
    vet_id = Column(Integer, ForeignKey('vet.id'), nullable=True)
    vet = relationship("Vet")
    name = Column(String(150), unique=True, nullable=False)
    breed_id = Column(Integer, ForeignKey('breed.id'), nullable=False)
    breed_type = relationship("Breed")
    # FIXME Add medial history

    memo = Column(String(564))

    def __repr__(self):
        return self.name


class Adoption(Model):
    id = Column(Integer, primary_key=True)
    animal_id = Column(Integer, ForeignKey('animal.id'), nullable=False)
    animal_name = relationship("Animal")
    person_id = Column(Integer, ForeignKey('person.id'), nullable=False)
    person_name = relationship("Person")
    memo = Column(String(564))

    def __repr__(self):
        return self.id