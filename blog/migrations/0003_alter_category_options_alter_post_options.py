# Generated by Django 5.2.3 on 2025-06-21 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_category_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "category", "verbose_name_plural": "categories"},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ("publish",)},
        ),
    ]
