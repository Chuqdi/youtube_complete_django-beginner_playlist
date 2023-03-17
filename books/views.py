from django.shortcuts import render, redirect

from books.models import Book
from .forms import BookForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin






class DeleteBook(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Book
    template_name ="delete.html"
    success_url ="/list_books"

    def test_func(self):
        ##HOW TO GET THE QUERYSET INSTANCE
        ##self.get_object()
        
        ##HOW TO GET THE LOGGED IN USER
        #self.request.user

        return self.get_object().creator == self.request.user
        



class UpdateBook(LoginRequiredMixin,UpdateView):
    model = Book
    template_name ="update.html"
    fields = ['name', 'description']
    success_url ="/list_books"   




@login_required
def list_books(request):
    books = Book.objects.filter(creator=request.user).order_by("-id")
    print(books)
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
            messages.success(request, "Book was created successfully")
            form.save()

            
            return redirect("list_books")


    return render(request, "create_book.html",{"form":form})



def index(request):
    return render(
        request,
        "index.html",
    )





    



