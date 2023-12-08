# Generated by Django 4.2.6 on 2023-10-30 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('avatar_filename', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('password', models.CharField(max_length=255)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('role', models.CharField(choices=[('ADMIN', 'Admin'), ('USER', 'User')], max_length=5)),
                ('username', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=255)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=255)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='nexxus.user')),
            ],
            options={
                'verbose_name': 'Note',
                'verbose_name_plural': 'Notes',
                'db_table': 'notes',
            },
        ),
    ]
