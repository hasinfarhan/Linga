# Generated by Django 2.0 on 2018-01-22 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20180122_0559'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-date', '-time', 'status')},
        ),
    ]
