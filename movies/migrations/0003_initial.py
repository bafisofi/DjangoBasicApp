# Generated by Django 4.1.2 on 2022-10-10 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0002_delete_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=120, verbose_name='Second Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Addres')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=120, verbose_name='Second Name')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
                ('place_of_birth', models.DateField(blank=True, null=True)),
                ('place_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
                ('biography', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Genre of the movie', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Venue Name')),
                ('address', models.CharField(max_length=300)),
                ('zip_code', models.CharField(max_length=15, verbose_name='Zip Code')),
                ('phone', models.CharField(max_length=25, verbose_name='Contact phone')),
                ('web', models.URLField(max_length=120, verbose_name='Website Address')),
                ('email_address', models.EmailField(max_length=254, verbose_name='Email Address')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_movie', models.CharField(max_length=32)),
                ('summary', models.TextField(help_text='Pon aqui de que va el libro', max_length=100)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.director')),
                ('genre', models.ManyToManyField(to='movies.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Event Name')),
                ('event_date', models.DateField(verbose_name='Date')),
                ('description', models.TextField(blank=True)),
                ('attendees', models.ManyToManyField(blank=True, to='movies.clubuser')),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.director')),
                ('movie_title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.venue')),
            ],
        ),
    ]
