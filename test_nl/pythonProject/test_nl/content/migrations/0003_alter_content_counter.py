# Generated by Django 5.0.2 on 2024-02-19 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_alter_content_counter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="counter",
            field=models.PositiveIntegerField(
                default=0, editable=False, verbose_name="Счетчик просмотров"
            ),
        ),
    ]
