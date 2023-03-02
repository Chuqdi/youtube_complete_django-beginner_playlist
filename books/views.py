from django.shortcuts import render, redirect

from books.models import Book
from .forms import BookForm
from django.http import HttpResponse
from django.contrib import messages


def list_books(request):
    books = Book.objects.all().order_by("-id")
    return render(request, "list_books.html",{"books":books})




def create_book(request):
    # form = TestForm()
    form = BookForm()


    if request.method == "POST":
        
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Book was created successfully")

            
            return redirect("list_books")


    return render(request, "create_book.html",{"form":form})



def index(request):
    return render(
        request,
        "index.html",
    )





    



