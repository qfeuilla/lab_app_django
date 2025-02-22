# Generated by Django 3.1.6 on 2021-02-10 23:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('results', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docker', models.FileField(upload_to='')),
                ('token', models.CharField(max_length=15, unique=True, validators=[django.core.validators.MinLengthValidator(15)])),
                ('flag', models.CharField(choices=[('Wait', 'Waiting for machine'), ('Run', 'Running'), ('Finished', 'Finished'), ('Stopping', 'Pending Stop'), ('Stoped', 'Stoped'), ('Error', 'Error')], max_length=25)),
                ('result', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Session.result')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
