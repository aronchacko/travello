from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=="POST":
        username = request.POST['Username']
        firstname = request.POST['Firstname']
        lastname = request.POST['Lastname']
        email = request.POST['Email']
        password = request.POST['Password']
        password1 = request.POST['Password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username has already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email has already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username, password=password, first_name=firstname,
                                              last_name=lastname,email=email)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password is wrong")
            return render('register')
        return redirect('/')
    return render(request,"register.html")



def login(request):
    if request.method == 'POST':
        username=request.POST['Username']
        password=request.POST['Password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"ivalid details")
            return redirect('login')

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')