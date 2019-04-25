from openerp import models, fields


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    is_internal = fields.Boolean(
        string='Is Internal Warehouse',
    )
