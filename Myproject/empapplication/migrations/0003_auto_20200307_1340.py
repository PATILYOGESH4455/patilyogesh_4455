# Generated by Django 3.0.2 on 2020-03-07 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapplication', '0002_auto_20200307_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Employee_id',
            field=models.IntegerField(max_length=20),
        ),
    ]