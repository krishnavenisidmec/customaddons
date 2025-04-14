from odoo import models,fields,api


class Hospitalpatient(models.Model):
    _name="hospital.patient"
    _rec_name ="patient_id"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_id = fields.Many2one(comodel_name="res.partner", string="Name", tracking=True, required=True, )


    age=fields.Integer(string="Age")
    gender=fields.Char(string="Gender")
    email = fields.Char("Email",compute="compute_patient_email")
    doctor_id = fields.Many2one(comodel_name='hospital.doctor',  string='Doctor_Id')
    patient_lines = fields.One2many("hospital.patient.line", "patient", "Order lines")



    @api.onchange('patient_id')
    def onchange_patient_name(self):
         for rec in self:
                print(rec)
                rec.email = rec.patient_id.email

    def compute_patient_email(self):
        for rec in self:
            rec.email=rec.patient_id.email




class HospitalpatientLines(models.Model):
    _name="hospital.patient.line"


    product_id=fields.Many2one("product.product","product Name")
    quantity=fields.Integer("qty")
    unit_price=fields.Float("Unitprice")
    patient=fields.Many2one("hospital.patient","Patient")
    total = fields.Integer("subtotal",compute="compute_sub_total")


    def compute_sub_total(self):
        for rec in self:
            rec.total=rec.quantity * rec.unit_price







