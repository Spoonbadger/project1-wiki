from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("new_page", views.new_page, name="new_page"),
    path("edit", views.edit, name="edit"),
    path("edit_save", views.edit_save, name="edit_save"),
    path("random", views.random_page, name="random")
]
