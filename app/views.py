from flask.ext.appbuilder.views import MasterDetailView, CompactCRUDMixin
import logging
import calendar
from flask.ext.appbuilder import ModelView, IndexView
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder.charts.views import GroupByChartView, TimeChartView, BaseChartView
from flask.ext.appbuilder.models.group import aggregate_count
from flask.ext.babelpkg import lazy_gettext as _
import os

from flask.ext.appbuilder.models.datamodel import SQLAModel

from app import db, appbuilder
from .models import Vet, State, Person, Payment, PaymentType, Breed, Animal, AnimalHistory, AnimalType, AnimalStatus


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

    # Import Animal Types
    try:
        logging.info('Filling in Animal Types')
        type_list = json.loads(open('animalTypes.json').read())
        for type in type_list:
            db.session.add(AnimalType(animal_type=type))
            db.session.commit()
    except:
        db.session.rollback()

    # Import Breeds methods
    try:
        logging.info('Filling in Breeds')
        breed_list = json.loads(open('breedTypes.json').read())
        for breed in breed_list:
            db.session.add(Breed(breed=breed['breed'],
                                 type_id=breed['type_id']))
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
             'expanded': True}),
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
             'expanded': True}),
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
             'expanded': True}),
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

    list_columns = ['person', 'payment_type', 'date', 'amount', 'memo','adoption']
    base_order = ('date', 'asc')
    show_fieldsets = [
        (
            'Payment Info',
            {'fields': ['person', 'payment_type', 'date', 'amount', 'memo','adoption'],
             'expanded': True}),
    ]

    add_fieldsets = [
        (
            'Payment Info',
            {'fields': ['person', 'payment_type', 'date', 'amount', 'memo','adoption'],
             'expanded': True}),
    ]

    edit_fieldsets = [
        (
            'Payment Info',
            {'fields': ['person', 'payment_type', 'date', 'amount', 'memo','adoption'],
             'expanded': True}),
    ]


class AnimalModelView(ModelView):
    datamodel = SQLAInterface(Animal)

    list_columns = ['name']
    base_order = ('name', 'asc')
    show_fieldsets = [
        (
            'Summary',
            {'fields': ['name', 'vet', 'breed_type'],
             'expanded': True}),
    ]

    add_fieldsets = [
        (
            'Summary',
            {'fields': ['name', 'vet', 'breed_type'],
             'expanded': True}),
        ]

    edit_fieldsets = [
        (
            'Summary',
            {'fields': ['name', 'vet', 'breed_type'],
             'expanded': True}),
        ]


class BreedModelView(ModelView):
    datamodel = SQLAInterface(Breed)

    list_columns = ['breed']
    base_order = ('breed', 'asc')
    show_fieldsets = [
        (
            'Breed Name',
            {'fields': ['breed', 'animal_type'],
             'expanded': True}),
    ]

    add_fieldsets = [
        (
            'Breed Name',
            {'fields': ['breed', 'animal_type'],
             'expanded': True}),
    ]

    edit_fieldsets = [
        (
            'Breed Name',
            {'fields': ['breed', 'animal_type'],
             'expanded': True}),
    ]

class AnimalHistoryModelView(ModelView):
    datamodel = SQLAInterface(AnimalHistory)

    list_columns = ['id','animal_name', 'person_name', 'memo']
    base_order = ('id', 'asc')
    show_fieldsets = [
        (
            'Animal History Info',
            {'fields': ['animal_name', 'person_name','animal_status','memo'],
             'expanded': True}),
        ]

    add_fieldsets = [
        (
            'Animal History Info',
            {'fields': ['animal_name', 'person_name','animal_status','memo'],
             'expanded': True}),
        ]

    edit_fieldsets = [
        (
            'Animal History Info',
            {'fields': ['animal_name', 'person_name','animal_status','memo'],
             'expanded': True}),
        ]

class AnimalTypeModelView(ModelView):
    datamodel = SQLAInterface(AnimalType)

    list_columns = ['animal_type']
    base_order = ('animal_type', 'asc')
    show_fieldsets = [
        (
            'Summary',
            {'fields': ['animal_type'],
             'expanded': True}),
        ]

    add_fieldsets = [
        (
            'Summary',
            {'fields': ['animal_type'],
             'expanded': True}),
        ]

    edit_fieldsets = [
        (
            'Summary',
            {'fields': ['animal_type'],
             'expanded': True}),
        ]

class StatusModelView(ModelView):
    datamodel = SQLAInterface(AnimalStatus)

    list_columns = ['status']
    base_order = ('status', 'asc')
    show_fieldsets = [
        (
            'Summary',
            {'fields': ['status'],
             'expanded': True}),
        ]

    add_fieldsets = [
        (
            'Summary',
            {'fields': ['status'],
             'expanded': True}),
        ]

    edit_fieldsets = [
        (
            'Summary',
            {'fields': ['status'],
             'expanded': True}),
        ]

class BreedMasterView(MasterDetailView):
    datamodel = SQLAModel(Breed)
    related_views = [AnimalModelView]

class VetMasterView(MasterDetailView):
    datamodel = SQLAModel(Vet)
    related_views = [AnimalModelView]

class StatusMasterView(MasterDetailView):
    datamodel = SQLAModel(AnimalStatus)
    related_views = [AnimalModelView]

db.create_all()
fill_data()
appbuilder.add_view(VetModelView, "Vets", icon="fa-building-o", category='Vet')
appbuilder.add_view(VetMasterView, "Vet Listing", icon="fa-paw", category='Vet')

appbuilder.add_view(PersonModelView, "People", icon="fa-users", category='Customers')
appbuilder.add_view(PaymentModelView, "Payments", icon="fa-money", category='Customers')

appbuilder.add_view(AnimalModelView, "Animal", icon="fa-paw", category='Animals')
appbuilder.add_view(AnimalHistoryModelView, "AnimalHistory", icon="fa-paw", category='Animals')
appbuilder.add_view(StatusModelView, "Status", icon="fa-paw", category='Animals')
appbuilder.add_view(StatusMasterView, "List Status", icon="fa-paw", category='Animals')

appbuilder.add_view(BreedModelView, "Breed", icon="fa-paw", category='Breeds')
appbuilder.add_view(AnimalTypeModelView, "Animal Type", icon="fa-paw", category='Breeds')
appbuilder.add_view(BreedMasterView, "List Breeds", icon="fa-paw", category='Breeds')


appbuilder.add_link("Save-A-Pet", href="http://www.saveapetli.net/", icon="fa-paw")

