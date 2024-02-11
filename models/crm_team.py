
from odoo import fields, models


class CRMSalesTeam(models.Model):
    """CRMSalesTeam model extends the base crm.team model to add a field,
    crm_lead_state_id, which represents the default CRM Lead stage for
    leads associated with this sales team.
   """
    _inherit = 'crm.team'

    crm_lead_state_id = fields.Many2one("crm.stage", string="CRM Lead",
                                        store=True,
                                        help="CRM Lead stage for leads "
                                             "associated with this sales team.")
