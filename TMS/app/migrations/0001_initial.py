# Generated by Django 4.1.13 on 2024-03-09 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.IntegerField(max_length=10)),
                ('confirmpassword', models.IntegerField(max_length=10)),
                ('phonenumber', models.IntegerField(max_length=10)),
            ],
        ),
    ]
