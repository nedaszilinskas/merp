# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from openerp import models, fields, api


class StockPackOperation(models.Model):
    _inherit = 'stock.pack.operation'

    skipped = fields.Boolean(
        string='Skipped',
        help='Products is skipped in pickings and picking waves',
    )

    @api.model
    def _compute_operation_valid(self):
        res = True
        if hasattr(super(StockPackOperation, self), '_compute_operation_valid'):
            res &= super(StockPackOperation, self)._compute_operation_valid()
        return res and not self.skipped
