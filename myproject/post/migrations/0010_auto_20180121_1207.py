# Generated by Django 2.0 on 2018-01-21 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_postimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='imagefile',
            field=models.ImageField(upload_to='postImages'),
        ),
        migrations.AlterModelTable(
            name='postimage',
            table='dummy_post_images',
        ),
    ]
