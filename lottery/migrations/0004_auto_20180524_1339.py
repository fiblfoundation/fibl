# Generated by Django 2.0 on 2018-05-24 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0003_auto_20180524_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='comments',
            field=models.CharField(default='no comments', max_length=400),
        ),
        migrations.AlterField(
            model_name='client',
            name='full_name',
            field=models.CharField(max_length=40),
        ),
    ]