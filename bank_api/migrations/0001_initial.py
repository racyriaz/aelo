# Generated by Django 4.0 on 2021-12-28 16:11

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('password', models.CharField(max_length=1281)),
                ('last_login', models.DateTimeField(auto_now=True, null=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=150, primary_key=True, serialize=False, unique=True)),
                ('full_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('mobile', models.IntegerField(blank=True, default=None, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['username'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserOptions',
            fields=[
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bank_api.user')),
                ('cat_options', models.CharField(default='family,food,fuel,loan,smart_phone', max_length=100000)),
            ],
            options={
                'ordering': ['username'],
            },
        ),
        migrations.CreateModel(
            name='BankTranscations',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=19, verbose_name='Money/Amount in INR')),
                ('type_of_trans', models.CharField(blank=True, max_length=100, null=True)),
                ('comment', models.CharField(blank=True, max_length=30, null=True)),
                ('cat_of_trans', models.CharField(blank=True, max_length=200, null=True)),
                ('trans_date', models.DateField(null=True, verbose_name='Transaction Date')),
                ('trans_hour', models.CharField(max_length=6, null=True, verbose_name='Transaction Hour')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp of transaction entry')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Timestamp of transaction entry')),
                ('payment_mode', models.CharField(max_length=40, verbose_name='Payment Mode')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bank_api.user')),
            ],
            options={
                'ordering': ['modified'],
            },
        ),
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=40)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bank_api.user')),
            ],
            options={
                'ordering': ['username'],
            },
        ),
        migrations.CreateModel(
            name='AccountBalance',
            fields=[
                ('bank_name', models.CharField(max_length=70)),
                ('account_balance', models.DecimalField(decimal_places=2, max_digits=25)),
                ('timestamp', models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bank_api.user')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]