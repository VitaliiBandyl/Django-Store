# Generated by Django 3.0.8 on 2020-07-21 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200721_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_with_discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Price'),
            preserve_default=False,
        ),
    ]