from django.shortcuts import render,redirect
from .forms import Login_form,Register_form,BlogUploadForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Blog,UserProfile
from django.contrib.auth.models import User 
# Create your views here.

def home_view(request):
    user = request.user
    user_profile = UserProfile.objects.filter(id= user.id)
    return render(request,"home.html",{'user':user, 'user_profile':user_profile})

def login_view(request):
    if request.method == "POST":
        form = Login_form(request,data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("home")
    else:
        form = Login_form()
        redirect("home")
    return render(request,"login.html",context={"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request):
    if request.method == "POST":
        form = Register_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username,password=password )
            if user is not None:
                login(request,user)
                user_model = User.objects.get(username=username)
                new_profile =  UserProfile.objects.create(user=user_model)
                new_profile.save()
                print("sucess") 
                return redirect("home")
    else:
        print("Failed")
        form = Register_form()
    return render(request, "register.html",{"form":form})

def blogs_view():
    pass

@login_required
def blog_upload(request):
    if request.method == "POST" :
        form = BlogUploadForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            print("success")
            redirect("home")
    else:
        print("failde")
        form = BlogUploadForm()
    return render(request,"blogupload.html",{"form":form})

def all_blogs(request):
    items =  Blog.objects.all()
    return render(request, 'allblogs.html',{"items":items})

@login_required
def my_blogs(request):
    items = Blog.objects.filter(user=request.user)
    return render(request, 'myblogs.html',{"items":items})
