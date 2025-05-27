from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CarForm
from .models import Car

def main(request):
    return render(request,"views/main.html")

@login_required
def home(request):
    
    context = {
        'item_list' : Car.objects.all()
    }
    return render(request, "views/home.html",context)

def create_item(request):
    form = CarForm(request.POST or None )

    if form.is_valid():
       form.save()
       return redirect("main:home")
    return render(request, "views/create_item.html",{'form':form})