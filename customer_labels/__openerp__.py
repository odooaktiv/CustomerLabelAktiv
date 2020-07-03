# -*- coding: utf-8 -*-

{
    'name': 'Customer Labels',
    'category': 'Extra Tools',
    'version': '9.0.1.0.0',
    'summary': 'This module is usually used to print 10 Customer Labels on each page.',
    'website': 'http://www.aktivsoftware.com',
    'author': 'Aktiv Software',
    'license': 'AGPL-3',
    'description': 'Print Customer Label for the selected Customers.',

    'depends': [
        'sale'
    ],

    'data': [
        'views/customer_label_report.xml',
    ],

    'images': [
        'static/description/banner.jpg',
    ],

    'auto_install': False,
    'installable': True,
    'application': False

}
