# Generated by Django 4.0.6 on 2022-08-02 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_totalamount_expense'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='category',
            new_name='name',
        ),
    ]
