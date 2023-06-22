# Generated by Django 4.1.7 on 2023-03-14 06:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sports_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
                ('user_query', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('type', models.CharField(choices=[('C', 'coach'), ('T', 'Trainer'), ('M', 'Medical Staff'), ('S', 'Sweeper')], max_length=4)),
                ('experience', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback_Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
                ('feedback_text', models.TextField()),
                ('ratings', models.CharField(max_length=6)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_name', models.CharField(max_length=10)),
                ('no_of_players', models.IntegerField()),
                ('equipment', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sports_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Sport_Plan',
            fields=[
                ('plan_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('charge', models.IntegerField(max_length=5)),
                ('facilities', models.TextField()),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sports_app.sport')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sports_app.sport'),
        ),
    ]