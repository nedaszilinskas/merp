# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

{
    'name': 'Ventor Stock Picking Report (sorted)',
    "version": "8.0.1.0.0",
    'author': 'VentorTech',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Sort Pack Operations within Stock Picking report
""",
    'summary': 'Sort pack operations in report',
    'depends': [
        'merp_picking_wave',
    ],
    'data': [
        'views/report_stockpicking.xml',
    ],
}
