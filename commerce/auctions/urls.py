from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("listing/<str:listing_name>", views.listing, name="listing"),
    path("watchlist/<str:username>", views.watchlist, name="watchlist"),
    path("add_to_watchlist/<str:listing_name>", views.add_to_watchlist, name="add_to_watchlist"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category_name>", views.category, name="category"),
    path("bid/<str:listing_name>", views.bid, name="bid"),
    path("close_listing/<str:listing_name>", views.close_listing, name="close_listing"),
    path("comment/<str:listing_name>", views.comment, name="comment")
]
