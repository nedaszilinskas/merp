# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from openerp import models, fields


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    is_internal = fields.Boolean(
        string='Is Internal Warehouse',
    )
