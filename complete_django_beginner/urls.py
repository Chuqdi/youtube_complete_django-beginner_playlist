
from django.contrib import admin
from django.urls import path, include
from books.views import index,create_book, list_books





urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("create_book", create_book, name="create_book"),
    path("list_books", list_books, name="list_books")

]

