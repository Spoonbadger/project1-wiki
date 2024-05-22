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

    
def search(request, )