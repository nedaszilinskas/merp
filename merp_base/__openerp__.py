# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

{
    'name': 'Ventor Base',
    "version": "8.0.1.1.0",
    'author': 'VentorTech',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Base module that allow relation between Ventor modules
""",
    'summary': 'Base module that allow relation between Ventor modules',
    'depends': [
        'base',
        'stock',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/merp_config.xml',
        'views/res_config.xml',
        'views/res_users.xml',
    ],
}
