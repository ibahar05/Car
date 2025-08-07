from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout # import login to log the user in
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import View



def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                # If authentication is successful, log the user in
                login(request, user) 
                messages.success(request, f"You're Now Logged in as {username}")
                # Redirect to a success page or dashboard
                return redirect('main:home') # Replace 'home_page' with your actual URL name
            else:
                # If authentication fails, add an error message to the form
                messages.error(request, f"An error occured.")
        else:
            messages.error(request, f'An error occured trying to login.')
    elif request.method == 'GET':
        login_form = AuthenticationForm()
        
    return render(request, 'users/login.html', {'login_form': login_form})

@login_required
def logout(request):
    logout(request)
    return redirect (reverse("main:main"))



class Register(View):
    def get(self, request):
        register_form = UserCreationForm()
        return render(request,"users/register.html",{"register_form":register_form})

    def post(self, request):
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()
            login(request, user)
            messages.success(
                request, f" User {user.username} registered successfully"
            )
            return redirect("main:home")
        
        else:
            messages.error(request, f" An error accured trying to register")
            return render(request,"users/register.html",{"register_form":register_form})