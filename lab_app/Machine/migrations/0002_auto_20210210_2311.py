# Generated by Django 3.1.6 on 2021-02-10 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Machine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='type',
            field=models.CharField(choices=[(1, 'CPU'), (2, 'GPU')], max_length=20),
        ),
    ]
