# Generated by Django 3.2.16 on 2023-01-30 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0004_alter_news_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="courseteachers",
            options={"verbose_name": "Teacher", "verbose_name_plural": "Teachers"},
        ),
        migrations.AlterModelOptions(
            name="lesson",
            options={"ordering": ("course", "num"), "verbose_name": "Lesson", "verbose_name_plural": "Lessons"},
        ),
    ]
