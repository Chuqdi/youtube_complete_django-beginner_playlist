
from django.contrib import admin
from django.urls import path, include
from books.views import index,create_book, list_books
from users.views import sign_up
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("create_book", create_book, name="create_book"),
    path("list_books", list_books, name="list_books"),
    path("sign_up", sign_up, name="sign_up"),


    path("login", LoginView.as_view(template_name="login.html"), name="login"),

    
    path("logout", LogoutView.as_view(),name="logout")

]

