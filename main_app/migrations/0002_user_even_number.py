# Generated by Django 3.1.2 on 2020-10-27 16:50

from django.db import migrations, models
import django.utils.timezone
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='even_number',
            field=models.IntegerField(default=0, name='n'),
            preserve_default=False,
        ),
    ]