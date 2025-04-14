from odoo import models,fields

class Hospitalemergency(models.Model):
    _name="hospital.doctor"
    _rec_name=("name")

    name=fields.Char(string="Name")
    joining=fields.Date(string="experience")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], "Gender")

