# Generated by Django 3.2.8 on 2021-12-03 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opioidapp', '0014_auto_20211203_0203'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvgData',
            fields=[
                ('drugname', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('avgData', models.IntegerField()),
            ],
        ),
    ]
