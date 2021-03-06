# Generated by Django 3.2.3 on 2021-06-09 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auction_listings_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listings',
            name='height',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='auction_listings',
            name='width',
            field=models.IntegerField(default=80),
        ),
        migrations.AlterField(
            model_name='auction_listings',
            name='photo',
            field=models.ImageField(height_field=models.IntegerField(default=100), upload_to='auctions/images', width_field=models.IntegerField(default=80)),
        ),
    ]
