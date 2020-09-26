from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from todoapp.views import home ,  show

# Create your views here.

def login(request):
    if request.method == 'POST':
        user  = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not  None:
            auth.login(request, user)
            return redirect('show')
        else:
            return render(request, 'login.html', {'error' : "Invalid login credentials"})  
    else:
        return render(request, 'login.html')          

def signup(request):
    if request.method == 'POST':
        # creates a new user
        if request.POST['password'] == request.POST['password2']:
            # checkin if password match
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'register.html', {'error' : "Username already taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password']) 
                auth.login(request, user)
                return render(request, 'showdiary.html')   
        else:
            return render(request, 'register.html', {'error' : "Passwords do not match"})        
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')

