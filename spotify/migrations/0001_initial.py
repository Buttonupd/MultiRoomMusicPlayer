# Generated by Django 3.2.6 on 2021-08-11 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('RareFormAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpotifyToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('refresh_token', models.CharField(max_length=250)),
                ('access_token', models.CharField(max_length=250)),
                ('expires_in', models.DateTimeField()),
                ('token_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('song_id', models.CharField(max_length=50)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RareFormAPI.room')),
            ],
        ),
    ]