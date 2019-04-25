from openerp import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    default_warehouse = fields.Many2one(
        comodel_name='stock.warehouse',
    )
