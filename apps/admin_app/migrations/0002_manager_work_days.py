# Generated by Django 4.2.1 on 2023-07-20 15:25

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):
    dependencies = [
        ("admin_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="manager",
            name="work_days",
            field=multiselectfield.db.fields.MultiSelectField(
                blank=True,
                choices=[
                    ("Monday", "Monday"),
                    ("Tuesday", "Tuesday"),
                    ("Wednesday", "Wednesday"),
                    ("Thursday", "Thursday"),
                    ("Friday", "Friday"),
                    ("Saturday", "Saturday"),
                    ("Sunday", "Sunday"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]