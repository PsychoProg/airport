# Generated by Django 4.2.7 on 2023-12-04 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airport', '0003_rename_user_ticket_passenger_remove_ticket_cost_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='seat_number',
        ),
        migrations.AlterField(
            model_name='flight',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight_number',
            field=models.IntegerField(),
        ),
    ]
