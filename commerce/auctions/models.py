from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField


class User(AbstractUser):
    pass

class Auction_Listing(models.Model):
    name = models.CharField(max_length=64)
    initial_price = models.DecimalField(decimal_places=2, max_digits=10)
    current_bid = models.ForeignKey('Bid', on_delete=models.CASCADE, related_name="current_bid_of_item", null=True)
    description = models.CharField(max_length=128, blank=True, default="No description.")
    date_created = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to="auctions/images", blank=True)
    category = ForeignKey('Category', on_delete=models.CASCADE, related_name="category_of_item", blank=True)
    comments = ManyToManyField('Comment', related_name="comments_of_item", blank=True)
    creator = ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    closed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}: {self.creator.username}"

class Bid(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE, related_name="bid_user")
    listing = ForeignKey(Auction_Listing, on_delete=models.CASCADE, related_name="bid_listing", null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"{self.user.username}: ${self.amount} on {self.listing.name}"

class Comment(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE, related_name="user_of_comment")
    comment = models.CharField(max_length=128)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.date_posted}"

class Watchlist(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist_user")
    listings = ManyToManyField(Auction_Listing, related_name="watchlist_listings", blank=True)

    def __str__(self):
        return f"{self.user}'s Watchlist"

class Category(models.Model):
    name = models.CharField(max_length=64)
    listing = ManyToManyField(Auction_Listing, related_name="category_listings", blank=True)

    def __str__(self):
        return f"{self.name}"