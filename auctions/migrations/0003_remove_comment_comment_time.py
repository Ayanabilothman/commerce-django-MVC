# Generated by Django 4.0.1 on 2022-02-10 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category_listing_comment_bid_user_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_time',
        ),
    ]