# Generated by Django 2.0 on 2018-01-21 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20180121_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.TimeField(),
        ),
    ]
