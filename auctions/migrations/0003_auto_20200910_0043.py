# Generated by Django 3.0.8 on 2020-09-10 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_comments_ddd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='list_id',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='ddd',
        ),
        migrations.DeleteModel(
            name='cate',
        ),
        migrations.DeleteModel(
            name='watchlist',
        ),
    ]

