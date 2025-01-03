# Generated by Django 5.0 on 2024-03-18 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_attendance_table_admission_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance_table',
            name='stud_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='attendance_table',
            name='stud_profile',
            field=models.ImageField(null=True, upload_to='student'),
        ),
    ]
