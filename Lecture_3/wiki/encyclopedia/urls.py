from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:page_name>", views.get_page, name="wiki_entry"),
    path("wiki/", views.get_page, name="search_entry")
]
