# Generated by Django 2.0 on 2018-01-22 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'dummy_keywords',
            },
        ),
    ]
