# Generated by Django 2.1.4 on 2019-01-24 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontdesk', '0005_auto_20190124_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='mobile_number',
            field=models.CharField(max_length=10),
        ),
    ]
