import logging
import calendar
from flask.ext.appbuilder import ModelView
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder.charts.views import GroupByChartView
from flask.ext.appbuilder.models.group import aggregate_count
from flask.ext.babelpkg import lazy_gettext as _
import os

from app import db, appbuilder
from .models import Vet, State


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


class VetModelView(ModelView):
    datamodel = SQLAInterface(Vet)


    # name
    # address
    # address2
    # city
    # state
    # zipcode
    # work_phone
    # fax_number
    # email

    list_columns = ['name', 'work_phone', 'state']

    base_order = ('name', 'asc')
    # TODO Edit fields to match DB model
    show_fieldsets = [
        ('Summary', {'fields': ['name']}),
        (
            'Contact Info',
            {'fields': ['work_phone', 'fax_number', 'email'],
             'expanded': True}),
        (
            'Address Info',
            {'fields': ['address', 'address2', 'city', 'state', 'zipcode'],
             'expanded': False}),
    ]

    add_fieldsets = [
        ('Summary', {'fields': ['name']}),
        (
            'Contact Info',
            {'fields': ['work_phone', 'fax_number', 'email'],
             'expanded': True}),
        (
            'Address Info',
            {'fields': ['address', 'address2', 'city', 'state', 'zipcode'],
             'expanded': True}),
        ]

    edit_fieldsets = [
        ('Summary', {'fields': ['name']}),
        (
            'Contact Info',
            {'fields': ['work_phone', 'fax_number', 'email'],
             'expanded': True}),
        (
            'Address Info',
            {'fields': ['address', 'address2', 'city', 'state', 'zipcode'],
             'expanded': True}),
        ]


def pretty_month_year(value):
    return calendar.month_name[value.month] + ' ' + str(value.year)


def pretty_year(value):
    return str(value.year)


db.create_all()
fill_states()
appbuilder.add_view(VetModelView, "Vets", icon="fa-envelope")

