from optparse import TitledHelpFormatter
from django import forms
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages
from django.core import validators
import random
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util

from markdown2 import Markdown


class NewEntryForm(forms.Form):
    title = forms.CharField(label = "Title")
    content = forms.CharField(widget=forms.Textarea, label="Content")

class EditForm(forms.Form):
    content = forms.CharField(label="content", widget=forms.Textarea(attrs={'rows':10}))


def title(request, title):
    nd = Markdown()
    page = util.get_entry(title)
    finalPage = nd.convert(page)
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "entries": finalPage
        })

    return render(request, "encyclopedia/new.html",{
        "form": NewEntryForm()
    })
       

def index(request):
    if request.method == "POST":
        display = []
        search = request.POST['q']
        
        if search in util.list_entries():
            return redirect("/" + search, {    
                "entries": util.get_entry(search)           
            })

        return render(request, "encyclopedia/index.html", {
             "entries": util.list_search(search)
        })
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
            })    
        

def new(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if title in util.list_entries():
                raise forms.ValidationError('This entry already exists')    
            else:
                util.save_entry(title,content)
                return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
            }) 
                
    return render(request, "encyclopedia/new.html",{
        "form": NewEntryForm()
    })

def edit(request):
    if request.method == "POST":
        md = Markdown()
        a = request.POST['a']
        page = util.get_entry(a)
        final = md.convert(page)
        return render(request, "encyclopedia/edit.html",{
        "title": a,
        "page": final
        })
    return render(request, "encyclopedia/edit.html",{
    "a": title
    })

def do(request):
    if request.method == "POST":
        md = Markdown()
        title = request.POST['title']
        content = request.POST['content']
        md._encode_code(content)
        util.save_entry(title, content)
        return redirect
        {"/wiki/" + title}





def randompage(request):
    return render(request, "encyclopedia/randompage.html", {
        "entry":  random.choice(util.list_entries())
    })
    
   







