# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from openerp import api, models, fields as odoo_fields


class StockConfigSettings(models.TransientModel):
    _inherit = 'stock.config.settings'

    outgoing_wave_behavior_on_confirm = odoo_fields.Selection(
        selection=[
            (0, 'Close pickings in wave with creation of backorders '
                'for incomplete pickings'),
            (1, 'Close pickings in wave without creating backorders'),
            (2, 'Move wave to "On Hold" if not all pickings are confirmed')
        ],
        string='Behavior on Confirm',
        default=0,
    )

    @api.model
    def get_default_company_picking_values(self, fields):
        company = self.env.user.company_id
        return {
            'outgoing_wave_behavior_on_confirm': company.outgoing_wave_behavior_on_confirm,
        }

    @api.multi
    def set_company_picking_values(self):
        company = self.env.user.company_id
        company.outgoing_wave_behavior_on_confirm = self.outgoing_wave_behavior_on_confirm
