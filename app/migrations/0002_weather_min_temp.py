# Generated by Django 4.1.3 on 2022-11-01 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='min_temp',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
