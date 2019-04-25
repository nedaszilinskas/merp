# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

{
    'name': 'Ventor Picking Product Skip',
    "version": "8.0.1.0.0",
    'author': 'VentorTech',
    'website': 'https://ventor.tech/',
    'license': 'LGPL-3',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Allows smart skip of products in pickings
""",
    'summary': 'Allows smart skip of products in pickings',
    'depends': [
        'merp_base',
    ],
    'data': [
        'views/stock_picking.xml',
    ],
}
