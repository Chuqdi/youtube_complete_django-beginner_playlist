
from django.contrib import admin
from django.urls import path, include
from books.views import index,create_book, list_books, DeleteBook, UpdateBook
from users.views import sign_up
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("create_book", create_book, name="create_book"),
    path("delete_book/<int:pk>", DeleteBook.as_view(), name="delete_book"),
    path("update/<int:pk>", UpdateBook.as_view(), name="update_book"),
    path("list_books", list_books, name="list_books"),
    path("sign_up", sign_up, name="sign_up"),


    path("login", LoginView.as_view(template_name="login.html"), name="login"),

    
    path("logout", LogoutView.as_view(),name="logout")

]

