from django.shortcuts import render
from .models import Book
from .forms import BookForm
from django.http import HttpResponse

def index(request):
    return render(
        request,
        "index.html",

    )



