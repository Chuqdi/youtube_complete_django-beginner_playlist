from django.shortcuts import render
from .forms import TestForm, BookForm


def create_book(request):
    # form = TestForm()
    form = BookForm()
    return render(request, "create_book.html",{"form":form})



def index(request):
    return render(
        request,
        "index.html",
    )





    



