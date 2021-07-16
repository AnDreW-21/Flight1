# Generated by Django 3.2.3 on 2021-07-16 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0001_initial'),
        ('blog', '0002_add_flight_plane'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_flight',
            name='no_of_tickets',
        ),
        migrations.AlterField(
            model_name='add_flight',
            name='plane',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aircraft.addaircraft'),
        ),
    ]