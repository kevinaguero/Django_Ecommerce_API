# Generated by Django 3.1 on 2023-05-20 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_auto_20230518_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
