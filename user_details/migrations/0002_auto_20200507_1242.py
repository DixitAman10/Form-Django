# Generated by Django 3.0 on 2020-05-07 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='phone_number',
            new_name='contact',
        ),
    ]
