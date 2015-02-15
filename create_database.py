__author__ = 'Jesse'

from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, ForeignKey, create_engine, MetaData

engine = create_engine('postgresql+pg8000://postgres:postgres@localhost:5432/testdb')

metadata = MetaData()

PaymentTypes = Table('Payment_Types', metadata,
                     Column('payment_type', String, primary_key=True),
                     Column('is_credit_card', Boolean))

Payments = Table('Payments', metadata,
                 Column('payment_ID', Integer, primary_key=True),
                 Column('person_ID', None, ForeignKey('Person.person_ID')),
                 Column('payment_type', None, ForeignKey('Payment_Types.payment_type')),
                 Column('date', DateTime))