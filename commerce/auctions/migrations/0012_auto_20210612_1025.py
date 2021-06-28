# Generated by Django 3.2.3 on 2021-06-12 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20210609_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='auction_listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.CharField(blank=True, max_length=128)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(blank=True, upload_to='auctions/images')),
            ],
        ),
        migrations.RenameModel(
            old_name='bids',
            new_name='bid',
        ),
        migrations.RenameModel(
            old_name='comments',
            new_name='comment',
        ),
        migrations.DeleteModel(
            name='auction_listings',
        ),
    ]
