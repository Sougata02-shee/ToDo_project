from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.http import Http404

def login_(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        u=authenticate(username=username,password=password)
        print(u)

        if u is not None:
            login(request,u)
            return redirect('home')
        else:
            return render(request,'wrong.html')

    return render(request,'login_.html')

def register(request):

    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        User.objects.create_user(username=username,password=password,email=email)
        return redirect('login_')

    return render(request,'register.html')

def logout_(request):

    logout(request)

    return redirect('login_')


