from odoo import fields,models,api
from datetime import datetime
from odoo.exceptions import UserError







class SaleOrder(models.Model):
    _inherit="sale.order"

    Customer_code=fields.Char("customer code")

    @api.model
    def create(self, vals):
        if not vals.get('Customer_code'):
            year = datetime.now().year
            prefix = f'CUST/{year}/'

            last_order = self.search([
                ('Customer_code', 'like', f'{prefix}%')
            ], order='Customer_code desc', limit=1)

            if last_order and last_order.Customer_code:
                try:
                    last_number = int(last_order.Customer_code.split('/')[-1])
                except (IndexError, ValueError):
                    last_number = 0
            else:
                last_number = 0

            next_number = str(last_number + 1).zfill(4)
            vals['Customer_code'] = f'{prefix}{next_number}'

        return super().create(vals)

    def unlink(self):
        for order in self:
            if order.state not in ["draft", "cancel"]:
                raise UserError(("You are not allowed to delete any sale order"))
            return super(SaleOrder, self).unlink()