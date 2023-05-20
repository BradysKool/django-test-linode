# Generated by Django 4.1.7 on 2023-03-19 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_reservation_delete_inputer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=100)),
                ('shift', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
