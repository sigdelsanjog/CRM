# Generated by Django 3.0.5 on 2020-04-23 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200423_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
        migrations.AddField(
            model_name='products',
            name='tags',
            field=models.ManyToManyField(to='account.Tag'),
        ),
    ]
