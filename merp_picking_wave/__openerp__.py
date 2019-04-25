# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

{
    'name': 'Ventor Picking Wave',
    "version": "8.0.1.0.0",
    'author': 'VentorTech',
    'website': 'https://ventor.tech/',
    'license': 'LGPL-3',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Allows configurable picking wave
""",
    'summary': 'Allows configurable picking wave',
    'depends': [
        'merp_picking_wave_core',
    ],
    'data': [
        'views/res_config.xml',
        'views/stock_picking_wave.xml',
        'wizard/message_wizard.xml'
    ],
}
