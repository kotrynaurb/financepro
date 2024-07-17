# Generated by Django 4.2.13 on 2024-06-06 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeapp', '0016_appreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='billing_date',
        ),
        migrations.AddField(
            model_name='bill',
            name='date_paid',
            field=models.DateField(blank=True, null=True, verbose_name='Date paid'),
        ),
    ]
