# Generated by Django 4.1.13 on 2024-03-09 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_register_confirmpassword_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Register',
            new_name='Signupdetails',
        ),
    ]