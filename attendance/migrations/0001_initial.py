# Generated by Django 5.0 on 2024-02-07 08:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance_table',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True)),
                ('is_present', models.BooleanField(default=False)),
                ('roll_no', models.CharField(blank=True, max_length=250, null=True)),
                ('session_id', models.CharField(blank=True, max_length=250, null=True)),
                ('stud_name', models.CharField(blank=True, max_length=180)),
                ('sem_type', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_id', models.CharField(max_length=250, unique=True)),
                ('branch', models.CharField(max_length=250)),
                ('admission_year', models.PositiveIntegerField(help_text='Use the following format: <YYYY>', validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2024)])),
            ],
        ),
    ]
