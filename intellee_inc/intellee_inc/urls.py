"""intellee_inc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from project_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project_app.urls')),
    path('', include('courses_app.urls')),
    path('', views.index, name = 'index'),
    path('home/', views.home_page, name = 'home'),
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.user_login, name = 'login'),
    path('courses/', views.courses, name = 'courses'),
    path('profile/', views.user_profile, name = 'profile'),
    path('enrollment/', views.user_enrollment, name = 'enrollment'),
    path('logout/', views.user_logout, name = 'logout'),
    path('changepass/', views.change_pass, name = 'change_pass' ),
]
