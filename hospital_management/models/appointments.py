from odoo import models, fields, api
from datetime import date




class PatientAppointment(models.Model):
    _name = "hospital.patient.appointments"
    _rec_name = "patient_name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_name = fields.Many2one("res.partner", "Name", domain=[("email", "!=", False)])
    email = fields.Char(related="patient_name.email", string="email",tracking=True)
    age = fields.Integer("Age",tracking=True)
    date = fields.Date("Date")
    appointment_date = fields.Datetime("appointment date and time")
    company_id = fields.Many2one("res.company", string="Company")
    user_id = fields.Many2one("res.users")
    status = fields.Selection([("draft", "Draft"), ("confirm", "Confirmed")], "status", default="draft")
    appointment_line_id = fields.One2many("patient.appointments.line", "appointment_id", "appointment fee")



    def action_send_email(self):
        template = self.env.ref("hospital_management.mail_template_demo_patient_invoice")
        for rec in self:
            if not rec.email:
                raise ValueError("pls add partner email")
            else:
                rec.user_id = self.env.user.id
                template.send_mail(rec.id, force_send=True)

    def view_appointment(self):
        self.ensure_one()
        for rec in self:
            return {
                'name': "view patient",
                'view_mode': 'list',
                'res_model': 'hospital.patient',
                # 'domain': [('patient', '=', rec.patient_name)],
                'type': 'ir.actions.act_window',
            }


    def action_confirm(self):
        for rec in self:
            patient = self.env["hospital.patient"].search([('appointment_id', '=', rec.id)])
            if patient:
                raise ValueError("record existed")
            else:
                vals = {
                    'patient_id': rec.patient_name.id,
                    'email': rec.email,
                    'age': rec.age,
                    'appointment_date': rec.appointment_date,
                    'patient_lines': [(0, 0, {
                        'product_id': i.product.id,
                        'qty': i.qty,
                        'unit_price': i.unit_price,
                        'total': i.sub_total,

                    }) for i in rec.appointment_line_id]

                }
            self.env["hospital.patient"].create(vals)
            rec.status = "confirm"

    def action_reset_to_draft(self):
        for rec in self:
            if rec.status == "confirm":
                rec.status = "draft"


class PatientAppointmentLines(models.Model):
    _name = "patient.appointments.line"

    product_id = fields.Many2one("product.product", string="Product name", required=True)
    quantity = fields.Float(string="Qty", required=True, default=1.00)
    unit_price = fields.Float(related="product_id.lst_price", string="Unit price")
    amount_due = fields.Float(string="Due Amount")
    total = fields.Float(string="Sub Total", readonly=True, compute="compute_subtotal")
    appointment_id= fields.Many2one("hospital.patient.appointments", string="Patient", required=True)

    def compute_subtotal(self):
        for rec in self:
            rec.total = rec.quantity * rec.unit_price