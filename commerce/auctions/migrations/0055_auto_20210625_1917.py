# Generated by Django 3.2.3 on 2021-06-25 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0054_auto_20210625_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listing',
            name='comments',
            field=models.ManyToManyField(related_name='comments_of_item', to='auctions.Comment'),
        ),
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