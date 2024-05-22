from django.shortcuts import render, redirect
from markdown2 import Markdown
from . import util

def entry(request, title):
    content = markdown_to_html(title)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
    })

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def markdown_to_html(title):
    # Get the markdown content using the get_entry function in util
    md_file = util.get_entry(title)
    if md_file is None:
        return redirect("encyclopedia/error.html")
    else:
        # Convert to MD to HTML
        markdowner = Markdown()
        return markdowner.convert(md_file)

    
def search(request):
    if request.method == "POST":
        # Create a list of all entries
        entries = util.list_entries()
        # Get user input from the form
        user_search = request.POST["q"].lower()
        user_search = user_search.lower()
        # Initialize list of possible matches
        matches = []
        # See if user_search matches an entry
        for entry in entries:
            if user_search == entry.lower():
                return render(request, "encyclopedia/entry.html", {
                    "title": user_search,
                    "content": markdown_to_html(user_search)
                })
        # See if user_search is in an entry
            elif user_search in entry.lower():
                matches.append(entry)
        if not matches:
            return render(request, "encyclopedia/index.html", {
                "entries": entries,
            })
        else:
            return render(request, "encyclopedia/search.html", {
            "matches": matches
        })
    

