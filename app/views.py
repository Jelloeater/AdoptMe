from flask.ext.appbuilder.models.sqla.filters import FilterStartsWith
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
from .models import Vet, State, Person, Payment, Breed, Animal, AnimalHistory, AnimalType, AnimalStatus, \
    PaymentMethod, PaymentType, Color, Sex  # , PaymentType


def fill_data():
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
        logging.info('Filling in Payment Methods')
        payment_method_list = json.loads(open('paymentMethods.json').read())
        for payment_method in payment_method_list:
            db.session.add(PaymentMethod(payment_method=payment_method['payment_method'],
                                         is_credit_card=payment_method['is_credit_card']))
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

    # Import Animal Types
    try:
        logging.info('Filling in Colors')
        color_list = json.loads(open('colors.json').read())
        for color_item in color_list:
            db.session.add(Color(animal_color=color_item))
            db.session.commit()
    except:
        db.session.rollback()

    # Import Animal Types
    try:
        logging.info('Filling in Sex')
        color_list = json.loads(open('sex.json').read())
        for sex_item in color_list:
            db.session.add(Sex(animal_sex=sex_item))
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

    # Import paymentTypes methods
    try:
        logging.info('Filling in Payment Types')
        list_in = json.loads(open('paymentTypes.json').read())
        for sex in list_in:
            db.session.add(PaymentType(payment_type=sex))
            db.session.commit()
    except:
        db.session.rollback()

    # Import animalStatus methods
    try:
        logging.info('Filling in Animal Status')
        list_in = json.loads(open('animalStatus.json').read())
        for sex in list_in:
            db.session.add(AnimalStatus(status=sex))
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
    search_columns = ['name', 'work_phone', 'email', 'zipcode', 'memo']
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
    search_columns = ['name', 'work_phone', 'home_phone', 'mobile_phone', 'zipcode', 'memo']
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

    list_columns = ['person_id', 'person', 'payment_method', 'payment_type', 'date', 'amount', 'memo', 'animal_history_fk_id']
    base_order = ('date', 'asc')
    show_fieldsets = [
        (
            'Payment Info',
            {'fields': ['person_id', 'person' 'payment_method', 'payment_type', 'date', 'amount', 'memo', 'animal_history_fk_id'],
             'expanded': True}),
    ]

    add_fieldsets = [
        (
            'Payment Info',
            {'fields': ['person_id', 'payment_method', 'payment_type', 'date', 'amount', 'memo', 'animal_history_fk_id'],
             'expanded': True}),
    ]

    edit_fieldsets = [
        (
            'Payment Info',
            {'fields': ['person_id', 'payment_method', 'payment_type', 'date', 'amount', 'memo', 'animal_history_fk_id'],
             'expanded': True}),
    ]


class AnimalModelView(ModelView):
    datamodel = SQLAInterface(Animal)

    list_columns = ['id', 'name', 'vet', 'breed_type','sex','color']
    base_order = ('name', 'asc')
    show_fieldsets = [
        (
            'Summary',
            {'fields': ['id', 'name', 'vet', 'breed_type','sex','color'],
             'expanded': True}),
        (
            'Medical History',
            {'fields': ['spay_nut_date', 'dh_date', 'hwt_date', 'rabies_date', 'fvrcp_date', 'leuk_date',
                        'stool_date', 'stool_result', 'heart_guard_date', 'has_aids', 'birth_date', 'death_date',],
             'expanded': True})
    ]

    add_fieldsets = [
        (
            'Summary',
            {'fields': ['name', 'vet', 'breed_type','sex','color'],
             'expanded': True}),
        (
            'Medical History',
            {'fields': ['spay_nut_date', 'dh_date', 'hwt_date', 'rabies_date', 'fvrcp_date', 'leuk_date',
                        'stool_date', 'stool_result', 'heart_guard_date', 'has_aids', 'birth_date', 'death_date',],
             'expanded': True})
    ]

    edit_fieldsets = [
        (
            'Summary',
            {'fields': ['name', 'vet', 'breed_type','sex','color'],
             'expanded': True}),
        (
            'Medical History',
            {'fields': ['spay_nut_date', 'dh_date', 'hwt_date', 'rabies_date', 'fvrcp_date', 'leuk_date',
                        'stool_date', 'stool_result', 'heart_guard_date', 'has_aids', 'birth_date', 'death_date',],
             'expanded': True})
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

    list_columns = ['id', 'animal_id', 'animal_name', 'person_name', 'animal_status', 'date', 'memo']
    search_columns = ['animal_name', 'person_name', 'animal_status', 'date', 'memo']
    base_order = ('id', 'asc')
    # Animal ID's must be used as there can be multiple ones with the same name
    show_fieldsets = [
        (
            'Basic Info',
            {'fields': ['animal_id', 'animal_name', 'person_name', 'animal_status', 'date', 'memo'],
             'expanded': True}),
    ]


    add_fieldsets = [
        (
            'Basic Info',
            {'fields': ['animal_id', 'animal_name', 'person_name', 'animal_status', 'date', 'memo'],
             'expanded': True}),

    ]

    edit_fieldsets = [
        (
            'Basic Info',
            {'fields': ['animal_id', 'animal_name', 'person_name', 'animal_status', 'date', 'memo'],
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


class AnimalStatusModelView(ModelView):
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
    related_views = [AnimalHistoryModelView]


db.create_all()
fill_data()
appbuilder.add_view(VetModelView, "Vets", icon="fa-building-o", category='Vet')
appbuilder.add_view(VetMasterView, "Vet Listing", icon="fa-paw", category='Vet')

appbuilder.add_view(PersonModelView, "People", icon="fa-users", category='Customers')
appbuilder.add_view(PaymentModelView, "Payments", icon="fa-money", category='Customers')

appbuilder.add_view(AnimalModelView, "Animal", icon="fa-paw", category='Animals')
appbuilder.add_view(AnimalHistoryModelView, "Animal History", icon="fa-paw", category='Animals')
appbuilder.add_view(AnimalStatusModelView, "Edit Status", icon="fa-paw", category='Animals')
appbuilder.add_view(StatusMasterView, "List Status", icon="fa-paw", category='Animals')

appbuilder.add_view(BreedModelView, "Breed", icon="fa-paw", category='Breeds')
appbuilder.add_view(AnimalTypeModelView, "Animal Type", icon="fa-paw", category='Breeds')
appbuilder.add_view(BreedMasterView, "List Breeds", icon="fa-paw", category='Breeds')

appbuilder.add_link("Save-A-Pet", href="http://www.saveapetli.net/", icon="fa-paw")

