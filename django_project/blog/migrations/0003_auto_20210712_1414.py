# Generated by Django 3.2.3 on 2021-07-12 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210712_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_flight',
            name='author',
            field=models.CharField(default='Admin', max_length=10),
        ),
        migrations.AlterField(
            model_name='add_flight',
            name='destination',
            field=models.CharField(max_length=100),
        ),
    ]
