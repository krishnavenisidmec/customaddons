from odoo import models,fields,api
from datetime import datetime
from odoo.exceptions import ValidationError,UserError



class Shipmentdocument(models.Model):
    _name='shipment.document'

    name=fields.Char("document reference",required=True, copy=False, readonly=True, default='New')
    description=fields.Text("Description")
    file = fields.Binary("Upload PDF", required=True)
    file_name = fields.Char("File Name")
    document_status = fields.Selection([("pending", "Pending"), ("completed", "Completed")], "status",
                                       default='pending', compute="status_update")


    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            current_year = datetime.now().year
            seq = self.env['ir.sequence'].next_by_code('shipment.document') or '/'
            vals['name'] = f'DOC/{current_year}/{seq[-4:]}'
        return super(Shipmentdocument, self).create(vals)

    @api.constrains('file_name')
    def _check_pdf_file_type(self):
        for rec in self:
            if rec.file_name and not rec.file_name.lower().endswith('.pdf'):
                raise ValidationError("Only PDF files are allowed.")

    def status_update(self):
        for res in self:
            if res.file:
                res.document_status = "completed"
            else:
                res.document_status = "pending"

    def unlink(self):
        for rec in self:
            if rec.document_status == 'completed':
                raise ValidationError("Cannot delete documents for completed shipments.")
        return super().unlink()
