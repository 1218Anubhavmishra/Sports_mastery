# Generated by Django 4.2.2 on 2023-06-23 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sports_app", "0012_employee_achievements_employee_communication_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="facebook",
            field=models.CharField(default="NA", max_length=10),
        ),
        migrations.AddField(
            model_name="employee",
            name="instagram",
            field=models.CharField(default="NA", max_length=10),
        ),
        migrations.AddField(
            model_name="employee",
            name="twitter",
            field=models.CharField(default="NA", max_length=10),
        ),
    ]
