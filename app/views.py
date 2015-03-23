import logging
import calendar
from flask.ext.appbuilder import ModelView
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder.charts.views import GroupByChartView
from flask.ext.appbuilder.models.group import aggregate_count
from flask.ext.babelpkg import lazy_gettext as _
import os

from app import db, appbuilder
from .models import ContactGroup, Gender, Contact, State


def fill_states():
    try:
        logging.info('Filling in States')
        import json
        # logging.debug(os.listdir(os.curdir))
        os.chdir('app')
        # logging.debug(os.listdir(os.curdir))
        state_list = json.loads(open('states.json').read())
        for state in state_list:
            db.session.add(State(name=state))
            db.session.commit()
    except:
        db.session.rollback()


def fill_gender():
    try:
        db.session.add(Gender(name='Male'))
        db.session.add(Gender(name='Female'))
        db.session.commit()
    except:
        db.session.rollback()

class ContactModelView(ModelView):
    datamodel = SQLAInterface(Contact)

    list_columns = ['name', 'personal_celphone', 'birthday', 'contact_group.name', 'state']

    base_order = ('name', 'asc')

    show_fieldsets = [
        ('Summary', {'fields': ['name', 'gender', 'contact_group']}),
        (
            'Personal Info',
            {'fields': ['address', 'birthday', 'personal_phone', 'personal_celphone', 'state'], 'expanded': False}),
        ]

    add_fieldsets = [
        ('Summary', {'fields': ['name', 'gender', 'contact_group']}),
        (
            'Personal Info',
            {'fields': ['address', 'birthday', 'personal_phone', 'personal_celphone', 'state'], 'expanded': False}),
        ]

    edit_fieldsets = [
        ('Summary', {'fields': ['name', 'gender', 'contact_group' ]}),
        (
            'Personal Info',
            {'fields': ['address', 'birthday', 'personal_phone', 'personal_celphone', 'state'], 'expanded': False}),
        ]


class GroupModelView(ModelView):
    datamodel = SQLAInterface(ContactGroup)
    related_views = [ContactModelView]



def pretty_month_year(value):
    return calendar.month_name[value.month] + ' ' + str(value.year)

def pretty_year(value):
    return str(value.year)


db.create_all()
fill_gender()
fill_states()
appbuilder.add_view(GroupModelView, "List Groups", icon="fa-folder-open-o", category="Contacts", category_icon='fa-envelope')
appbuilder.add_view(ContactModelView, "List Contacts", icon="fa-envelope", category="Contacts")
appbuilder.add_separator("Contacts")

