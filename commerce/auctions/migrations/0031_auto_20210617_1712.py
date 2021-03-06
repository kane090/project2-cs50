# Generated by Django 3.2.3 on 2021-06-17 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0030_alter_watchlist_listings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction_listing',
            old_name='price',
            new_name='initial_price',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='auction',
        ),
        migrations.AddField(
            model_name='auction_listing',
            name='current_bid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='current_bid_of_item', to='auctions.bid'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='listings',
            field=models.ManyToManyField(blank=True, related_name='watchlist_listings', to='auctions.Auction_Listing'),
        ),
    ]
