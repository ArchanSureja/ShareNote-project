from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from urllib.parse import urlencode

# Create your views here.

def home(request):
    return render(request, 'home.html')


def register(request):
    content = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        cnfrmpassword = request.POST.get('cnfrmpassword')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists() and password != cnfrmpassword:
            note = 'This username is already taken. Enter a unique username. and Passwords do not match'
            content = { 'msg':note, 'username': request.POST.get('username', ''),'email': request.POST.get('email', '') }

        elif User.objects.filter(username=username).exists():
            content = { 'msg':'This username is already taken. Enter a unique username.', 'username': request.POST.get('username', ''),'email': request.POST.get('email', '') }

        elif password != cnfrmpassword:
            content = {'msg':'Passwords do not match.', 'username': request.POST.get('username', ''),'email': request.POST.get('email', '') }
        
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return redirect('/login')
    
    return render(request, 'register.html', content)


def login_user(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST" :
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            user = authenticate(username = username, password = password, email = email)   

            if user is not None:    
                login(request, user)
                return redirect("/")
            else:
                content = {'msg' : 'Enter valid credentials.'}
                return render(request, 'login.html', content) 
        else:
            return render(request, 'login.html')
        
def logout_user(request):
    logout(request)
    return redirect('/login')


def resetPasswordPage(request):
    if request.user.is_authenticated:
        return render(request, 'resetPassword.html')
    else:
        return redirect('/login')


def PassReset(request):
    if request.method == 'POST':
        password = request.POST['password']
        passwordNew = request.POST['passwordNew']
        
        user = request.user
        if user.check_password(password):
            user.set_password(passwordNew)
            user.save()
            
            logout(request)
            msg = 'Password successfully updated.'
            return render(request, 'resetPassword.html', {'msg': msg})
            
        else:
            msg = 'Current password is incorrect.'
            return render(request, 'resetPassword.html', {'msg': msg})
        
    
def forgotPasswordPage(request):
    return render(request, 'forgotPassword.html')
    

def PassForgot(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwordNew = request.POST['passwordNew']
        cnfrmpasswordNew = request.POST['cnfrmpasswordNew']

        if User.objects.filter(username=username).exists():
            if passwordNew == cnfrmpasswordNew:
                user = User.objects.get(username=username)
                user.set_password(passwordNew)  
                user.save()

                logout(request)

                msg = 'Password successfully updated.'
                return render(request, 'forgotPassword.html', {'msg': msg})

            else : 
                msg = 'Passwords do not match.'
                return render(request, 'forgotPassword.html', {'msg': msg})
        
        else:
            msg = 'User does not match.'
            return render(request, 'forgotPassword.html', {'msg': msg})




