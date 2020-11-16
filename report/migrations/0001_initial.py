# Generated by Django 3.1.2 on 2020-10-18 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('units', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('credit_limit', models.FloatField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('key', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('date', models.DateField(null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('vat', models.FloatField(blank=True, null=True)),
                ('amount_due', models.FloatField(blank=True, null=True)),
                ('customer_code', models.ForeignKey(db_column='customer_code', on_delete=django.db.models.deletion.CASCADE, to='report.customer')),
            ],
            options={
                'db_table': 'invoice',
            },
        ),
        migrations.CreateModel(
            name='InvoiceLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lineitem', models.IntegerField()),
                ('quantity', models.IntegerField(null=True)),
                ('unit_price', models.FloatField(null=True)),
                ('extended_price', models.FloatField(null=True)),
                ('invoice_no', models.ForeignKey(db_column='invoice_no', on_delete=django.db.models.deletion.CASCADE, to='report.invoice')),
                ('product_code', models.ForeignKey(db_column='product_code', on_delete=django.db.models.deletion.CASCADE, related_name='product', to='report.product')),
            ],
            options={
                'db_table': 'invoice_line_item',
                'unique_together': {('lineitem', 'invoice_no')},
            },
        ),
    ]
