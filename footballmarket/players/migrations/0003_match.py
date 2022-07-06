# Generated by Django 4.0.5 on 2022-06-29 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_remove_club_player_player_club'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('teams', models.CharField(max_length=100)),
                ('score', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
