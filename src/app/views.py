from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register_request(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UserCreationForm()
    context = {
        "form": form,
        "form_title": "Register"
    }
    return render(request=request, template_name="form.html", context=context)

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            print("yippee")
            user = form.save()
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("/")
        messages.error(request, "Unsuccessful login. Invalid information.")
    form = AuthenticationForm()
    context = {
        "form": form,
        "form_title": "Login"
    }
    return render(request=request, template_name="form.html", context=context)

def home(request):
    return render(request, "base.html")

