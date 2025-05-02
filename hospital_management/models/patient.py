from odoo import models,fields,api
from datetime import date
from odoo.exceptions import ValidationError
import re




class Hospitalpatient(models.Model):
    _name="hospital.patient"
    _rec_name ="patient_id"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char("patient sequence", default="New")
    patient_id = fields.Many2one(comodel_name="res.partner", string="Name", tracking=True, required=True, )
    doctor_names = fields.Many2many(comodel_name="hospital.doctor", string="Doctors")


    user_id = fields.Many2one("res.users", "user", compute="compute_user_company")
    company_id = fields.Many2one("res.company", "Company", compute="compute_user_company")

    age=fields.Integer(string="Age")
    gender=fields.Char(string="Gender")
    email = fields.Char("Email",compute="compute_patient_email")
    doctor_id = fields.Many2one(comodel_name='hospital.doctor',  string='Doctor_Id')
    patient_lines = fields.One2many("hospital.patient.line", "patient", "Order lines")
    is_patient_in_ward=fields.Boolean("is patient in ward")
    admit_date=fields.Date("Admit date")
    discharge_date=fields.Date("discharge date")
    status = fields.Selection([("admit", "Admitted"), ("discharge", "Discharged")], "status", default='admit',compute='status_date')
    image_1920 = fields.Binary("image")
    appointment_id= fields.Many2one('hospital.patient.appointments', string="Appointment")
    appointment_date = fields.Datetime("Appointment Date", related='appointment_id.appointment_date', store=True)


    @api.onchange('patient_id')
    def onchange_patient_name(self):
         for rec in self:
                print(rec)
                rec.email = rec.patient_id.email

    def compute_patient_email(self):
     for rec in self:
         rec.email = rec.patient_id.email

    def compute_user_company(self):
        for rec in self:
            rec.user_id = self.env.user
            rec.company_id = self.env.user.company_id.id

    def send_email(self):
        for rec in self:
            template = self.env.ref("hospital_management.mail_template_patient_confirm")
            template.send_mail(rec.id, force_send=True)

    def create(self, vals):
        vals["user_id"] = self.env.user.id
        vals["company_id"] = self.env.user.company_id.id
        vals["name"] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(Hospitalpatient, self).create(vals)



    def status_date(self):
        today=date.today()
        for i in self:
            if i.discharge_date and today > i.discharge_date:
                i.status = 'discharge'
            else:
                i.status = 'admit'

    def view_patient_lines(self):
        self.ensure_one()
        return {
            'name': "view patient invoices",
            'view_mode': 'list',
            'res_model': 'hospital.patient.line',
            'domain': [('patient', '=', self.id)],
            'type': 'ir.actions.act_window',
        }
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





