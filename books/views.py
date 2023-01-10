from django.shortcuts import render



def book(request):
    bookName ="Learning Django"
   
    return render(
        request,
        "index.html",
        context={
           "book_name":bookName
        }


    )

