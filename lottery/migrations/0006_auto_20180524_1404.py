# Generated by Django 2.0 on 2018-05-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0005_client_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='shortcode',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]