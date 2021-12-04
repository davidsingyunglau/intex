# Generated by Django 3.2.8 on 2021-12-02 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drugname', models.CharField(max_length=30)),
                ('isopioid', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'drug',
            },
        ),
        migrations.CreateModel(
            name='Prescriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=11)),
                ('lname', models.CharField(max_length=11)),
                ('gender', models.CharField(max_length=1)),
                ('credentials', models.CharField(max_length=20)),
                ('specialty', models.CharField(max_length=62)),
                ('isopioidprescriber', models.CharField(max_length=5)),
                ('totalprescriptions', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'prescriber',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=14)),
                ('state_abv', models.CharField(max_length=2)),
                ('population', models.IntegerField()),
                ('death', models.IntegerField()),
            ],
            options={
                'db_table': 'state',
            },
        ),
        migrations.CreateModel(
            name='Triple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=0)),
                ('drug_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opioidapp.drug')),
                ('prescriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opioidapp.prescriber')),
            ],
            options={
                'db_table': 'triple',
            },
        ),
        migrations.AddField(
            model_name='prescriber',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opioidapp.state'),
        ),
    ]
