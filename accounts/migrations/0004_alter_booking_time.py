# Generated by Django 4.2.19 on 2025-03-04 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_booking_guests_alter_booking_table_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(max_length=5),
        ),
    ]
