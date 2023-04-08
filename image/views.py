from django.shortcuts import render, redirect
from .models import Image
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages #import messages
from django.core.files.storage import FileSystemStorage
import os, secrets, datetime
from testproject.helpers import HelperClass
from django.core.paginator import Paginator

def index(request):
    data=Image.objects.all().order_by("id")
    paginator = Paginator(data, per_page=2)
    page = request.GET.get('page', 1)
    page_object = paginator.get_page(page)
    context = {"page_obj": page_object}
    # HelperClass.genrrate_image_path(data)
    return render(request,'image/index.html', context)

# def create(request):
#     return render(request,'user/create.html')

def store(request):
    if request.method=='POST':
        image = request.FILES['image']
        title = request.POST.get('title', '')
        # os.chmod('media/photos', 755)

        filename, file_extension = os.path.splitext(image.name)
        secret_range  = secrets.SystemRandom()
        salt=secret_range.randrange(100000, 999999)

        obj = Image(author=request.user.id, title=title,filename=image.name, salt=salt, status=1, extension=file_extension)
        obj.save()
        date = obj.created_at
        path ='media/files/images/'+str(date.year)+'/'+str(date.month)+'/'+str(date.day)+'/'+str(date.strftime("%f"))+'-'+str(obj.salt)+'/'+str(date.year)+str(date.month)+str(date.day)+'_'+str(date.strftime("%f"))+'-'+str(obj.salt)
        # path ='media/files/images/'+date.year+'/'+date.month+'/'+date.day+'/'+date.strftime("%f")+'-'+obj.salt+'/'+date.year+date.month+date.day+'_'+date.strftime("%f")+'-'+obj.extension
        fs =FileSystemStorage(location=path)
        uploadfilename = fs.save(image.name,image)
        dd(  path)
        # object = Image()
        # object.save()
    # return render(request,'user/index.html')
    #  return redirect("user")  
    return redirect('image:index')

# def user_login(request):
#     if (request.method == 'POST'):
#         username = request.POST.get('username', null)
#         password = request.POST.get('password', null)
#         user = authenticate(username=username, password=password)
#         if user:
#             login(request, user)
#             messages.success(request, "Loged In Successfull" )
#             return redirect('user:profile')
#         else:
#             messages.error(request, "Check You Credentials" )
#             return redirect('user:login')
#     return render(request, 'user/login.html')

# def user_logout(request):
#     logout(request)
#     return redirect('user:login')

# def register(request): 
#     if (request.method == 'POST'):
#         username = request.POST['username']
#         password = request.POST['password']
#         # password = request.POST.get("password", null)
#         email = request.POST['email']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         if User.objects.filter(username=username).exists():
#             messages.error(request, "User Allready exist" )
#             return render(request, 'user/register.html')
#         else:
#             user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request, "Registered Successfull" )
#             return redirect('user:profile')
#     return render(request, 'user/register.html')

# # @login_required
# def profile(request):
#     data =request.user
#     if request.method == 'POST':
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage();
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'core/simple_upload.html', {
#             'uploaded_file_url': uploaded_file_url
#         })

#     return render(request, 'user/profile.html',{'data':data})