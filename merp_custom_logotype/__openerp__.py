# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Mobile Logo',
    "version": "8.0.1.0.0",
    'author': 'VentorTech',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Adds customer logotype for Ventor app
""",
    'summary': 'Custom Mobile Logo',
    'depends': [
        'merp_base',
    ],
    'data': [
        'views/merp_config.xml',
    ],
}
