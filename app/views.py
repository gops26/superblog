from django.shortcuts import render,redirect
from .forms import Login_form
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def home_view(request):
    return render(request,"home.html")

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
    return logout(request)

def register_view():
    pass

def blogs_view():
    pass
