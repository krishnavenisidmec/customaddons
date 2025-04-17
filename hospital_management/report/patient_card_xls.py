from odoo import models, fields, api


class PatientCardXlsx(models.AbstractModel):
    _name = 'report.hospital_management.report_patient_report_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, patients):
        format1 = workbook.add_format({'font_size': 12, 'align': "left", 'bold': True})
        format2 = workbook.add_format({'font_size': 10, 'align': "left"})

        sheet = workbook.add_worksheet('Patient Report')

        row = 0
        for patient in patients:
            sheet.write(row + 0, 0, 'Patient ID', format1)
            sheet.write(row + 0, 1, patient.patient_id.name or '', format2)

            sheet.write(row + 1, 0, 'Age', format1)
            sheet.write(row + 1, 1, patient.age or '', format2)

            sheet.write(row + 2, 0, 'Admit Date', format1)
            sheet.write(row + 2, 1, str(patient.admit_date) or '', format2)

            sheet.write(row + 3, 0, 'Discharge Date', format1)
            sheet.write(row + 3, 1, str(patient.discharge_date) or '', format2)


            doctor_names = ', '.join(doctor.name for doctor in patient.doctor_names)
            sheet.write(row + 4, 0, 'Doctor Names', format1)
            sheet.write(row + 4, 1, doctor_names if doctor_names else 'No doctors assigned', format2)

