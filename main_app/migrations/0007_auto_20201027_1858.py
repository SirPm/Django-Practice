# Generated by Django 3.1.2 on 2020-10-27 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20201027_1826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='even',
            new_name='Input an even number',
        ),
    ]
