from django.shortcuts import render
from .forms import BookForm
from django.http import HttpResponse



def create_book(request):
    # form = TestForm()
    form = BookForm()


    if request.method == "POST":
        
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            
            return HttpResponse("Book saved successfuyully")


    return render(request, "create_book.html",{"form":form})



def index(request):
    return render(
        request,
        "index.html",
    )





    



