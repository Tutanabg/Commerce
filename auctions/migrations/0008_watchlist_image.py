# Generated by Django 3.0.8 on 2020-09-10 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_watchlist_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

