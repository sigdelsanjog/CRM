# Generated by Django 3.0.5 on 2020-06-01 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]