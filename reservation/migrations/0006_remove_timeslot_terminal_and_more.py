# Generated by Django 5.0.6 on 2024-06-21 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_terminal_remove_reservation_terminal_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslot',
            name='terminal',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='operation',
        ),
        migrations.DeleteModel(
            name='Terminal',
        ),
    ]