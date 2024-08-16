# Generated by Django 3.2.25 on 2024-08-15 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('language', models.CharField(choices=[('Telugu', 'Telugu'), ('Hindi', 'Hindi'), ('English', 'English')], default='Telugu', max_length=25)),
                ('song_thumbnail', models.FileField(upload_to='')),
                ('year', models.IntegerField()),
                ('singer', models.CharField(max_length=100)),
                ('song_file', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'Song',
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_name', models.CharField(max_length=100)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_dashboard.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.users')),
            ],
            options={
                'db_table': 'Playlist',
            },
        ),
    ]