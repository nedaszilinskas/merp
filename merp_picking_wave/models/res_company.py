# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from openerp import models, fields


class Company(models.Model):
    _inherit = 'res.company'

    outgoing_wave_behavior_on_confirm = fields.Selection(
        [
            (0, 'Close pickings in wave with creation of backorders '
                'for incomplete pickings'),
            (1, 'Close pickings in wave without creating backorders'),
            (2, 'Move wave to "On Hold" if not all pickings are confirmed')
        ],
        string='Behavior on Confirm', default=0)
