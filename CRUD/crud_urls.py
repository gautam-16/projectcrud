"""django_project1 URL Configuration

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
from django.urls import path,include
from.import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('index/create',views.create,name='create'),
    path('index/read',views.read,name='read'),
    path('index/update',views.update,name='update'),
    path('index/delete/<int:emp_id>',views.delete,name='delete'),
]