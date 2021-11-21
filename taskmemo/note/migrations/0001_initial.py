# Generated by Django 3.1.6 on 2021-11-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('score', models.IntegerField(choices=[(1, '低'), (2, '普通'), (3, '重要'), (4, '最重要'), (5, '緊急')])),
                ('text', models.TextField()),
            ],
        ),
    ]
