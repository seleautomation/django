# Generated by Django 2.1.4 on 2019-01-09 11:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontdesk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userSignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=35, verbose_name='Full Name')),
                ('business_type', models.CharField(max_length=15, verbose_name='Business Type')),
                ('mobile_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{0, 9}$')], verbose_name='Mobile Number')),
                ('email', models.CharField(max_length=70, validators=[django.core.validators.RegexValidator(message='Email ID must be entered in the format: abc@domain.com', regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\\.[a-zA-Z]+$')], verbose_name='Email')),
                ('password', models.CharField(max_length=15, verbose_name='Password')),
            ],
        ),
    ]
