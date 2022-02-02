from django.urls import reverse
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here
def index(request: HttpRequest):
    if "tasks" not in request.session:
        request.session["tasks"] = []
        
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })
    
def add(request: HttpRequest):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "task_form": form
            })
        
    return render(request, "tasks/add.html", {
        "task_form": NewTaskForm()
    })    
