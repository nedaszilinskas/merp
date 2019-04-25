# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from openerp import api, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def sort_printer_picking_list(self, pack_operation_ids):
        """ sort list of pack operations by configured field
        """
        strategy = self.env.user.company_id.outgoing_routing_strategy
        strategy_order = self.env.user.company_id.outgoing_routing_order

        return pack_operation_ids.sorted(
            key=lambda r: getattr(r.location_id, strategy, 'None'),
            reverse=strategy_order
        )
