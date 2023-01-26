
from django.contrib import admin
from django.urls import path, include
from books.views import index, create_book


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),

]

