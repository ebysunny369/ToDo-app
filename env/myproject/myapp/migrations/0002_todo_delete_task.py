# Generated by Django 4.2.6 on 2024-02-07 04:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Todo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True)),
                ("date", models.DateTimeField(blank=True, null=True)),
                ("completed", models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name="Task",
        ),
    ]
