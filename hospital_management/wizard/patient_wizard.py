from odoo import fields, models, _


class PatientReport(models.TransientModel):
    _name = 'patient.invoices.wizard'
    _description = 'patient invoices report'

    patient_id = fields.Many2one("res.partner", "Patient")
    admit_date = fields.Date("Admit Date")
    discharge_date = fields.Date("Discharge Date")

    def view_pdf_report(self):
        return self.env.ref('hospital_management.report_patient_pdf').report_action(self)