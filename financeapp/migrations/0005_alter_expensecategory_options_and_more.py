# Generated by Django 4.2.13 on 2024-06-01 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeapp', '0004_billissuer_alter_expense_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expensecategory',
            options={'verbose_name': 'Expense category', 'verbose_name_plural': 'Expense categories'},
        ),
        migrations.AlterModelOptions(
            name='incomecategory',
            options={'verbose_name': 'Income category', 'verbose_name_plural': 'Income categories'},
        ),
    ]
