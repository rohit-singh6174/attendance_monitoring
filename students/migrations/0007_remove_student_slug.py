# Generated by Django 5.0 on 2024-01-28 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_alter_student_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='slug',
        ),
    ]
