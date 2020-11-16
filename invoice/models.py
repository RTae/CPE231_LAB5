from django.db import models

# Create your models here.
class Product(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100, null=True)
    units = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = "product"
        managed = False
    def __str__(self):
        return self.code

class Customer(models.Model):
    customer_code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    credit_limit = models.FloatField(null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    
    class Meta:
        db_table = "customer"
        managed = False
    def __str__(self):
        return self.customer_code

class Invoice(models.Model):
    invoice_no = models.CharField(max_length=10, primary_key=True)
    date = models.DateField(null=True)
    customer_code = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='customer_code')
    due_date = models.DateField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    vat = models.FloatField(null=True, blank=True)
    amount_due = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = "invoice"
        managed = False

class InvoiceLineItem(models.Model):
    lineitem = models.IntegerField()
    invoice_no = models.ForeignKey(Invoice, on_delete=models.CASCADE, db_column='invoice_no')
    product_code = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product', db_column='product_code')
    quantity = models.IntegerField(null=True)
    unit_price = models.FloatField(null=True)
    extended_price = models.FloatField(null=True)

    class Meta:
        db_table = "invoice_line_item"
        unique_together = (("lineitem", "invoice_no"),)
        managed = False


