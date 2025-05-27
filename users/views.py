from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login # import login to log the user in
from django.contrib import messages



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
                messages.success(request, "You're Now Logged in as {username}")
                # Redirect to a success page or dashboard
                return redirect('main:home') # Replace 'home_page' with your actual URL name
            else:
                # If authentication fails, add an error message to the form
                login_form.add_error(None, "نام کاربری یا رمز عبور اشتباه است.")
    
    elif request.method == 'GET':
        login_form = AuthenticationForm()
        
    return render(request, 'users/login.html', {'login_form': login_form})