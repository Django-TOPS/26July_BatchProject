# Generated by Django 3.2.7 on 2021-12-17 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_uploadpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadpost',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
