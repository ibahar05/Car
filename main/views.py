from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def main(request):
    return render(request,"views/main.html")

@login_required
def home(request):

    return render(request, "views/home.html")

