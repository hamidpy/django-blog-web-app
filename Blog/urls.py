"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('', views.INDEX, name='home'),
    path('about/', views.ABOUT, name='about'),
    path('blog-single/', views.BLOGSINGLE, name='blog_single'),
    path('blog-single-alt/', views.BLOGSINGLEALT, name='blog_single_alt'),
    path('category/', views.CATEGORY, name='category'),
    path('classic/', views.CLASSIC, name='classic'),
    path('contact/', views.CONTACT, name='contact'),
    path('minimal/', views.MINIMAL, name='minimal'),
    path('personal/', views.PERSONAL, name='personal'),
    path('personal-alt/', views.PERSONALALT, name='personal_alt'),

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
