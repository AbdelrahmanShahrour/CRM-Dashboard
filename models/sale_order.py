
from odoo import models


class SalesOrder(models.Model):
    """Extends sale order for overriding action confirm function"""
    _inherit = 'sale.order'

    def action_confirm(self):
        """Override the action_confirm method to change CRM Stage.
        Returns:
            dict: A dictionary containing the result of the original
            action_confirm method."""
        res = super(SalesOrder, self).action_confirm()
        self.opportunity_id.stage_id = self.team_id.crm_lead_state_id
        return res
