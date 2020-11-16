# Generated by Django 3.1.2 on 2020-10-25 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0018_auto_20191102_1553'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='invoice',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='invoicelineitem',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'managed': False},
        ),
        migrations.RemoveField(
            model_name='invoicelineitem',
            name='id',
        ),
        migrations.AlterField(
            model_name='invoicelineitem',
            name='invoice_no',
            field=models.OneToOneField(db_column='invoice_no', on_delete=django.db.models.deletion.DO_NOTHING, to='invoice.invoice'),
        ),
        migrations.AlterField(
            model_name='invoicelineitem',
            name='lineitem',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='invoicelineitem',
            name='product_code',
            field=models.ForeignKey(db_column='product_code', on_delete=django.db.models.deletion.DO_NOTHING, related_name='product', to='invoice.product'),
        ),
        migrations.AlterModelTable(
            name='invoicelineitem',
            table='invoice_line_item',
        ),
    ]
