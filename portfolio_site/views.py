from django.shortcuts import render,redirect
from .models import contacts
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout




# Create your views here.
def index(request):
    return render(request,'portfolio_site/index.html')

def contact(request):
    if request.method == 'POST':
        DB = contacts()
        DB.Name = request.POST.get("name")
        DB.LastName = request.POST.get("l_name")
        DB.Age = request.POST.get("age")
        DB.Email = request.POST.get("email")
        DB.Message = request.POST.get("message")

        DB.save()
        print('done')
        return render(request, 'portfolio_site/index.html')
    else:
        return render(request, 'portfolio_site/contact.html')

def project(request):
    return render(request,'portfolio_site/project.html')

def register(request):
    if request.method =='POST':
        first_name = request.POST['f_name']
        username = request.POST['username']
        password = request.POST['password1']    

        user = User.objects.create_user(first_name = first_name, username = username, password = password)
        user.save()
        return redirect('/')
    else:
        return render(request,'portfolio_site/register.html',{'form' : UserCreationForm})

def view_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = user_name, password = password)
        if user is not None:
            auth_login(request,user)
            return render(request,'portfolio_site/index.html')
            
    else:
        return render(request,'portfolio_site/login.html')

def view_logout(request):
    auth_logout(request)
    return redirect('/')