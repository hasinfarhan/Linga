# Generated by Django 2.0 on 2018-01-20 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primaryAddress', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
