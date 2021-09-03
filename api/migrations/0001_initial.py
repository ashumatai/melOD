# Generated by Django 3.1 on 2021-09-03 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomCode', models.CharField(default='', max_length=10, unique=True)),
                ('host', models.CharField(max_length=50, unique=True)),
                ('guestCanPause', models.BooleanField(default=False)),
                ('votesToSkip', models.IntegerField(default=1)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]