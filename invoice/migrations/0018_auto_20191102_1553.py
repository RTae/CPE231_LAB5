# Generated by Django 2.2.2 on 2019-11-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0017_auto_20191102_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='amount_due',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='vat',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
