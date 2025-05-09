{
    'name': 'Business management',
    'version': '1.0',
    'author': 'krishnaveni',
    "depends": ["base","account", "sale","mail","report_xlsx"],
    'data': [
        'security/ir.model.access.csv',
        'data/ir.sequence.xml',
        'views/res_partner.xml',
        'views/view_saleorder.xml',
        'views/shipment.xml',
        'views/customer.xml',
        'reports/report_partner_template.xml',
        'reports/report.xml',
        'reports/sale_wizard_report.xml',
        'reports/sale_wizard_template.xml',
        'wizards/partner_wizard.xml',
        'wizards/sale_order_wizard.xml',
        'data/mail_template.xml',
        'views/followup.xml',
        'views/menu.xml',
    ],
}
