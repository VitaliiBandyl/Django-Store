# Generated by Django 3.0.8 on 2020-07-18 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20200715_1850'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='RatingStar',
        ),
    ]