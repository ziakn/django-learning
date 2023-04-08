from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages #import messages
from django.core.files.storage import FileSystemStorage


def index(request):
    return render(request,'user/index.html')

def create(request):
    return render(request,'user/create.html')

def store(request):
    # return render(request,'user/index.html')
    #  return redirect("user")  
    return redirect('user:index')

def user_login(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Loged In Successfull" )
            return redirect('user:profile')
        else:
            messages.error(request, "Check You Credentials" )
            return redirect('user:login')
    return render(request, 'user/login.html')

def user_logout(request):
    logout(request)
    return redirect('user:login')

def register(request): 
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if User.objects.filter(username=username).exists():
            messages.error(request, "User Allready exist" )
            return render(request, 'user/register.html')
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registered Successfull" )
            return redirect('user:profile')
    return render(request, 'user/register.html')

# @login_required
def profile(request):
    data =request.user
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage();
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })

    return render(request, 'user/profile.html',{'data':data})