"""Billing_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from Billing_App import views

urlpatterns = [
    path('', views.main_page),
    path('login',views.login),
    path('admin_page',views.admin_page),
    path('add_items',views.add_items),
    path('View_items',views.View_items),
    path('update_items/<edid>',views.update_items),
    path('update_items_post/<edid>',views.update_items_post),
    path('delete_added_items/<dltid>',views.delete_added_items),
    path('create_bill',views.create_bill),
    path('bill_detils/<int:pk>',views.bill_detils),


]
