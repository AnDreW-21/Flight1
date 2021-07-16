# Generated by Django 3.2.3 on 2021-07-15 23:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
                ('To', models.CharField(max_length=100)),
                ('check_in_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('check_out_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.CharField(default='Admin', max_length=10)),
                ('no_of_tickets', models.DecimalField(decimal_places=0, default=100, max_digits=3)),
                ('class_avaiable', models.DecimalField(decimal_places=0, default=3, max_digits=1)),
            ],
        ),
    ]
