# Generated by Django 3.1.12 on 2023-03-11 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_student_studentname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='studentname',
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='eventyear',
            field=models.IntegerField(default=2022),
        ),
    ]