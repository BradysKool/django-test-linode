# Generated by Django 4.1.7 on 2023-03-25 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_employees_delete_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('koolness', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
    ]