# Generated by Django 4.2.7 on 2023-12-04 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airport', '0004_remove_ticket_seat_number_alter_flight_cost_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='passenger_phone',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
