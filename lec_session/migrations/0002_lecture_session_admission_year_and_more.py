# Generated by Django 5.0 on 2024-03-27 05:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lec_session', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture_session',
            name='admission_year',
            field=models.PositiveIntegerField(help_text='Use the following format: <YYYY>', null=True, validators=[django.core.validators.MinValueValidator(1900)]),
        ),
        migrations.AddField(
            model_name='lecture_session',
            name='sem_type',
            field=models.BooleanField(default=False),
        ),
    ]