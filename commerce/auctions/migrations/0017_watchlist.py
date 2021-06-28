# Generated by Django 3.2.3 on 2021-06-15 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_alter_auction_listing_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listings', models.ManyToManyField(blank=True, related_name='watchlist_listings', to='auctions.Auction_Listing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]