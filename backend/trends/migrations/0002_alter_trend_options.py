# Generated by Django 5.0.7 on 2024-08-17 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trends', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trend',
            options={'ordering': ['-hits']},
        ),
    ]
