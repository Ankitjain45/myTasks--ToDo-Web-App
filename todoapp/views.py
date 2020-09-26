from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import todo

# Create your views here.

def show(request):
    log_user = request.user
    todos = todo.objects.filter(user = log_user)
    context = {'entries' : todos}
    print(log_user)
    return render(request, 'showdiary.html', context)

def home(request):
    return render(request, 'login.html')

def add(request):
    print(request.method)
    if request.method == "POST":
        print("hiii")
        content1 = request.POST.get('content')  
        title1 = request.POST.get('title')
        todo1 = todo(content=content1, title=title1, user=request.user)
        todo1.save()
        return redirect("show")

    else:
        print("noooooo")
        return render(request, 'addtodo.html')   



    