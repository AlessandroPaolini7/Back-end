# Generated by Django 4.1.3 on 2023-12-19 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonDRF', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='inventory',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
