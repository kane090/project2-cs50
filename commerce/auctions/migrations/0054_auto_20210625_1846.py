# Generated by Django 3.2.3 on 2021-06-25 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0053_auto_20210625_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='listing',
            field=models.ManyToManyField(blank=True, related_name='category_listings', to='auctions.Auction_Listing'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='listings',
            field=models.ManyToManyField(blank=True, related_name='watchlist_listings', to='auctions.Auction_Listing'),
        ),
    ]
