from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn

"""
You can use the extra Flask-AppBuilder fields and Mixin's
AuditMixin will add automatic timestamp of created and modified by who
"""
import datetime
from sqlalchemy import Table, Column, Integer, String, Boolean, Numeric, SmallInteger, TIMESTAMP, ForeignKey, \
    create_engine, MetaData, Date

from sqlalchemy.orm import relationship
from flask.ext.appbuilder import Model


# http://flask-appbuilder.readthedocs.org/en/latest/quickhowto.html

mindate = datetime.date(datetime.MINYEAR, 1, 1)


class Payment_Types(Model):
    payment_type = Column('payment_type', String(10), primary_key=True),
    is_credit_card = Column('is_credit_card', Boolean, nullable=False)

    def __repr__(self):
        return self.name


class US_States(Model):
    Column('state', String(2), primary_key=True)

    def __repr__(self):
        return self.name


class Payments(Model):
    Column('payment_ID', Integer, primary_key=True),
    Column('person_ID', None, ForeignKey('Person.person_ID')),
    Column('payment_type', None, ForeignKey('Payment_Types.payment_type')),
    Column('timestamp', TIMESTAMP, nullable=False),
    Column('amount', Numeric, nullable=False)

    def __repr__(self):
        return self.name


class Person(Model):
    Column('person_ID', Integer, primary_key=True),
    Column('last_name', String(32), nullable=False),
    Column('first_name', String(32), nullable=False),
    Column('address', String(32), nullable=False),
    Column('address2', String(32)),
    Column('city', String(32), nullable=False),
    Column('state', None, ForeignKey('US_States.state'), nullable=False),
    Column('zip', String(10), nullable=False),
    Column('home_phone', String(22), nullable=False),
    Column('work_phone', String(22)),
    Column('mobile_phone', String(22)),
    Column('email', String(50)),
    Column('memo', String(200))

    def __repr__(self):
        return self.name

# Adoption = Table('Adoption', metadata,
# Column('adoption_ID', Integer, primary_key=True),
#                  Column('animal_ID', None, ForeignKey('Animal.animal_ID'), nullable=False),
#                  Column('person_ID', None, ForeignKey('Person.person_ID'), nullable=False),
#                  Column('is_foster', Boolean, nullable=False),
#                  Column('timestamp', TIMESTAMP, nullable=False),
#                  Column('memo', String(200)))
#
# Animal = Table('Animal', metadata,
#                Column('animal_ID', Integer, primary_key=True),
#                Column('animal_name', String(32), nullable=False),
#                Column('vet_ID', None, ForeignKey('Vet.vet_ID'), nullable=False),
#                Column('breed_id', None, ForeignKey('Breed.breed_ID')),
#                Column('sex', SmallInteger, nullable=False),
#                # 0 = not known, 1 = male, 2 = female, 9 = not applicable
#                Column('color', String(32), nullable=False),
#                Column('spay_nut', Boolean, nullable=False),
#                Column('spay_nut_date', Date, nullable=False),
#                Column('dh_date', Date),
#                Column('hwt_date', Date),
#                Column('rabies_date', Date),
#                Column('fvrcp_date', Date),
#                Column('leuk_date', Date),
#                Column('stool_date', Date),
#                Column('stool_result', String(32)),
#                Column('heart_guard_date', Date),
#                Column('has_aids', Boolean),
#                Column('death_date', Date),
#                Column('memo', String(200)))
#
# Breed = Table('Breed', metadata,
#               Column('breed_ID', Integer, primary_key=True),
#               Column('type', String(32)),  # Dog, Cat, Etc
#               Column('breed', String(32)))
#
# Vet = Table('Vet', metadata,
#             Column('vet_ID', Integer, primary_key=True),
#             Column('vet_name', String(32), nullable=False),
#             Column('address', String(32), nullable=False),
#             Column('address2', String(32)),
#             Column('city', String(32), nullable=False),
#             Column('state', None, ForeignKey('US_States.state'), nullable=False),
#             Column('zip', String(10), nullable=False),
#             Column('work_phone', String(22), nullable=False),
#             Column('work2_phone', String(22)),
#             Column('mobile_phone', String(22)),
#             Column('email', String(50)),
#             Column('memo', String(200)))
#
# metadata.drop_all(engine)
# metadata.create_all(engine)
