__author__ = 'Jesse'

# from sqlalchemy.dialects.postgresql import \
# ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE, \
# DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INTEGER, \
# INTERVAL, JSON, JSONB, MACADDR, NUMERIC, OID, REAL, SMALLINT, TEXT, \
# TIME, TIMESTAMP, UUID, VARCHAR, INT4RANGE, INT8RANGE, NUMRANGE, \
# DATERANGE, TSRANGE, TSTZRANGE, TSVECTOR
# http://docs.sqlalchemy.org/en/rel_0_9/core/tutorial.html


from sqlalchemy import Table, Column, Integer, String, Boolean, Numeric, TIMESTAMP, ForeignKey, create_engine, MetaData

engine = create_engine('postgresql+pg8000://postgres:postgres@localhost:5432/testdb')

metadata = MetaData()

Payment_Types = Table('Payment_Types', metadata,
                      Column('payment_type', String(10), primary_key=True),
                      Column('is_credit_card', Boolean, nullable=False))

US_States = Table('US_States', metadata,
                  Column('state', String(2), primary_key=True))

Payments = Table('Payments', metadata,
                 Column('payment_ID', Integer, primary_key=True),
                 Column('person_ID', None, ForeignKey('Person.person_ID')),
                 Column('payment_type', None, ForeignKey('Payment_Types.payment_type')),
                 Column('timestamp', TIMESTAMP, nullable=False),
                 Column('amount', Numeric, nullable=False))

Person = Table('Person', metadata,
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
               Column('email', String(50)))

Vet = Table('Vet', metadata,
            Column('vet_ID', Integer, primary_key=True),
            Column('vet_name', String(32), nullable=False),
            Column('address', String(32), nullable=False),
            Column('address2', String(32)),
            Column('city', String(32), nullable=False),
            Column('state', None, ForeignKey('US_States.state'), nullable=False),
            Column('zip', String(10), nullable=False),
            Column('work_phone', String(22), nullable=False),
            Column('work2_phone', String(22)),
            Column('mobile_phone', String(22)),
            Column('email', String(50)))

Adoption = Table('Adoption', metadata,
                 Column('adoption_ID', Integer, primary_key=True),
                 Column('animal_ID', None, ForeignKey('Animal.animal_ID'), nullable=False),
                 Column('person_ID', None, ForeignKey('Person.person_ID'), nullable=False),
                 Column('timestamp', TIMESTAMP, nullable=False))

Breed = Table('Breed', metadata,
              Column('breed', String(32), primary_key=True))

metadata.drop_all(engine)
metadata.create_all(engine)