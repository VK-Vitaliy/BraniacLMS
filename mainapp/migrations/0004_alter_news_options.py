# Generated by Django 3.2.16 on 2023-01-30 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_auto_20230124_0934"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="news",
            options={"ordering": ("-created",), "verbose_name": "News", "verbose_name_plural": "News"},
        ),
    ]
