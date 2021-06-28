from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from .models import *

class CreateListingForm(forms.Form):
    title = forms.CharField(max_length=64, required=True, label="Title")
    price = forms.DecimalField(decimal_places=2, max_digits=5, required=True, label="Starting bid")
    description = forms.CharField(max_length=128, required=False, label="Description") 
    photo = forms.ImageField(required=False, label="Photo (optional)")
    category = forms.CharField(max_length=64, required=False, label="Category (optional)")


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Auction_Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            watchlist = Watchlist(user=user)
            watchlist.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create(request):
    if request.method == "POST":
        form = CreateListingForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data["title"]
            initial_price = form.cleaned_data["price"]
            description = form.cleaned_data["description"]
            photo = form.cleaned_data["photo"]
            user = request.user
            category = form.cleaned_data["category"]
            if category == "":
                category = Category(name="None")
            else:
                category = Category(name=form.cleaned_data["category"])
            category.save()
            l = Auction_Listing(name=title, initial_price=initial_price,
                description=description, photo=photo, category=category, creator=user)
            l.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/create.html", {
            "form": CreateListingForm()
        })

def listing(request, listing_name, message=None):
    auction_listing = Auction_Listing.objects.get(name=listing_name)
    try:
        watchlist = Watchlist.objects.get(user=request.user).listings.all()
    except (TypeError, ObjectDoesNotExist):
        watchlist = None
    return render(request, "auctions/listing.html", {
        "listing": auction_listing,
        "message": message,
        "watchlist": watchlist,
        "comments": auction_listing.comments.all().order_by('id').reverse()
    })

@login_required
def watchlist(request, username):
    try:
        user = User.objects.get(username=username)
        return render(request, "auctions/watchlist.html", {
            "username": username,
            "list": Watchlist.objects.get(user=user).listings.all()
        })
    except ObjectDoesNotExist:
        return render(request, "auctions/watchlist.html", {
            "username": username
        })

@login_required
def add_to_watchlist(request, listing_name):
    auction_listing = Auction_Listing.objects.get(name=listing_name)
    watchlist = Watchlist.objects.get(user=request.user)
    if auction_listing not in watchlist.listings.all():
        watchlist.listings.add(auction_listing)
        watchlist.save()
        message = "Successfully added listing to watchlist!"
    else:
        watchlist.listings.remove(auction_listing)
        watchlist.save()
        message = "Successfully removed listing from watchlist!"
    return listing(request, listing_name, message)

def categories(request):
    return render(request, "auctions/categories.html", {
        "list_of_categories": Category.objects.exclude(name="None")
    })

def category(request, category_name):
    return render(request, "auctions/category.html", {
        "category": category_name,
        "items_in_category": Auction_Listing.objects.filter(category=Category.objects.get(name=category_name), closed=False)
    })

@login_required
def bid(request, listing_name):
    if request.method == "POST":
        bid_amount = float(request.POST.get("bid"))
        auction = Auction_Listing.objects.get(name=listing_name)
        bid_message = "Successfully placed your bid!"
        error_message = "Your bid is not high enough!"
        if bid_amount > float(auction.initial_price):
            if auction.current_bid:
                if bid_amount > float(auction.current_bid.amount):
                    bid = Bid(user=request.user, listing=auction, amount=bid_amount)
                    bid.save()
                    auction.current_bid = bid
                    auction.save()
                    return listing(request, listing_name, bid_message)
                else:
                    return listing(request, listing_name, error_message)
            else:
                bid = Bid(user=request.user, listing=auction, amount=bid_amount)
                bid.save()
                auction.current_bid = bid
                auction.save()
                return listing(request, listing_name, bid_message)
        else:
            return listing(request, listing_name, error_message)

@login_required
def close_listing(request, listing_name):
    auction_listing = Auction_Listing.objects.get(name=listing_name)
    auction_listing.closed = True
    auction_listing.save()
    return listing(request, listing_name)

@login_required
def comment(request, listing_name):
    if request.method == "POST":
        text = request.POST.get("comment")
        auction_listing = Auction_Listing.objects.get(name=listing_name)
        user_comment = Comment(user=request.user, comment=text)
        user_comment.save()
        auction_listing.comments.add(user_comment)
        auction_listing.save()
        message = "Successfully commented on listing!"
        return listing(request, listing_name, message=message)