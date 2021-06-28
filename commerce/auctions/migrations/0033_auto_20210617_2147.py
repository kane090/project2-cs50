# Generated by Django 3.2.3 on 2021-06-17 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0032_auto_20210617_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='listing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bid_listing', to='auctions.auction_listing'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='listings',
            field=models.ManyToManyField(blank=True, related_name='watchlist_listings', to='auctions.Auction_Listing'),
        ),
    ]