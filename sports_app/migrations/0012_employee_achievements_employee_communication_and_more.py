# Generated by Django 4.2.2 on 2023-06-23 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("sports_app", "0011_admission_request"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="achievements",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="employee",
            name="communication",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="employee",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="profile_pics"),
        ),
        migrations.AddField(
            model_name="employee",
            name="institute",
            field=models.CharField(default="NA", max_length=50),
        ),
        migrations.AddField(
            model_name="employee",
            name="knowledge",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="employee",
            name="monthly_charge",
            field=models.CharField(default="NA", max_length=5),
        ),
        migrations.AddField(
            model_name="employee",
            name="planning",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="employee",
            name="professionalism",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="employee",
            name="students",
            field=models.CharField(default="NA", max_length=10),
        ),
        migrations.AlterField(
            model_name="employee",
            name="email",
            field=models.EmailField(default="NA", max_length=40),
        ),
        migrations.AlterField(
            model_name="employee",
            name="employee_name",
            field=models.CharField(default="NA", max_length=45),
        ),
        migrations.AlterField(
            model_name="employee",
            name="experience",
            field=models.CharField(default="NA", max_length=3),
        ),
        migrations.AlterField(
            model_name="employee",
            name="sport",
            field=models.ForeignKey(
                default="NA",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="sports_app.sport",
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="type",
            field=models.CharField(
                choices=[
                    ("C", "coach"),
                    ("T", "Trainer"),
                    ("M", "Medical Staff"),
                    ("S", "Sweeper"),
                ],
                default="NA",
                max_length=4,
            ),
        ),
    ]
