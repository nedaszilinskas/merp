# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from openerp import models, fields


class Company(models.Model):
    _inherit = 'res.company'

    default_inventory_location = fields.Many2one('stock.location',
        string='Default Inventory Location')