from django.shortcuts import render, redirect

from books.models import Book
from .forms import BookForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required




@login_required
def list_books(request):
    books = Book.objects.filter(creator=request.user).order_by("-id")
    return render(request, "list_books.html",{"books":books})



@login_required
def create_book(request):
    # form = TestForm()
    form = BookForm()


    if request.method == "POST":
        
        form = BookForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.creator = request.user
            form.save()
            messages.success(request, "Book was created successfully")

            
            return redirect("list_books")


    return render(request, "create_book.html",{"form":form})



def index(request):
    return render(
        request,
        "index.html",
    )





    



