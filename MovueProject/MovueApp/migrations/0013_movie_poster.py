# Generated by Django 5.1.6 on 2025-02-22 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovueApp', '0012_remove_genre_movies_movie_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='posters/'),
        ),
    ]
