from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def get_page(request, page_name):
    return render(request, "encyclopedia/entry.html", {
        "page_name": page_name.upper(),
        "entry": util.get_entry(page_name)
    })

