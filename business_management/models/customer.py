from odoo import models, fields, api
from odoo.osv import expression


class TaskCustomer(models.Model):
    _name = 'task.customer'
    _description = 'Customer Gst Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char("Customer", tracking=True, required=True)
    partner_id = fields.Many2one("res.partner", "Partner name")
    age = fields.Integer("Age", tracking=True, compute="compute_age_field")
    email = fields.Char("Email")
    user_id = fields.Many2one("res.users", "Users")
    company_id = fields.Many2one("res.company", "Company")
    image_1920 = fields.Binary("image")
    is_credit_note = fields.Boolean(string="Is Credit Note", compute="_compute_is_credit_note")

    def mail(self):
        for i in self:
            temp = self.env.ref("business_management.email_template")
            temp.send_mail(i.id, force_send=True)

    @api.onchange('user_id', 'partner_id')
    def _onchange_partner_id(self):
        for rec in self:
            if rec.user_id:
                rec.email = rec.user_id.email
            if rec.partner_id:
                rec.company_id = rec.partner_id.company_id

    @api.depends('partner_id')
    def compute_age_field(self):
        for rec in self:
            rec.age = rec.partner_id.age

    def _compute_is_credit_note(self):
        for i in self:
            i.is_credit_note = i.move_type == 'out_refund'

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []

        
        domain = expression.OR([
            [('name', operator, name)],
            [('email', operator, name)],
            [('partner_id.name', operator, name)],
        ])


        return self.search(expression.AND([domain, args]), limit=limit)


class Accounting(models.Model):
    _inherit="account.move"

    task_customer_id = fields.Many2one('task.customer', string="Customer Task")
