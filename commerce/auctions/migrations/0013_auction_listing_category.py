# Generated by Django 3.2.3 on 2021-06-12 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20210612_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listing',
            name='category',
            field=models.CharField(choices=[('F', 'Fashion'), ('T', 'Toys'), ('E', 'Electronics'), ('H', 'Home'), ('O', 'Other'), (None, 'None')], default='None', max_length=64),
            preserve_default=False,
        ),
    ]
