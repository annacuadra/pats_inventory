# Generated by Django 5.0.4 on 2024-04-09 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('number', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('location', models.CharField(blank=True, choices=[('Admin Office', 'Admin Office'), ('Room 01', 'Room 01'), ('Room 02', 'Room 02'), ('Room 03', 'Room 03'), ('Room 04', 'Room 04'), ('Room 05', 'Room 05')], max_length=20, null=True)),
                ('status', models.CharField(blank=True, choices=[('Working', 'Working'), ('Not Working', 'Not Working')], max_length=20, null=True)),
            ],
        ),
    ]