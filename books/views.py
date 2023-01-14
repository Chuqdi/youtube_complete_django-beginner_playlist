from django.shortcuts import render
from .models import Book
from .forms import BookForm
from django.http import HttpResponse

def index(request):
    return render(
        request,
        "index.html",

    )


def create_book(request):
    if request.method == "POST":
        
        bookForm = BookForm(request.POST)
        if bookForm.is_valid():
            bookForm.save()
            return HttpResponse("Book was creates successfully")
    else:
        bookForm = BookForm()
    return render(request, "create_book.html",
    {
        "form":bookForm
    }
    )

