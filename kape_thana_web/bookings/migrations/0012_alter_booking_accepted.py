# Generated by Django 5.1.2 on 2025-01-10 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0011_alter_booking_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='accepted',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
