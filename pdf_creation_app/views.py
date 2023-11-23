from django.shortcuts import render
from .serializer import *
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from fpdf import FPDF
from datetime import datetime
from num2words import num2words


def axis(y, pdf):
    y += 5
    if y > 270:
        y = 10
        pdf.add_page()
        return y
    return y


class PdfCreation(CreateAPIView):
    serializer_class = Cus

    def post(self, request, *args, **kwargs):
        serializer = Cus(data=request.data)
        if serializer.is_valid():
            pdf = FPDF('P', 'mm', 'A4')
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            serializer.save()
            address = serializer.validated_data['cus_address']
            email = serializer.validated_data['email']
            phone_number = serializer.validated_data['phone_number']
            product = serializer.validated_data['product']
            mrp = serializer.validated_data['mrp']
            discount = serializer.validated_data['discount']
            qty = serializer.validated_data['qty']
            gst = serializer.validated_data['gst']
            sgst = serializer.validated_data['sgst']
            cgst = serializer.validated_data['cgst']
            emp_name = serializer.validated_data['emp_name']
            emp_number = serializer.validated_data['emp_number']
            executive_name = serializer.validated_data['executive_name']
            executive_number = serializer.validated_data['executive_number']
            company_name = 'voni'

            pdf = FPDF('P', 'mm', 'A4')
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)

            pdf.set_font('times', '', 10)
            pdf.rect(10, 10, 95, 20)
            pdf.image(r'C:\Users\Vrdella\Desktop\pdf_creation\pdf_creation_project\pdf_creation_app\voni.png', 11, 11, 15, 15)
            pdf.set_xy(35, 13)
            pdf.multi_cell(60, 5,txt="3RD FLOOR, 4 D/10, VIJAY TOWERS COLLECTOR OFFICEROAD, Tiruchirappalli, Tamil Nadu, 62000",align='R')

            contact = "Contact No: +91 86104 67352 / 86104 70299 ,Land Line: 0422-2966694 ,Website: www.vonismart.com"
            pdf.set_font('times', '', 10)
            pdf.set_xy(106, 11)
            pdf.multi_cell(60, 5, contact, align='L')
            pdf.rect(105, 10, 95, 15)

            pdf.set_font('times', '', 12)
            pdf.rect(105, 25, 95, 5)
            pdf.set_xy(125, 25)
            pdf.cell(30, 5, "Quotation", align='C')

            pdf.set_font('times', '', 10)
            pdf.rect(10, 30, 190, 5)
            pdf.set_xy(11, 30)
            pdf.cell(0, 5, "Customer / Consignee Name & Address")

            pdf.set_font('times', '', 10)
            pdf.rect(10, 35, 95, 20)
            pdf.set_xy(11, 35)
            pdf.multi_cell(45, 8, address)

            pdf.set_font('times', '', 10)
            pdf.rect(105, 35, 45, 5)
            pdf.set_xy(105, 35)
            pdf.cell(0, 5, "QUOTE NO", align='L')

            pdf.set_font('times', '', 10)
            pdf.rect(150, 35, 50, 5)
            pdf.set_xy(151, 35)
            pdf.cell(0, 5, "Q - 128", align='L')

            pdf.set_font('times', '', 10)
            pdf.rect(105, 40, 45, 5)
            pdf.set_xy(106, 40)
            pdf.cell(0, 5, "Date", align='L')

            date = datetime.now().date()
            pdf.set_font('times', '', 10)
            pdf.rect(150, 40, 50, 5)
            pdf.set_xy(151, 40)
            pdf.cell(0, 5, str(date), align='L')

            pdf.set_font('times', '', 10)
            pdf.rect(105, 45, 45, 5)
            pdf.set_xy(105, 45)
            pdf.cell(0, 5, "Revision", align='L')

            pdf.set_font('times', '', 10)
            pdf.rect(150, 45, 50, 5)
            pdf.set_xy(151, 45)
            pdf.cell(0, 5, "")

            pdf.set_font('times', '', 10)
            pdf.rect(105, 50, 45, 5)
            pdf.set_xy(106, 50)
            pdf.cell(0, 5, "Date", align='L')

            pdf.set_font('times', '', 10)
            pdf.rect(150, 50, 50, 5)
            pdf.set_xy(151, 50)
            pdf.cell(0, 5, "")

            pdf.set_font('times', '', 10)
            pdf.rect(10, 55, 40, 5)
            pdf.set_xy(11, 55)
            pdf.cell(0, 5, 'Email-id')

            pdf.set_font('times', '', 10)
            pdf.rect(50, 55, 150, 5)
            pdf.set_xy(51, 55)
            pdf.cell(0, 5, str(email))

            pdf.set_font('times', '', 10)
            pdf.rect(10, 60, 40, 5)
            pdf.set_xy(11, 60)
            pdf.cell(0, 5, 'Contact Person/Mobile')

            pdf.set_font('times', '', 10)
            pdf.rect(50, 60, 150, 5)
            pdf.set_xy(51, 60)
            pdf.cell(0, 5, str(phone_number))

            pdf.set_font('times', '', 10)
            pdf.rect(10, 65, 10, 5)
            pdf.set_xy(10, 65)
            pdf.cell(0, 5, 'S.NO')

            pdf.set_font('times', '', 10)
            pdf.rect(20, 65, 30, 5)
            pdf.set_xy(21, 65)
            pdf.cell(0, 5, 'HSN/SAC')

            pdf.set_font('times', '', 10)
            pdf.rect(50, 65, 55, 5)
            pdf.set_xy(51, 65)
            pdf.cell(0, 5, 'Description')

            pdf.set_font('times', '', 10)
            pdf.rect(105, 65, 15, 5)
            pdf.set_xy(106, 65)
            pdf.cell(0, 5, 'MRP')

            pdf.set_font('times', '', 10)
            pdf.rect(120, 65, 15, 5)
            pdf.set_xy(121, 65)
            pdf.cell(0, 5, 'Dis%')

            pdf.set_font('times', '', 10)
            pdf.rect(135, 65, 15, 5)
            pdf.set_xy(135, 65)
            pdf.cell(0, 5, 'Dis.Price')

            pdf.set_font('times', '', 10)
            pdf.rect(150, 65, 15, 5)
            pdf.set_xy(151, 65)
            pdf.cell(0, 5, 'QTY')

            pdf.set_font('times', '', 10)
            pdf.rect(165, 65, 35, 5)
            pdf.set_xy(166, 65)
            pdf.cell(0, 5, 'Total')
            y = 65
            d = {
                'HSN/SAC': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                'Description': ['EC4M', 'EC6M', 'EC8MF', 'EC8MF2', 'EC4M', 'EC6M', 'EC8MF', 'EC8MF2', 'EC4M', 'EC6M',
                                'EC8MF', 'EC8MF2', 'EC4M', 'EC6M', 'EC8MF', 'EC8MF2'],
                "MRP": [14500, 17250, 21000, 21500, 14500, 17250, 21000, 21500, 14500, 17250, 21000, 21500, 14500,
                        17250, 21000, 21500],
                "DIS": [62, 57, 57, 57, 62, 57, 57, 57, 62, 57, 57, 57, 62, 57, 57, 57],
                "QTY": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            }
            grand_total = []
            for i in range(len(d['HSN/SAC'])):
                y = axis(y, pdf)
                pdf.set_font('times', '', 10)
                pdf.rect(10, y, 10, 5)
                pdf.set_xy(11, y)
                pdf.cell(0, 5, str(i + 1))

                pdf.set_font('times', '', 10)
                pdf.rect(20, y, 30, 5)
                pdf.set_xy(26, y)
                pdf.cell(0, 5, d['HSN/SAC'][i])

                pdf.set_font('times', '', 10)
                pdf.rect(50, y, 55, 5)
                pdf.set_xy(51, y)
                pdf.cell(0, 5, d['Description'][i])

                pdf.set_font('times', '', 10)
                pdf.rect(105, y, 15, 5)
                pdf.set_xy(106, y)
                pdf.cell(0, 5, str(d['MRP'][i]))

                pdf.set_font('times', '', 10)
                pdf.rect(120, y, 15, 5)
                pdf.set_xy(121, y)
                pdf.cell(0, 5, str(d['DIS'][i]))

                discount_price = round(d['MRP'][i] - (d['MRP'][i] * (d['DIS'][i] / 100)), 2)
                pdf.set_font('times', '', 10)
                pdf.rect(135, y, 15, 5)
                pdf.set_xy(136, y)
                pdf.cell(0, 5, str(discount_price))
                grand_total.append(discount_price)

                pdf.set_font('times', '', 10)
                pdf.rect(150, y, 15, 5)
                pdf.set_xy(151, y)
                pdf.cell(0, 5, str(d['QTY'][i]))

                total = d['QTY'][i] * discount_price
                pdf.set_font('times', '', 10)
                pdf.rect(165, y, 35, 5)
                pdf.set_xy(166, y)
                pdf.cell(0, 5, str(total))

            y = axis(y, pdf)
            pdf.set_font('times', '', 10)
            pdf.rect(10, y, 190, 5)

            y = axis(y, pdf)
            note = """
            1. Switches have mobile app, and voice control options.
            2. 24 Months Direct Replacement Warranty.
            3. Extended warranty up to 3years applicable upon Invoice.
            """
            pdf.set_font('times', 'BU', 10)
            pdf.set_text_color(255, 0, 0)
            pdf.rect(10, y, 95, 30)
            pdf.set_xy(10, y)
            pdf.cell(0, 5, 'Note')
            pdf.set_font('times', '', 10)
            pdf.set_text_color(255, 0, 0)
            pdf.set_xy(10, y)
            pdf.multi_cell(90, 5, note)

            pdf.set_text_color(0, 0, 0)
            pdf.set_font('times', '', 10)
            pdf.rect(105, y, 45, 5)
            pdf.set_xy(105, y)
            pdf.cell(0, 5, 'Sub_Total')

            pdf.set_text_color(255, 0, 0)
            pdf.set_font('times', '', 10)
            pdf.rect(150, y, 15, 5)
            pdf.set_xy(151, y)
            pdf.cell(0, 5, '4')

            pdf.set_font('times', '', 10)
            pdf.rect(165, y, 35, 5)
            pdf.set_xy(166, y)
            pdf.cell(0, 5, str(sum(grand_total)))

            y = axis(y, pdf)
            pdf.set_text_color(0, 0, 0)
            pdf.set_font('times', '', 10)
            pdf.rect(105, y, 45, 5)
            pdf.set_xy(105, y)
            pdf.cell(0, 5, 'Others')

            pdf.set_font('times', '', 10)
            pdf.rect(150, y, 15, 5)
            pdf.set_xy(151, y)
            pdf.cell(0, 5, '0')

            pdf.set_font('times', '', 10)
            pdf.rect(165, y, 35, 5)
            pdf.set_xy(166, y)
            pdf.cell(0, 5, '0.00')

            if company_name == 'voni':
                y = axis(y, pdf)
                pdf.set_font('times', '', 10)
                pdf.rect(105, y, 45, 5)
                pdf.set_xy(105, y)
                pdf.cell(0, 5, 'Installation')

            elif company_name == 'vrihodha':
                y = axis(y, pdf)
                pdf.set_font('times', '', 10)
                pdf.rect(105, y, 45, 5)
                pdf.set_xy(105, y)
                pdf.cell(0, 5, 'Transport')

            pdf.set_font('times', '', 10)
            pdf.rect(165, y, 35, 5)
            pdf.set_xy(166, y)
            pdf.cell(0, 5, '')

            y = axis(y, pdf)
            pdf.set_font('times', '', 10)
            pdf.rect(105, y, 60, 5)
            pdf.set_xy(105, y)
            pdf.cell(0, 5, 'Grand Total')

            total = sum(grand_total)
            pdf.set_font('times', '', 10)
            pdf.rect(165, y, 35, 5)
            pdf.set_xy(166, y)
            pdf.cell(0, 5, 'INR ' + str(total))

            y = axis(y, pdf)
            pdf.set_font('times', '', 10)
            pdf.rect(105, y, 60, 5)
            pdf.set_xy(106, y)
            pdf.cell(0, 5, 'Round Off')

            pdf.set_font('times', '', 10)
            pdf.rect(165, y, 35, 5)
            pdf.set_xy(166, y)
            pdf.cell(0, 5, 'INR ' + str(round(total)))

            y = axis(y, pdf)
            pdf.set_text_color(255, 0, 0)
            pdf.set_font('times', '', 10)
            pdf.rect(105, y, 15, 5)
            pdf.set_xy(105, y)
            pdf.cell(0, 5, 'In Words')

            pdf.set_text_color(255, 0, 0)
            pdf.set_font('times', '', 8)
            pdf.rect(120, y, 80, 5)
            pdf.set_xy(120, y)
            pdf.cell(0, 5, num2words(round(total)))

            y = axis(y, pdf)
            pdf.set_text_color(0, 0, 0)
            pdf.set_font('times', '', 10)
            pdf.rect(10, y, 40, 10)
            pdf.set_xy(11, y)
            pdf.cell(0, 5, 'OUR PAN_NO ')
            pdf.set_xy(11, y+4)
            pdf.cell(0,5,'AAICV1213H')

            pdf.set_font('times', '', 10)
            pdf.rect(50, y, 55, 10)
            pdf.set_xy(51, y)
            pdf.cell(0, 5, 'OUR GSTIN')
            pdf.set_xy(51, y+4)
            pdf.cell(0, 5, '33AAICV1213H1ZP')

            pdf.set_font('times', '', 10)
            pdf.rect(105, y, 95, 5)
            pdf.set_xy(106, y)
            pdf.cell(0, 5, 'Terms & Conditions:')

            y = axis(y, pdf)
            pdf.set_font('times', '', 10)
            pdf.rect(105, y, 15, 5)
            pdf.set_xy(106, y)
            pdf.cell(0, 5, 'Price')

            pdf.set_font('times', '', 10)
            pdf.rect(120, y, 80, 10)
            pdf.set_xy(120, y)
            pdf.cell(0, 5, 'Ex-GoDown-COIMBATORE')

            y = axis(y, pdf)
            details = """
            Name : VONI SMARTIOT
            Bank : HDFC Bank
            A/C No : 50200057594221
            IFSC : HDFC0002086
            Branch : Thiruverumbur Branch"""
            pdf.set_font('times', 'BU', 10)
            pdf.rect(10, y, 95, 40)
            pdf.set_xy(10, y)
            pdf.cell(0, 5, 'Bank Details')
            pdf.set_font('times', '', 10)
            pdf.set_xy(10, y)
            pdf.multi_cell(60, 5, details)

            pdf.set_font('times', '', 10)
            pdf.rect(105, y, 15, 5)
            pdf.set_xy(106, y)
            pdf.cell(0, 5, 'GST')

            pdf.set_font('times', '', 10)
            pdf.rect(120, y, 80, 5)
            pdf.set_xy(120, y)
            pdf.cell(0, 5, str(gst)+"%")

            if sgst == '' or sgst is None:
                pass
            else:
                pdf.set_font('times', '', 10)
                pdf.rect(135, y, 15, 5)
                pdf.set_xy(136, y)
                pdf.cell(0, 5, 'SGST')

                pdf.set_font('times', '', 10)
                pdf.rect(150, y, 15, 5)
                pdf.set_xy(151, y)
                pdf.cell(0, 5, str(sgst)+"%")

            if cgst == '' or cgst is None:
                pass
            else:
                pdf.set_font('times', '', 10)
                pdf.rect(165, y, 15, 5)
                pdf.set_xy(166, y)
                pdf.cell(0, 5, 'CGST')

                pdf.set_font('times', '', 10)
                pdf.rect(180, y, 20, 5)
                pdf.set_xy(181, y)
                pdf.cell(0, 5, str(cgst)+"%")

            y = axis(y, pdf)
            pdf.set_font('times', '', 10)
            pdf.rect(105, y, 15, 5)
            pdf.set_xy(106, y)
            pdf.cell(0, 5, 'Frieght')

            pdf.set_font('times', '', 10)
            pdf.rect(120, y, 80, 5)
            pdf.set_xy(120, y)
            pdf.cell(0, 5, 'Extra as Actual')

            y = axis(y, pdf)
            pdf.set_font('times', '', 10)
            pdf.rect(105, y, 15, 10)
            pdf.set_xy(106, y)
            pdf.cell(0, 10, 'Validity')

            pdf.set_font('times', '', 8)
            pdf.rect(120, y, 80, 10)
            pdf.set_xy(120, y)
            pdf.multi_cell(78, 5,
                           'Our offer is valid for 30 days from the date of this quotation and subject to the prior confirmation thereafter')

            y = axis(y, pdf)
            pdf.set_font('times', '', 10)
            pdf.rect(105, y + 5, 15, 10)
            pdf.set_xy(106, y + 5)
            pdf.cell(0, 10, 'Delivery')

            pdf.set_font('times', '', 8)
            pdf.rect(120, y + 5, 80, 10)
            pdf.set_xy(120, y + 5)
            pdf.multi_cell(78, 5, 'We shall supply the items within 3 week from the receipt of your confirmed order.')

            y = axis(y, pdf)
            pdf.set_font('times', '', 10)
            pdf.rect(105, y + 10, 15, 10)
            pdf.set_xy(106, y + 10)
            pdf.cell(0, 10, 'Payment')

            pdf.set_font('times', '', 10)
            pdf.rect(120, y + 10, 80, 10)
            pdf.set_xy(120, y + 10)
            pdf.cell(0, 10, '50% Advanced Payment')

            y = axis(y, pdf)
            pdf.set_font('times', '', 10)
            pdf.rect(10, y + 15, 95, 20)
            pdf.set_xy(11, y + 20)
            pdf.cell(0, 10, 'THANK YOU FOR YOUR BUSINESS')

            pdf.set_font('times', '', 10)
            pdf.rect(105, y + 15, 25, 10)
            pdf.set_xy(106, y + 15)
            pdf.cell(0, 10, 'Created By')

            pdf.set_font('times', '', 10)
            pdf.rect(130, y + 15, 25, 10)
            pdf.set_xy(131, y + 15)
            pdf.cell(0, 10, emp_name)

            pdf.set_font('times', '', 10)
            pdf.rect(155, y + 15, 45, 10)
            pdf.set_xy(156, y + 15)
            pdf.cell(0, 10, str(emp_number))

            y = axis(y, pdf)
            pdf.set_font('times', '', 10)
            pdf.rect(105, y + 20, 25, 10)
            pdf.set_xy(106, y + 20)
            pdf.cell(0, 10, 'Executive')

            pdf.set_font('times', '', 10)
            pdf.rect(130, y + 20, 25, 10)
            pdf.set_xy(131, y + 20)
            pdf.cell(0, 10, executive_name)

            pdf.set_font('times', '', 10)
            pdf.rect(155, y + 20, 45, 10)
            pdf.set_xy(156, y + 20)
            pdf.cell(0, 10, executive_number)

            pdf.output('pdf.pdf')

            return Response({'status': 'success',
                             'response_code': status.HTTP_200_OK})
        else:
            return Response({'status': 'Failed',
                             'response_code': status.HTTP_400_BAD_REQUEST})
