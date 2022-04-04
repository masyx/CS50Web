from cProfile import label
from xml.dom.pulldom import default_bufsize
from django.http import HttpRequest
from django.shortcuts import render
from django import forms

from . import util


class NewTextField(forms.Form):
    new_entry_form = forms.Textarea()



# Create your views here
def index(request):
    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })
    
def get_page(request: HttpRequest, page_name=''):
    page_to_search = request.GET.get('q')
    if page_to_search:
        entry = util.get_entry(page_to_search)
        if entry:
            return render(request, "encyclopedia/entry.html",{
               "page_name": page_to_search.upper(),
                "entry": entry 
            })
        else:
            entries = util.get_possible_entries(page_to_search)
            return render(request, "encyclopedia/index.html", {
                "entries": entries
            }) 
        
    return render(request, "encyclopedia/entry.html", {
        "page_name": page_name.upper(),
        "entry": util.get_entry(page_name)
    })
    
    
def add_entry(request: HttpRequest):
    if request.method == "POST":
        entry_title = request.POST.get('entryTitle')
        entry_content = request.POST.get('entryContent')
        
        existing_entries = [entry.upper() for entry in util.list_entries()] 
        if entry_title.upper() not in existing_entries:
            util.save_entry(entry_title, entry_content)
            return index(request)
        else:
            return render(request, "encyclopedia/new_entry.html", {
                "error": f"Entry with the title '{entry_title}' already exists."
            })
    
    return render(request, "encyclopedia/new_entry.html")    