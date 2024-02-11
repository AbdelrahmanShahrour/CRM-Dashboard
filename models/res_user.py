
from odoo import fields, models


class ResUser(models.Model):
    """ResUser model extends the base res. Users model to add a field 'sales'
    that represents the target for the salesperson."""
    _inherit = 'res.users'

    sales = fields.Float(string="Target", help="The target value for the "
                                               "salesperson.")
