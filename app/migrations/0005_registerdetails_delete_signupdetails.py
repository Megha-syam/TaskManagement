# Generated by Django 4.1.13 on 2024-03-09 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_signupdetails_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='registerdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Signupdetails',
        ),
    ]
