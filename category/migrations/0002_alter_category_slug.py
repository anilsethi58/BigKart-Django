# Generated by Django 5.1.3 on 2024-11-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
    ]
