# Generated by Django 3.1.2 on 2020-10-27 17:26

from django.db import migrations, models
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_user_even'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='even',
            field=models.IntegerField(default=0),
        ),
    ]