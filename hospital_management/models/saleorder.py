from odoo import fields,models


class SaleOrder(models.Model):
    _inherit="sale.order"

    Customer_Name=fields.Char("customer name")