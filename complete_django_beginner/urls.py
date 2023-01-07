
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def user(request):
    return HttpResponse("<h1>All The User</h1>")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("user", user, name="user")
]

