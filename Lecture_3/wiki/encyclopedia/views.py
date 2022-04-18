from cProfile import label
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django import forms
import random
import markdown2

from . import util


class EntryForm(forms.Form):
    new_entry_title = forms.CharField(label="New Entry Title:")
    new_entry_content = forms.CharField(label="Entry content:", widget=forms.Textarea(attrs={'placeholder': 'Start typing here'}))



# Create your views here
def index(request):
    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })
    
def get_page(request: HttpRequest, page_name=''):
    page_to_search = request.GET.get('q')
    if page_to_search:
        originalEntry = util.get_entry(page_to_search)
        if originalEntry:
            entry = markdown2.markdown(originalEntry)
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
        "entry": markdown2.markdown(util.get_entry(page_name))
    })
    
    
def add_entry(request: HttpRequest):
    if request.method == "POST":
        # entry_title = request.POST.get('new_entry_title')
        # entry_content = request.POST.get('new_entry_content')
        form = EntryForm(request.POST)
        if form.is_valid(): 
            entry_title = form.cleaned_data['new_entry_title']
            entry_content = form.cleaned_data['new_entry_content']
            existing_entries = [entry.upper() for entry in util.list_entries()] 
            if entry_title.upper() not in existing_entries:
                util.save_entry(entry_title, entry_content)
                return redirect("index")
            else:
                return render(request, "encyclopedia/new_entry.html", {
                    "error": f"Entry with the title '{entry_title}' already exists."
                })
        else:
            return render(request,"encyclopedia/new_entry.html", context={
                "new_form": form
            })    
    
    return render(request, "encyclopedia/new_entry.html", context={
        "new_form": EntryForm()
    })    


def edit_entry(request:HttpRequest, ENTRY_TITLE=''):
    if request.method == "POST":
        entry_name = request.POST.get('entryTitle');
        entry_content = request.POST.get('entryContent')
        util.save_entry(entry_name, entry_content)
        return redirect("index")
    
    return render(request, "encyclopedia/edit_entry.html",{
        "entry_name": ENTRY_TITLE.capitalize(),
        "entry_content": util.get_entry(ENTRY_TITLE)
    })
    
    
def random_page(request:HttpRequest):
    entries = util.list_entries()
    random_number = random.randint(0, len(entries) - 1)
    #entry_name = util.get_entry(entries[random_number])
    return redirect("wiki_entry", page_name=entries[random_number])
    
    