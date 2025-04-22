from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date
import re


class ResPartner(models.Model):
    _inherit = 'res.partner'

    gst_number = fields.Char(string='GST Number')
    dob = fields.Date("Date of Birth")
    age = fields.Integer(string="Age", compute="_compute_age", store=True)

    @api.depends('dob')
    def _compute_age(self):
        for rec in self:
            if rec.dob:
                today = date.today()
                dob=rec.dob
                rec.age = today.year - rec.dob.year - (
                        (today.month, today.day) < (rec.dob.month, rec.dob.day))
            else:
                rec.age = 0

    @api.constrains('gst_number')
    def _check_gst_number(self):
        gst_pattern = r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$'

        for partner in self:
            if partner.gst_number:
                gst = partner.gst_number.strip().upper()
                if len(gst) != 15 or not re.match(gst_pattern, gst):
                    raise ValidationError(
                        "Invalid GST Number. It must be 15 characters and follow the standard format.")


