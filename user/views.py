from django.shortcuts import render ,redirect
from .models import User
from django.contrib import auth
# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['phone']
        address = request.POST['address']

        rs = User.objects.filter(username = username)
        if rs.exists():
            return render(request,'user/signup.html')
        else:
            User.objects.create(
                username=username,password=password,phone = phone , address= address
            )
            return render(request , 'user/login.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.hmtl')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        rs = User.objects.filter(username=username, password=password ,phone=phone ,address=address).first()

        if rs is not None:
            auth.login(request, rs)
            return redirect('/home/')
        else:
            return render(request, 'login.html')
    
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/login/')
    return render(request, 'login.html')

        