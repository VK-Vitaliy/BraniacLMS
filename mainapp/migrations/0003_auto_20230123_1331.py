# Generated by Django 3.2.16 on 2023-01-23 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0002_courses_cover"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Lessons",
            new_name="Lesson",
        ),
        migrations.RenameField(
            model_name="lesson",
            old_name="courses",
            new_name="course",
        ),
    ]
