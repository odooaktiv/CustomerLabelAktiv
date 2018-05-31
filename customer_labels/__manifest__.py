# -*- coding: utf-8 -*-

{
    'name': 'Customer Labels',
    'category': 'Base',
    'version': '1.1',
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
