# Generated by Django 3.2.8 on 2021-12-03 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opioidapp', '0015_avgdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrescriberOnlyOpioids',
            fields=[
                ('prescriberid', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]