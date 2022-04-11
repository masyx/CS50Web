from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:page_name>", views.get_page, name="wiki_entry"),
    path("wiki/", views.get_page, name="search_entry"),
    path("NewEntry/", views.add_entry, name="add_entry"),
    path("EditEntry/<str:ENTRY_TITLE>", views.edit_entry, name="edit_entry"),
    path("RandomPage", views.random_page, name="random_page")
]
