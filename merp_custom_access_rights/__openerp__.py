# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

{
    'name': 'Ventor Custom Access Rights',
    "version": "8.0.1.0.0",
    'author': 'VentorTech',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Ventor Custom Access Rights
""",
    'summary': 'Ventor Custom Access Rights',
    'depends': [
        'merp_base',
    ],
    'data': [
        'security/groups.xml',
        'views/res_users.xml',
    ],
}
