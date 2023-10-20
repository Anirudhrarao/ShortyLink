"""
URL configuration for ShortyLink project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import home, register_page, login_page, logout_page, shorten_url, url_list, redirect_to_long_url

urlpatterns = [
    path("", home, name="home"),
    path("register-page/", register_page, name="register"),
    path("login-page/", login_page, name="login"),
    path("logout/", logout_page, name="logout"),
    path("shortener/", shorten_url, name="shortener"),
    path("urls/", url_list, name="urls"),
    path('r/<str:short_code>/', redirect_to_long_url, name='redirect_to_long_url'),
    path('admin/', admin.site.urls),
]
