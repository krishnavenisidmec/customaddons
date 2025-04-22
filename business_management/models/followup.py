from odoo import models,fields,api
from datetime import date


class Customerfollowup(models.Model):
    _name='customer.followup'

    salesperson_id = fields.Many2one('res.users', string='Salesperson')
    followup_date=fields.Date('Follow-up-date')

    @api.model
    def default_get(self, fields_list):
        res = super(Customerfollowup, self).default_get(fields_list)
        res['salesperson_id'] = self.env.user.id
        res['followup_date'] = date.today()
        return res