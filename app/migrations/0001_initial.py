# Generated by Django 4.1.3 on 2022-11-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates', models.DateField()),
                ('max_temp', models.IntegerField()),
                ('precipitation', models.IntegerField()),
            ],
        ),
    ]