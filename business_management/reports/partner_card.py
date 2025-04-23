from odoo import models, fields, api


class PartnerCardXlsx(models.AbstractModel):
    _name = 'report.business_management.report_partner_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        format1 = workbook.add_format({'font_size': 12, 'align': "left", 'bold': True})
        format2 = workbook.add_format({'font_size': 10, 'align': "left"})

        sheet = workbook.add_worksheet('Partner Report')

        row = 0
        for partner in partners:
            sheet.write(row + 0, 0, 'Partner ID', format1)
            sheet.write(row + 0, 1, partner.partner_id.name or '', format2)

            sheet.write(row + 1, 0, 'Age', format1)
            sheet.write(row + 1, 1, partner.age or '', format2)

            sheet.write(row + 2, 0, 'Email', format1)
            sheet.write(row + 2, 1, partner.email or '', format2)



