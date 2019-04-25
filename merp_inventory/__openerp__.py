# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

{
    'name': 'Ventor Inventory Improvements',
    "version": "8.0.1.0.0",
    'author': 'Ventor, Xpansa Group',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Module allows to define default location that will be used for Inventory Adjustments instead of default 'WH/Stock'
""",
    'summary': 'Add small improvements to Inventory Adjustment process',
    'depends': [
        'merp_base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config.xml',
        'views/res_users.xml',
        'views/stock_inventory.xml',
    ],
}
