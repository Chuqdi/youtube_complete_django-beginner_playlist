
from django.contrib import admin
from django.urls import path
from books.views import book


urlpatterns = [
    path('admin/', admin.site.urls),
    path("book", book, name="book")
]

