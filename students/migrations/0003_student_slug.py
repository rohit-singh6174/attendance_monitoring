# Generated by Django 5.0 on 2024-01-28 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_year_of_admission'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
