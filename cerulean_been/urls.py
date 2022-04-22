"""cerulean_been URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from cerulean.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('signup',signup,name='signup'),
    path('home',home,name='home'),
    path('artwork_order',artwork_order,name='artwork_order'),
    path('employee_details',employee_details,name='employee_details'),
    path('print_order',print_order,name='print_order'),
    path('project_cost_analysis',project_cost_analysis,name='project_cost_analysis'),
    path('add_artwork_order',add_artwork_order,name='add_artwork_order'),
    path('add_employee_work',add_employee_work,name='add_employee_work'),
    path('view_deatils_artwork/<int:pid>',view_deatils_artwork,name="view_deatils_artwork"),
    path('delete_artwork/<int:pid>',delete_artwork,name="delete_artwork"),
    path('edit_artwork_order/<int:pid>',edit_artwork_order,name="edit_artwork_order"),
    path('view_employee_work/<int:pid>',view_employee_work,name="view_employee_work"),
    path('delete_employee_work/<int:pid>',delete_employee_work,name="delete_employee_work"),
    path('edit_employee_work/<int:pid>',edit_employee_work,name="edit_employee_work"),
    path('add_print_order',add_print_order,name='add_print_order'),
    path('view_print_order/<int:pid>',view_print_order,name='view_print_order'),
    path('Logout',Logout,name="Logout"),
]
