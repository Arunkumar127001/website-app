# Generated by Django 3.2.11 on 2022-05-28 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=15)),
                ('zip', models.IntegerField(max_length=6)),
            ],
        ),
    ]
