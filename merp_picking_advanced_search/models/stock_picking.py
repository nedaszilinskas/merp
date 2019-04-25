# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from openerp import models, api, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    product_id_not_moved = fields.Many2many(
        'product.product', string='Product Not Moved',
        compute='_compute_products_not_moved', related=False, store=True)

    @api.one
    @api.depends('pack_operation_ids.qty_done')
    def _compute_products_not_moved(self):
        res = self.env['product.product']
        for operation in self.pack_operation_ids:
            if operation.qty_done < operation.product_qty:
                res += operation.product_id
        self.product_id_not_moved = res
