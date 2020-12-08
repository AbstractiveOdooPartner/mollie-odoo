# -*- coding: utf-8 -*-

{
    'name': 'Mollie Settlement Sync',
    'version': '12.0.1.1',
    'description': '',
    'summary': 'This module settlements from mollie',
    'author': 'Mollie',
    'maintainer': 'Applix',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'account_accountant', 'payment_mollie_official'
    ],
    'data': [
        'views/account_journal.xml',
        'views/bank_statement.xml',
        'views/templates.xml',
        'wizard/mollie_init_views.xml'
    ],
    "qweb": ['static/src/xml/*.xml'],
}
