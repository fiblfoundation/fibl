# Generated by Django 2.0 on 2018-05-24 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0004_auto_20180524_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='shortcode',
            field=models.CharField(blank=True, max_length=9, unique=True),
        ),
    ]
