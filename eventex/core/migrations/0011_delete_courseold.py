# Generated by Django 4.1.7 on 2023-04-19 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_course_abc_to_mti'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CourseOld',
        ),
    ]
