# Generated by Django 3.2.3 on 2021-06-24 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0034_alter_watchlist_listings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction_listing',
            name='current_bid',
        ),
        migrations.AddField(
            model_name='auction_listing',
            name='current_bid',
            field=models.ManyToManyField(blank=True, related_name='current_bid_of_item', to='auctions.Bid'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='listings',
            field=models.ManyToManyField(blank=True, related_name='watchlist_listings', to='auctions.Auction_Listing'),
        ),
    ]
