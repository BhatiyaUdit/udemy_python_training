# Generated by Django 3.2.9 on 2021-11-14 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='slug',
            field=models.SlugField(max_length=250),
        ),
    ]
