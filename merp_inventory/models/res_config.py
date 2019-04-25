# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from openerp import api, models, fields as odoo_fields


class StockConfigSettings(models.TransientModel):
    _inherit = 'stock.config.settings'

    default_inventory_location = odoo_fields.Many2one(
        comodel_name='stock.location',
        string='Default Inventory Location',
    )

    @api.model
    def get_default_inventory_values(self, fields):
        company = self.env.user.company_id
        return {
            'default_inventory_location': company.default_inventory_location.id,
        }

    @api.multi
    def set_company_inventory_values(self):
        company = self.env.user.company_id
        company.default_inventory_location = self.default_inventory_location
