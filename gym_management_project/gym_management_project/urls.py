"""gym_management_project URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from gym_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page,name='home'),
    path('login/', views.login_page,name='login'),
    path('logout/', views.user_logout,name='logout'),

    path('add_enquiry/', views.add_enquiry,name='add_enquiry'),
    path('view_enquiry/', views.view_enquiry,name='view_enquiry'),
    path('delete_enquiry/<int:id>/', views.delete_enquiry,name='delete_enquiry'),

    path('add_equipment/', views.add_equipment,name='add_equipment'),
    path('view_equipment/', views.view_equipment,name='view_equipment'),
    path('delete_equipment/<int:id>/', views.delete_equipment,name='delete_equipment'),

    path('add_plan/', views.add_plan,name='add_plan'),
    path('view_plan/', views.view_plan,name='view_plan'),
    path('delete_plan/<int:id>/', views.delete_plan,name='delete_plan'),

    path('add_member/', views.add_member,name='add_member'),
    path('view_member/', views.view_member,name='view_member'),
    path('delete_member/<int:id>/', views.delete_member,name='delete_member'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)