# Generated by Django 3.0.8 on 2020-07-21 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='url',
            new_name='slug',
        ),
    ]
