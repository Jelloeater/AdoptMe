import calendar
from flask.ext.appbuilder import ModelView
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder.charts.views import GroupByChartView
from flask.ext.appbuilder.models.group import aggregate_count
from flask.ext.babelpkg import lazy_gettext as _


from app import db, appbuilder
from models import Payment_Types, Payments, Person, US_States


class PersonModelView(ModelView):
    datamodel = SQLAInterface(Person)


    list_columns = ['person_ID', 'last_name', 'first_name', 'address', 'address2', 'city', 'state', 'zip', 'home_phone', 'work_phone', 'mobile_phone', 'email', 'memo']

    base_order = ('name', 'asc')

    show_fieldsets = [
        ('Summary', {'fields': list_columns}),
        (
            'Personal Info',
            {'fields': list_columns, 'expanded': False}),
        ]

    add_fieldsets = [
        ('Summary', {'fields': list_columns}),
        (
            'Personal Info',
            {'fields': list_columns, 'expanded': False}),
        ]

    edit_fieldsets = [
        ('Summary', {'fields': list_columns}),
        (
            'Personal Info',
            {'fields': list_columns, 'expanded': False}),
        ]





db.create_all()

appbuilder.add_separator("Contacts")

