from django.shortcuts import render
from .models import Book


def book(request):
    bookName ="Learning Django"
   
    return render(
        request,
        "index.html",
        context={
        }


    )

