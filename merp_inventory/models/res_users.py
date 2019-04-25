# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from openerp import api, models, fields


class User(models.Model):
    _inherit = 'res.users'
 
    default_inventory_location = fields.Many2one('stock.location',
        string='Default Inventory Location')
