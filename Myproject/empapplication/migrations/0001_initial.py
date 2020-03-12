# Generated by Django 3.0.2 on 2020-03-04 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_id', models.CharField(max_length=20)),
                ('First_name', models.CharField(max_length=40)),
                ('Last_name', models.CharField(max_length=40)),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]