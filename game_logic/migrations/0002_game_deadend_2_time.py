# Generated by Django 4.2.1 on 2023-05-15 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_logic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='deadend_2_time',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
