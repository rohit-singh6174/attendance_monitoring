# Generated by Django 5.0 on 2024-02-02 11:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0007_remove_student_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture_Session',
            fields=[
                ('session_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=False)),
                ('subject_name', models.CharField(max_length=30)),
                ('start_time', models.TimeField(default='00:00:00')),
                ('end_time', models.TimeField(default='00:00:00')),
                ('date', models.DateField(blank=True, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.department')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
