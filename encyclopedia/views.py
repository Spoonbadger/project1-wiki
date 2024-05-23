from django.shortcuts import render
from markdown2 import Markdown
from . import util


def edit(request):
    if request.method == "POST":
        


def entry(request, title):
    content = markdown_to_html(title)
    if content:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content,
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "error": "Page not found"
        })


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def markdown_to_html(title):
    # Get the markdown content using the get_entry function in util
    md_file = util.get_entry(title)
    if md_file is None:
        return None
    else:
        # Convert to MD to HTML
        markdowner = Markdown()
        return markdowner.convert(md_file)


def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html")
    else:
    # If the new_page_title == entry from entries, present error message
        new_entry_title = request.POST['new_page_title']
        new_entry_title_lower = new_entry_title.lower()
        new_content = request.POST['new_content']
        entries = util.list_entries()
        for entry in entries:
            if new_entry_title_lower == entry.lower():
                return render(request, "encyclopedia/error.html", {
                    "error": "Page already exists",
                })
        util.save_entry(new_entry_title, new_content)
        new_entry_title = new_entry_title.title()
        html_content = markdown_to_html(new_entry_title)
        return render(request, "encyclopedia/entry.html",{
            "title": new_entry_title,
            "content": html_content,
        })
        


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
    

