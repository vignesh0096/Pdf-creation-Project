from django.db import models


class Customerdetails(models.Model):
    cus_address = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.BigIntegerField(blank=True, null=True)
    product = models.CharField(max_length=100, blank=True, null=True)
    mrp = models.IntegerField(db_column='MRP', blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(max_length=100, blank=True, null=True)
    qty = models.CharField(db_column='QTY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gst = models.IntegerField(db_column='GST', blank=True, null=True)  # Field name made lowercase.
    sgst = models.IntegerField(db_column='SGST', blank=True, null=True)  # Field name made lowercase.
    cgst = models.IntegerField(db_column='CGST', blank=True, null=True)  # Field name made lowercase.
    emp_name = models.CharField(db_column='Emp_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emp_number = models.PositiveBigIntegerField(db_column='Emp_Number', blank=True, null=True)  # Field name made lowercase.
    executive_name = models.CharField(db_column='Executive_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    executive_number = models.CharField(db_column='Executive_number', max_length=100, blank=True, null=True)  # Field name made lowercase.
    quote_no = models.AutoField(db_column='Quote_no', primary_key=True)

    class Meta:
        managed = False
        db_table = 'customerdetails'

