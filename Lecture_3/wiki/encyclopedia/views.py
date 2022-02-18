from asyncio.windows_events import NULL
from webbrowser import get
from django.http import HttpRequest
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def get_page(request: HttpRequest, page_name=''):
    page_to_search = request.GET.get('q')
    if page_to_search != None:
        return render(request, "encyclopedia/entry.html",{
           "page_name": page_to_search.upper(),
            "entry": util.get_entry(page_to_search) 
    })    
        
    return render(request, "encyclopedia/entry.html", {
        "page_name": page_name.upper(),
        "entry": util.get_entry(page_name)
    })

