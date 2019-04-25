# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from openerp import api, models, fields as odoo_fields


class StockConfigSettings(models.TransientModel):
    _inherit = 'stock.config.settings'

    outgoing_routing_strategy = odoo_fields.Selection(
        [
            ('name', 'Sort by source locations in alphabetical order'),
            ('removal_prio', 'Sort by location removal strategy priority field'),
        ],
        string='Routing Strategy', default='name')

    outgoing_routing_order = odoo_fields.Selection(
        [
            (0, 'Ascending (A-Z)'),
            (1, 'Descending (Z-A)'),
        ],
        string='Routing Order', default=0)

    routing_available_for = odoo_fields.Selection(
        [
            ('picking', 'Picking'),
        ],
        string='Routing Available For',
    )

    @api.model
    def get_default_company_outgoing_strategy_values(self, fields):
        company = self.env.user.company_id
        return {
            'outgoing_routing_strategy': company.outgoing_routing_strategy,
            'outgoing_routing_order': company.outgoing_routing_order,
        }

    @api.multi
    def set_company_outgoing_strategy_values(self):
        company = self.env.user.company_id
        company.outgoing_routing_strategy = self.outgoing_routing_strategy
        company.outgoing_routing_order = self.outgoing_routing_order

    @api.model
    def ui_get_routing_available_for(self):
        available_for = self.fields_get(['routing_available_for']) \
            .get('routing_available_for') \
            .get('selection')

        return dict(available_for).keys()
