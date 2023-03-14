from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def sign_up(request):
    form = UserCreationForm()

    if request.method =="POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "User Creation was successfuuly")
            return redirect("sign_up")

    return render(request, "sign_up.html", {"form":form})