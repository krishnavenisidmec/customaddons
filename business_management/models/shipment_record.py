from odoo import models,fields,api


class ShipmentRecord(models.Model):
    _name = 'shipment.record'
    _description = 'Shipment Record'

    name = fields.Char("Shipment Reference", required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ], default='draft', string="Status")
