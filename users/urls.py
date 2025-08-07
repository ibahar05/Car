from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/",views.login_view, name= "login_view"),
    path("register/",views.Register.as_view(), name= "register"),
    path("logout/",views.logout, name = "logout"),
]



