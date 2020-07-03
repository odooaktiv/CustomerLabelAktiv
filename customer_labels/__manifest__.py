# -*- coding: utf-8 -*-

{
    'name': 'Customer Labels',
    'category': 'Extra Tools',
    'version': '11.0.1.0.0',
    'summary': 'This module is usually used to print 10 Customer Labels on each page.',
    'website': 'http://www.aktivsoftware.com',
    'author': 'Aktiv Software',
    'license': 'AGPL-3',
    'description': 'Print Customer Labels for the selected Customers.',

    'depends': [
        'contacts'
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
