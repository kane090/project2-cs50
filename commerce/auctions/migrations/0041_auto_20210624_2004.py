# Generated by Django 3.2.3 on 2021-06-24 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0040_alter_watchlist_listings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listing',
            name='current_bid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_bid_of_item', to='auctions.bid'),
        ),
        migrations.AlterField(
            model_name='auction_listing',
            name='description',
            field=models.CharField(blank=True, default='No description.', max_length=128),
        ),
        migrations.AlterField(
            model_name='auction_listing',
            name='photo',
            field=models.ImageField(blank=True, default='No photo provided.', upload_to='auctions/images'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='listing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bid_listing', to='auctions.auction_listing'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='listings',
            field=models.ManyToManyField(blank=True, related_name='watchlist_listings', to='auctions.Auction_Listing'),
        ),
    ]
