# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

{
    'name': 'Ventor Outgoing Routing',
    "version": "8.0.1.0.0",
    'author': 'VentorTech',
    'website': 'https://ventor.tech/',
    'license': 'LGPL-3',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Adds Outgoing Routing options
=============================
name: sort by source location name (in alphabetical order)
removal_prio: sort by location removal strategy priority field
""",
    'summary': 'Adds Outgoing Routing options',
    'depends': [
        'merp_base',
    ],
    'data': [
        'views/res_config.xml',
        'views/stock.xml',
        'views/picking.xml'
    ],
}
