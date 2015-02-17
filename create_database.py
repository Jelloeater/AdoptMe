__author__ = 'Jesse'

# from sqlalchemy.dialects.postgresql import \
# ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE, \
#     DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INTEGER, \
#     INTERVAL, JSON, JSONB, MACADDR, NUMERIC, OID, REAL, SMALLINT, TEXT, \
#     TIME, TIMESTAMP, UUID, VARCHAR, INT4RANGE, INT8RANGE, NUMRANGE, \
#     DATERANGE, TSRANGE, TSTZRANGE, TSVECTOR
#     http://docs.sqlalchemy.org/en/rel_0_9/core/tutorial.html


from sqlalchemy import Table, Column, Integer, String, Boolean, Numeric, DateTime, ForeignKey, create_engine, MetaData

engine = create_engine('postgresql+pg8000://postgres:postgres@localhost:5432/testdb')

metadata = MetaData()

PaymentTypes = Table('Payment_Types', metadata,
                     Column('payment_type', String, length=10, primary_key=True),
                     Column('is_credit_card', Boolean))

Payments = Table('Payments', metadata,
                 Column('payment_ID', Integer, primary_key=True),
                 Column('person_ID', None, ForeignKey('Person.person_ID')),
                 Column('payment_type', None, ForeignKey('Payment_Types.payment_type')),
                 Column('timestamp', DateTime),
                 Column('amount', Numeric))

Person = Table('Person', metadata,
               Column('person_ID', Integer, primary_key=True),
               Column('last_name', String, length=32),
               Column('first_name', String, length=32),
               Column('first_name', String, length=32)

)