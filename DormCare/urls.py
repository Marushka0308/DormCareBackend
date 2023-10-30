"""DormCare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from DormCare.sign_up_views import sign_up
from DormCare.login_views import login
from django.contrib import admin
from django.urls import path
from DormCare import sign_up_views
from DormCare import complain_views
from DormCare import announcements
from DormCare import login_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', sign_up_views.sign_up),
    path('complain/', complain_views.complain),
    path('complain/<int:id>',complain_views.complain_detail),
    path('announcements/',announcements.announcement),
    path('login/', login_views.login, name='login'),
]

