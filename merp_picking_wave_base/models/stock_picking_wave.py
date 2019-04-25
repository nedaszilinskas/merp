# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from openerp import models, fields, api, exceptions, _


class PickingWave(models.Model):
    _inherit = 'stock.picking.wave'

    related_pack_operations = fields.Many2many(
        'stock.pack.operation', relation='wave_pack_operations',
        string='Operations',
        compute='_compute_related_pack_operations', store=True)

    operations_to_pick = fields.Many2many(
        'stock.pack.operation', relation='wave_operations_to_pick',
        string='Operations to Pick',
        compute='_compute_operations_to_pick', store=False)

    strategy_order_r = fields.Char(string='Strategy Order',
        compute='_compute_operations_to_pick', store=False)

    @api.one
    @api.depends('picking_ids', 'picking_ids.pack_operation_ids')
    def _compute_related_pack_operations(self):
        res = self.env['stock.pack.operation']
        for picking in self.picking_ids:
            for operation in picking.pack_operation_ids:
                res += operation
        self.related_pack_operations = res

    @api.one
    @api.depends('picking_ids',
                 'picking_ids.pack_operation_ids',
                 'picking_ids.pack_operation_ids.location_id',
                 'picking_ids.pack_operation_ids.qty_done')
    def _compute_operations_to_pick(self):
        strategy = self.env.user.company_id.outgoing_routing_strategy
        strategy_order = self.env.user.company_id.outgoing_routing_order
        res = self.env['stock.pack.operation']
        for picking in self.picking_ids:
            res += picking.operations_to_pick
        self.operations_to_pick = res.sorted(
            key=lambda r: getattr(r.location_id, strategy, 'None'),
            reverse=strategy_order
        )

        settings = self.env['res.company'].fields_get(
            ['outgoing_routing_strategy', 'outgoing_routing_order'])
        strategies = settings['outgoing_routing_strategy']['selection']
        orders = settings['outgoing_routing_order']['selection']
        self.strategy_order_r = _('Strategy Order: ') + ', '.join([
            dict(strategies)[strategy].lower(),
            dict(orders)[strategy_order].lower()
        ])
