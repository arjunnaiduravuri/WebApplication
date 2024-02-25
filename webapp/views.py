from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'index.html')

def LoginFo(request):
    if request.method == "POST":
        usname = request.POST['uname']
        uspassword = request.POST['upassword']
        
        user= authenticate('request',username=usname,password=uspassword)

        if user is not None :
            messages.info(request, f"You are now logged in as {usname}.")
            login(request, user)
            return render(request, 'index.html')
        else:
            messages.info(request, "User Not Found")
            return render(request, 'register.html')
            # return redirect("registerPage")

    return render(request, 'login.html')

def RegisterPage(request):
    if request.method == 'POST':
        rname = request.POST['rname']
        remail = request.POST['remail']
        rpassword = request.POST['rpassword']
        rcpassword = request.POST.get('rcpassword')
        
        if User.objects.filter(username=rname).exists():
            messages.info(request, "Username Already Exists")
            return render(request, 'login.html')
        
            # return redirect('loginF')
        elif User.objects.filter(email=remail).exists():
            messages.info(request, "Email Already Exists")
            return render(request, 'login.html')
            # return redirect('loginF')
        else:
            user = User.objects.create_user(username=rname, email=remail, password=rpassword)
            user.save()
            messages.info(request, "User created sucesfully")
            return render(request, 'login.html')


            # return redirect('loginF')


    return render(request, 'register.html')