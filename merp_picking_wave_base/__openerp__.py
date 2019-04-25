# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

{
    'name': 'Ventor Picking Wave Base Module',
    "version": "8.0.1.0.0",
    'author': 'Ventor, Xpansa Group',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Allows configurable picking and receiving wave
""",
    'summary': 'Allows configurable picking/picking wave',
    'depends': [
        'stock_picking_wave',
        'merp_base',
        'merp_custom_access_rights',
        'merp_picking_advanced_search',
        'merp_outgoing_routing'
    ],
    'data': [
        'views/stock_picking_wave.xml'
    ],
}
