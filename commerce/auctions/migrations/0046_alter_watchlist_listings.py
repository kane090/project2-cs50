# Generated by Django 3.2.3 on 2021-06-24 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0045_auto_20210624_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='listings',
            field=models.ManyToManyField(blank=True, related_name='watchlist_listings', to='auctions.Auction_Listing'),
        ),
    ]