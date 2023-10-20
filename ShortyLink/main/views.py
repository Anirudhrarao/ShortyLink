from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from main.utils import generate_unique_short_code
from .models import ShortenedURL
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'base.html',context={'page':'Home'})

def register_page(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.filter(username=username)
            if user.exists():
                messages.error(request,'Username already taken.')
                return redirect('register')
            else:
                user = User.objects.create(
                    email=email,
                    username=username
                )
                user.set_password(password)
                user.save()
                messages.success(request,f'Welcome {username} your registration done successful.')
                return redirect('home')
        return render(request,'register.html',context={'page':'Register'})
    except Exception as e:
        raise e

def login_page(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if not User.objects.filter(username=username).exists():
                messages.error(request, 'Invalid username')
                return redirect('login_page')
            else:
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request, 'Logged in successfully')
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid credentials')
        return render(request,'login.html',context={'page':'Login'})
    except Exception as e:
        raise e
    
def logout_page(request):
    try:
        logout(request)
        messages.success(request, 'You have been successfully logged out.')
        return redirect('home')
    except Exception as e:
        raise e


@login_required(login_url='login')
def shorten_url(request):
    try:
        if request.method == 'POST':
            long_url = request.POST.get('long_url')
            short_code = generate_unique_short_code()
            shortened_url = ShortenedURL(user=request.user,
                                        long_url=long_url,
                                        short_code=short_code)
            shortened_url.save()
            messages.success(request,'url')
            return redirect('urls')
        return render(request, 'shorten_url.html',context={'page':'URL Shortener'})
    except Exception as e:
        raise e 

@login_required(login_url='login')
def url_list(request):
    try:
        urls = ShortenedURL.objects.all()
        return render(request,'url_list.html',{'urls':urls})
    except Exception as e:
        raise e
    
def redirect_to_long_url(request, short_code):
    shortened_url = get_object_or_404(ShortenedURL, short_code=short_code)
    return redirect(shortened_url.long_url)