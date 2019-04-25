# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from openerp import models, fields, api
from openerp import http

import logging
_logger = logging.getLogger(__name__)


class StockConfigSettings(models.TransientModel):
    _inherit = 'stock.config.settings'

    module_merp_outgoing_routing = fields.Boolean(
        'Add Outgoing Routing strategy options (sort locations)')

    module_merp_custom_access_rights = fields.Boolean(
        'Enable Custom Access Rights for mERP Warehouse App')

    module_merp_picking_wave = fields.Boolean('Enable Picking Wave')

    module_merp_picking_products_skip = fields.Boolean(
        'Allow smart skip of products in pickings and picking waves')

    module_merp_instant_move = fields.Boolean(
        'Allow add more items automatically via mERP Warehouse app')

    module_merp_inventory = fields.Boolean(
        'Advanced mERP Inventory Improvements')

    module_merp_custom_logotype = fields.Boolean(
        'Enable Customer Logotype')

    module_merp_internal_warehouse = fields.Boolean(
        string='Allows to select default warehouse that will be pre-selected'
        ' for user when using menu "Internal Transfer"',
    )

    @api.depends('company_id')
    def _compute_merp_version(self):
        manifest = http.addons_manifest.get('merp_base', None)
        version = manifest['version'].split('.')
        return '.'.join(version[-3:])

    merp_version = fields.Char(string='mERP Version',
        compute='_compute_merp_version', store=False,
        default=lambda self: self._compute_merp_version())
