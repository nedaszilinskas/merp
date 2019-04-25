# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

{
    'name': 'Ventor Picking Advanced Search',
    "version": "8.0.1.0.0",
    'author': 'VentorTech',
    'website': 'https://ventor.tech/',
    'license': 'LGPL-3',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Advanced search for picking
===========================
Search by products not moved
""",
    'summary': 'Advanced search for picking',
    'depends': [
        'merp_base',
    ],
    'data': [
        'views/stock_picking.xml',
    ],
}
