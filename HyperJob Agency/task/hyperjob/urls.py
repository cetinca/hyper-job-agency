"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from resume import views as resume_views
from vacancy import views as vacancy_views

urlpatterns = [
    path('', vacancy_views.base, name='base'),
    path('home', vacancy_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('signup', vacancy_views.signup, name='signup'),
    path('login', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('vacancies', vacancy_views.VacancyListView.as_view(), name='vacancies'),
    path('vacancy/new', vacancy_views.VacancyCreateView.as_view(), name='vacancy_create'),
    path('resumes', resume_views.ResumeListView.as_view(), name='resumes'),
    path('resume/new', resume_views.ResumeCreateView.as_view(), name='resume_create'),
]
