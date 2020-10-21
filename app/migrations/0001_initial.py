# Generated by Django 3.0.7 on 2020-10-21 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('squirrel_id', models.CharField(max_length=30, unique=True)),
                ('shift', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('primary_fur_color', models.CharField(blank=True, max_length=30)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('specific_location', models.CharField(blank=True, max_length=30)),
                ('running', models.BooleanField(blank=True)),
                ('chasing', models.BooleanField(blank=True)),
                ('climbing', models.BooleanField(blank=True)),
                ('eating', models.BooleanField(blank=True)),
                ('foraging', models.BooleanField(blank=True)),
                ('other_Activities', models.CharField(blank=True, max_length=30)),
                ('kuks', models.BooleanField(blank=True)),
                ('quaas', models.BooleanField(blank=True)),
                ('moans', models.BooleanField(blank=True)),
                ('tail_flags', models.BooleanField(blank=True)),
                ('tail_twitches', models.BooleanField(blank=True)),
                ('approaches', models.BooleanField(blank=True)),
                ('indifferent', models.BooleanField(blank=True)),
                ('runs_From', models.BooleanField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='apprequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('squi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.squirrel')),
            ],
        ),
    ]
