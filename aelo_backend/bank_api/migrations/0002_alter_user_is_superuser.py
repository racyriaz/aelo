# Generated by Django 3.2.6 on 2021-09-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
    ]