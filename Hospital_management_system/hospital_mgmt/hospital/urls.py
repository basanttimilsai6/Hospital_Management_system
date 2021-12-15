"""hospital_mgmt URL Configuration

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
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('suggest/', views.suggest, name='suggest'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout_admin, name='logout'),
    # path('index/', views.Index, name='index'),
    path('view_doctor/', views.View_Doctor, name='view_doctor'),
    path('add_doctor/', views.Add_Doctor, name='add_doctor'),
    path('delete_doctor/<int:id>', views.Delete_Doctor, name='delete_doctor'),
    path('update_doctor/<int:id>', views.Update_Doctor, name='update_doctor'),
    path('view_patient/', views.View_Patient, name='view_patient'),
    path('add_patient/', views.Add_Patient, name='add_patient'),
    path('delete_patient/<int:id>', views.Delete_Patient, name='delete_patient'),
    path('update_patient/<int:id>', views.Update_Patient, name='update_patient'),
    path('view_appointment/', views.View_Appointment, name='view_appointment'),
    path('add_appointment/', views.Add_Appointment, name='add_appointment'),
    path('delete_appointment/<int:id>', views.Delete_Appointment, name='delete_appointment'),
    path('update_appointment/<int:id>', views.Update_Appointment, name='update_appointment'),
]
