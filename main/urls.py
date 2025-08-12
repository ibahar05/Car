from django.urls import path
from main import views

app_name = "main"

urlpatterns = [
    path("",views.main, name = "main"),
    path("home/",views.home, name="home"),
    path("list/",views.list_view, name="list"),
]

