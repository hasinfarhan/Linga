# Generated by Django 2.0 on 2018-01-21 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_remove_dummypost_postid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DummyPost',
            new_name='Post',
        ),
    ]
