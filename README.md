# AdoptMe
An animal management database

## Requirements
Uses
flask-appbuilder (Python)
python-psycopg2 (Debian)
Postgres 9.1 (Debian)
postgresql-server-dev-* (Debian)

## Setup instructions
apt-get install postgresql-server-dev-* python-psycopg2 postgresql postgresql-client postgresql-
pip install flask-appbuilder

configure DB permissions and users

Create db 'adoptme'

Edit FAB config file(config.py) 
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/adoptme'
(ex) u postgres / p postgres
*NOTE* it is a good idea to pick a strong password, as this is just for testing

run 'run.py'
cd to App folder
fabmanager create-admin
Create admin user
login to web GUI with admin credentials
Create users

