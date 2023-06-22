# Generated by Django 4.1.7 on 2023-04-14 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports_app', '0009_coach_assign'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport_Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=40)),
                ('weight', models.CharField(default=None, max_length=40)),
                ('height', models.CharField(default=None, max_length=40)),
                ('gender', models.CharField(default=None, max_length=40)),
                ('prefered_sport', models.CharField(default=None, max_length=40)),
                ('health_condition', models.CharField(default=None, max_length=40)),
            ],
        ),
    ]