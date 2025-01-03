# Generated by Django 5.0 on 2024-01-28 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_roll_no', models.CharField(max_length=250, unique=True)),
                ('stud_name', models.CharField(max_length=100)),
                ('stud_phone', models.CharField(max_length=12)),
                ('stud_email', models.EmailField(max_length=254)),
                ('stud_div', models.CharField(max_length=1)),
                ('stud_profile', models.ImageField(null=True, upload_to='student')),
                ('finger_id', models.IntegerField()),
                ('year_of_admission', models.IntegerField(max_length=4)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.department')),
            ],
        ),
    ]
