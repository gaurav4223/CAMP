# Generated by Django 3.1.12 on 2023-03-11 13:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20230311_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
