from fpdf import FPDF


def axis(y,pdf):
    y += 5
    if y > 270:
        y = 10
        pdf.add_page()
        return y
    return y


pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

d = {
    'HSN/SAC': ['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    'Description': ['EC4M', 'EC6M', 'EC8MF', 'EC8MF2', 'EC4M', 'EC6M', 'EC8MF', 'EC4M', 'EC6M', 'EC8MF', 'EC8MF2', 'EC4M', 'EC6M', 'EC8MF'],
    "MRP": [14500, 17250, 21000, 21500, 14500, 17250, 21000, 14500, 17250, 21000, 21500, 14500, 17250, 21000],
    "DIS": [62, 57, 57, 57, 62, 57, 57, 62, 57, 57, 57, 62, 57, 57],
    "QTY": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
}


pdf.set_font('times', '', 10)
pdf.rect(10, 10, 95, 20)
pdf.image('voni.png', 11, 11, 15, 15)
pdf.set_xy(35, 13)
pdf.multi_cell(60, 5, text="3RD FLOOR, 4 D/10, VIJAY TOWERS COLLECTOR OFFICEROAD, Tiruchirappalli, Tamil Nadu, 62000",
               align='R')

contact = "Contact No: +91 86104 67352 / 86104 70299 ,Land Line: 0422-2966694 ,Website: www.vonismart.com"
pdf.set_xy(106, 11)
pdf.multi_cell(60, 5, contact, align='L')
pdf.rect(105, 10, 95, 15)

pdf.rect(105, 25, 95, 5)
pdf.set_xy(125, 25)
pdf.cell(30, 5, "Quotation", align='C')

pdf.rect(10, 30, 190, 5)
pdf.set_xy(11, 30)
pdf.cell(0, 5, "Customer / Consignee Name & Address")

pdf.rect(10, 35, 95, 20)
pdf.set_xy(11, 35)
pdf.multi_cell(45, 8, "Mr.Sriniwas Lokhande, Amravati, Maharashtra.")

pdf.rect(105, 35, 45, 5)
pdf.set_xy(105, 35)
pdf.cell(0, 5, "QUOTE NO", align='L')

pdf.rect(150, 35, 50, 5)
pdf.set_xy(151, 35)
pdf.cell(0, 5, "Q - 387", align='L')

pdf.rect(105, 40, 45, 5)
pdf.set_xy(106, 40)
pdf.cell(0, 5, "Date", align='L')

pdf.rect(150, 40, 50, 5)
pdf.set_xy(151, 40)
pdf.cell(0, 5, "19-Jun-23", align='L')

pdf.rect(105, 45, 45, 5)
pdf.set_xy(105, 45)
pdf.cell(0, 5, "Revision", align='L')

pdf.rect(150, 45, 50, 5)
pdf.set_xy(151, 45)
pdf.cell(0, 5, "")

pdf.rect(105, 50, 45, 5)
pdf.set_xy(106, 50)
pdf.cell(0, 5, "Date", align='L')

pdf.rect(150, 50, 50, 5)
pdf.set_xy(151, 50)
pdf.cell(0, 5, "")

pdf.rect(10, 55, 40, 5)
pdf.set_xy(11, 55)
pdf.cell(0, 5, 'Email-id')

pdf.rect(50, 55, 150, 5)
pdf.set_xy(51, 55)
pdf.cell(0, 5, '')

pdf.rect(10, 60, 40, 5)
pdf.set_xy(11, 60)
pdf.cell(0, 5, 'Contact Person/Mobile')

pdf.rect(50, 60, 150, 5)
pdf.set_xy(51, 60)
pdf.cell(0, 5, '9970170971')

y = 60
y = axis(y,pdf)
pdf.rect(10, 65, 10, 5)
pdf.set_xy(10, 65)
pdf.cell(0, 5, 'S.NO')

pdf.rect(20, 65, 30, 5)
pdf.set_xy(21, 65)
pdf.cell(0, 5, 'HSN/SAC')

pdf.rect(50, 65, 55, 5)
pdf.set_xy(51, 65)
pdf.cell(0, 5, 'Description')

pdf.rect(105, 65, 15,5)
pdf.set_xy(106, 65)
pdf.cell(0, 5, 'MRP')

pdf.rect(120, 65, 15, 5)
pdf.set_xy(121, 65)
pdf.cell(0, 5, 'Dis%')

pdf.rect(135, 65, 15,5)
pdf.set_xy(135, 65)
pdf.cell(0, 5, 'Dis.Price')

pdf.rect(150, 65, 15,5)
pdf.set_xy(151, 65)
pdf.cell(0, 5, 'QTY')

pdf.rect(165, 65, 35, 5)
pdf.set_xy(166, 65)
pdf.cell(0, 5, 'Total')

height = 170 - y
pdf.rect(10, 65, 10, height)

pdf.rect(20, 65, 30, height)

pdf.rect(50, 65, 55, height)

pdf.rect(105, 65, 15,height)

pdf.rect(120, 65, 15, height)

pdf.rect(135, 65, 15,height)

pdf.rect(150, 65, 15,height)

pdf.rect(165, 65, 35, height)

grand_total = []
for i in range(len(d['HSN/SAC'])):
    y = axis(y, pdf)
    pdf.set_xy(11, y)
    pdf.cell(0, 5, str(i + 1))

    pdf.set_xy(26, y)
    pdf.cell(0, 5, d['HSN/SAC'][i])

    pdf.set_xy(51, y)
    pdf.cell(0, 5, d['Description'][i])

    pdf.set_xy(106, y)
    pdf.cell(0, 5, str(d['MRP'][i]))

    pdf.set_xy(121, y)
    pdf.cell(0, 5, str(d['DIS'][i]))

    discount_price = round(d['MRP'][i] - (d['MRP'][i] * (d['DIS'][i] / 100)), 2)
    pdf.set_xy(136, y)
    pdf.cell(0, 5, str(discount_price))
    grand_total.append(discount_price)

    pdf.set_xy(151, y)
    pdf.cell(0, 5, str(d['QTY'][i]))

    total = d['QTY'][i] * discount_price
    pdf.set_xy(166, y)
    pdf.cell(0, 5, str(total))

y = axis(y, pdf)
y = y + (170-y)
pdf.rect(10, y, 190, 5)

y = 170
y = axis(y, pdf)
note = """
1. Switches have mobile app, and voice control options.
2. 24 Months Direct Replacement Warranty.
3. Extended warranty up to 3years applicable upon Invoice."""
pdf.set_font('times', 'BU', 10)
pdf.set_text_color(255, 0, 0)
pdf.rect(10, y, 95, 30)
pdf.set_xy(11, y)
pdf.cell(0, 5, 'Note')
pdf.set_font('times', '', 10)
pdf.set_text_color(255, 0, 0)
pdf.set_xy(11, y + 2)
pdf.multi_cell(85, 5, note)

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

pdf.rect(165, y, 35, 5)
pdf.set_xy(166, y)
pdf.cell(0, 5, str(sum(grand_total)))

y = axis(y, pdf)
pdf.set_text_color(0, 0, 0)
pdf.set_font('times', '', 10)
pdf.rect(105, y, 45, 5)
pdf.set_xy(105, y)
pdf.cell(0, 5, 'Others')

pdf.rect(150, y, 15, 5)
pdf.set_xy(151, y)
pdf.cell(0, 5, '0')

pdf.rect(165, y, 35, 5)
pdf.set_xy(166, y)
pdf.cell(0, 5, '0.00')

y = axis(y, pdf)
pdf.rect(105, y, 45, 5)
pdf.set_xy(105, y)
pdf.cell(0, 5, 'Installation')

pdf.rect(165, y, 35, 5)
pdf.set_xy(166, y)
pdf.cell(0, 5, '')

y = axis(y, pdf)
pdf.rect(105, y, 60, 5)
pdf.set_xy(105, y)
pdf.cell(0, 5, 'Grand Total')

total = sum(grand_total)
pdf.rect(165, y, 35, 5)
pdf.set_xy(166, y)
pdf.cell(0, 5, 'INR ' + str(total))

y = axis(y, pdf)
pdf.rect(105, y, 60, 5)
pdf.set_xy(106, y)
pdf.cell(0, 5, 'Round Off')

pdf.rect(165, y, 35, 5)
pdf.set_xy(166, y)
pdf.cell(0, 5, 'INR ' + str(round(total)))

y = axis(y, pdf)
pdf.set_text_color(255, 0, 0)
pdf.set_font('times', '', 10)
pdf.rect(105, y, 15, 5)
pdf.set_xy(105, y)
pdf.cell(0, 5, 'In Words')

pdf.rect(120, y, 80, 5)
pdf.set_xy(120, y)
pdf.cell(0, 5, 'Thirty-One Thousand Two Hundred Three Rupees')

y = axis(y, pdf)
pdf.set_text_color(0, 0, 0)
pdf.set_font('times', '', 10)
pdf.rect(10, y, 40, 10)
pdf.set_xy(11, y)
pdf.multi_cell(30, 5, 'OUR PAN NO AAICV1213H')

pdf.rect(50, y, 55, 10)
pdf.set_xy(51, y)
pdf.multi_cell(40, 5, 'OUR GSTIN 33AAICV1213H1ZP')

pdf.rect(105, y, 95, 5)
pdf.set_xy(106, y)
pdf.cell(0, 5, 'Terms & Conditions:')

y = axis(y, pdf)
pdf.rect(105, y, 15, 5)
pdf.set_xy(106, y)
pdf.cell(0, 5, 'Price')

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
pdf.set_xy(11, y)
pdf.cell(0, 5, 'Bank Details')
pdf.set_font('times', '', 10)
pdf.set_xy(11, y)
pdf.multi_cell(50, 5, details)

pdf.rect(105, y, 15, 5)
pdf.set_xy(106, y)
pdf.cell(0, 5, 'GST')

pdf.rect(120, y, 80, 5)
pdf.set_xy(120, y)
pdf.cell(0, 5, '18%')

y = axis(y, pdf)
pdf.rect(105, y, 15, 5)
pdf.set_xy(106, y)
pdf.cell(0, 5, 'Frieght')

pdf.rect(120, y, 80, 5)
pdf.set_xy(120, y)
pdf.cell(0, 5, 'Extra as Actual')

y = axis(y, pdf)
pdf.rect(105, y, 15, 10)
pdf.set_xy(106, y)
pdf.cell(0, 10, 'Validity')

pdf.rect(120, y, 80, 10)
pdf.set_xy(120, y)
pdf.multi_cell(78, 5,
               'Our offer is valid for 30 days from the date of this quotation and subject to the prior confirmation thereafter')

y = axis(y, pdf)
pdf.rect(105, y + 5, 15, 10)
pdf.set_xy(106, y + 5)
pdf.cell(0, 10, 'Delivery')

pdf.rect(120, y + 5, 80, 10)
pdf.set_xy(120, y + 5)
pdf.multi_cell(78, 5, 'We shall supply the items within 3 week from the receipt of your confirmed order.')

y = axis(y, pdf)
pdf.rect(105, y + 10, 15, 10)
pdf.set_xy(106, y + 10)
pdf.cell(0, 10, 'Payment')

pdf.rect(120, y + 10, 80, 10)
pdf.set_xy(120, y + 10)
pdf.cell(0, 10, '50% Advanced Payment')

y = axis(y, pdf)
pdf.rect(10, y + 15, 95, 20)
pdf.set_xy(11, y + 20)
pdf.cell(0, 10, 'THANK YOU FOR YOUR BUSINESS')

pdf.rect(105, y + 15, 25, 10)
pdf.set_xy(106, y + 15)
pdf.cell(0, 10, 'Created By')

pdf.rect(130, y + 15, 25, 10)
pdf.set_xy(131, y + 15)
pdf.cell(0, 10, 'Ashema Begam')

pdf.rect(155, y + 15, 45, 10)
pdf.set_xy(156, y + 15)
pdf.cell(0, 10, '7810021422')

y = axis(y, pdf)
pdf.rect(105, y + 20, 25, 10)
pdf.set_xy(106, y + 20)
pdf.cell(0, 10, 'Executive')

pdf.rect(130, y + 20, 25, 10)
pdf.set_xy(131, y + 20)
pdf.cell(0, 10, 'Mukesh Tiwari')

pdf.rect(155, y + 20, 45, 10)
pdf.set_xy(156, y + 20)
pdf.cell(0, 10, '7810021451')

pdf.output('pdf.pdf')
