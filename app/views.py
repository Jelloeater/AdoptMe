import logging
import calendar
from flask.ext.appbuilder import ModelView
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder.charts.views import GroupByChartView
from flask.ext.appbuilder.models.group import aggregate_count
from flask.ext.babelpkg import lazy_gettext as _
import os

from app import db, appbuilder
from .models import Vet, State, Person, Payment, PaymentType


def fill_data():
    # FIXME Only the first method call is getting executed on the DB
    import json
    # Import States
    try:
        logging.info('Filling in States')
        # logging.debug(os.listdir(os.curdir))
        os.chdir('app')
        # logging.debug(os.listdir(os.curdir))
        state_list = json.loads(open('states.json').read())
        for state in state_list:
            db.session.add(State(name=state))
            db.session.commit()
    except:
        db.session.rollback()

    # Import Payment methods
    try:
        logging.info('Filling in Payment Types')
        payment_type_list = json.loads(open('paymentTypes.json').read())
        for payment_type in payment_type_list:
            db.session.add(PaymentType(payment_type=payment_type['payment_type'],
                                       is_credit_card=payment_type['is_credit_card']))
            db.session.commit()
    except:
        db.session.rollback()



def pretty_month_year(value):
    return calendar.month_name[value.month] + ' ' + str(value.year)


def pretty_year(value):
    return str(value.year)


class VetModelView(ModelView):
    datamodel = SQLAInterface(Vet)

    list_columns = ['name', 'work_phone', 'memo']
    base_order = ('name', 'asc')
    show_fieldsets = [
        ('Summary', {'fields': ['name', 'memo']}),
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
        ('Summary', {'fields': ['name', 'memo']}),
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
        ('Summary', {'fields': ['name', 'memo']}),
        (
            'Contact Info',
            {'fields': ['work_phone', 'fax_number', 'email'],
             'expanded': True}),
        (
            'Address Info',
            {'fields': ['address', 'address2', 'city', 'state', 'zipcode'],
             'expanded': True}),
    ]


class PersonModelView(ModelView):
    datamodel = SQLAInterface(Person)

    list_columns = ['name', 'work_phone', 'home_phone', 'mobile_phone', 'memo']
    base_order = ('name', 'asc')
    show_fieldsets = [
        ('Summary', {'fields': ['name', 'memo']}),
        (
            'Contact Info',
            {'fields': ['work_phone', 'home_phone', 'mobile_phone', 'email'],
             'expanded': True}),
        (
            'Address Info',
            {'fields': ['address', 'address2', 'city', 'state', 'zipcode'],
             'expanded': False}),
    ]

    add_fieldsets = [
        ('Summary', {'fields': ['name', 'memo']}),
        (
            'Contact Info',
            {'fields': ['work_phone', 'home_phone', 'mobile_phone', 'email'],
             'expanded': True}),
        (
            'Address Info',
            {'fields': ['address', 'address2', 'city', 'state', 'zipcode'],
             'expanded': False}),
    ]

    edit_fieldsets = [
        ('Summary', {'fields': ['name', 'memo']}),
        (
            'Contact Info',
            {'fields': ['work_phone', 'home_phone', 'mobile_phone', 'email'],
             'expanded': True}),
        (
            'Address Info',
            {'fields': ['address', 'address2', 'city', 'state', 'zipcode'],
             'expanded': True}),
    ]


class PaymentModelView(ModelView):
    datamodel = SQLAInterface(Payment)

    list_columns = ['person', 'payment_type', 'date', 'amount', 'memo']
    base_order = ('date', 'asc')
    show_fieldsets = [
        (
            'Payment Info',
            {'fields': ['person', 'payment_type', 'date', 'amount', 'memo'],
             'expanded': True}),
    ]

    add_fieldsets = [
        (
            'Payment Info',
            {'fields': ['person', 'payment_type', 'date', 'amount', 'memo'],
             'expanded': True}),
    ]

    edit_fieldsets = [
        (
            'Payment Info',
            {'fields': ['person', 'payment_type', 'date', 'amount', 'memo'],
             'expanded': True}),
    ]


db.create_all()
fill_data()
appbuilder.add_view(VetModelView, "Vets", icon="fa-building-o")
appbuilder.add_view(PersonModelView, "People", icon="fa-users")
appbuilder.add_view(PaymentModelView, "Payments", icon="fa-money")

