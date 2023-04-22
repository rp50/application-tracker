from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("register/", views.register_form, name="register"),
    path("login/", views.login_form, name="login"),
    path("logout/", views.logout_form, name="logout"),
    path("add/", views.add_application, name="add"),
]
