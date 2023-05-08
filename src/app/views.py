from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import ApplicationForm


def register_form(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    form = UserCreationForm()
    context = {"form": form, "form_title": "Register"}
    return render(request=request, template_name="register.html", context=context)


def login_form(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return redirect("/")
            else:
                print("User not found")
    form = AuthenticationForm()
    context = {"form": form, "form_title": "Login"}
    return render(request, "login.html", context=context)


def logout_form(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")


@login_required
def add_application(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            Job(
                title=form.cleaned_data["title"],
                company=form.cleaned_data["company"],
                link=form.cleaned_data["link"],
                date_applied=form.cleaned_data["date_applied"],
                stage=form.cleaned_data["stage"],
                stage_completed=form.cleaned_data["stage_completed"],
                stage_deadline=form.cleaned_data["stage_deadline"],
                applicant=request.user,
            ).save()
        return redirect("/")
    form = ApplicationForm()
    context = {"form": form, "form_title": "Add Application"}
    return render(request, template_name="form.html", context=context)


@login_required()
def edit_application(request, id):
    job = Job.objects.get(id=id)
    if request.method == "GET":
        form = ApplicationForm(instance=job)
        context = {"form": form}
        return render(request, template_name="form.html", context=context)
    elif request.method == "POST":
        form = ApplicationForm(request.POST, instance=job)
        if form.is_valid():
            job = form.save()
    return redirect("/")


@login_required
def home(request):
    username = request.user.username
    user_jobs = Job.objects.filter(applicant=request.user.id)
    print(user_jobs)
    context = {"username": username, "user_jobs": user_jobs}

    return render(request, "home.html", context=context)
