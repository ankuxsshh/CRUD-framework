"""learn URL Configuration

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
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('index',views.index),
    path('userreg',views.userreg),
    path('userv',views.userv),
    path('contactv',views.contactv),
    path('contactsave',views.contactsave),
    path('userlogin',views.userlogin),
    path('logout',views.logout),
    path('profilev',views.profilev),
    path('adminprofile',views.adminprofile),
    path('delete/<int:id>',views.delete,name='delete'),
    path('dele/<int:id>',views.dele,name='dele'),
    path('update/<int:id>',views.update,name='update'),
    path('update/updates/<int:id>',views.updates,name='updates'),
    path('uupdate/<int:id>',views.uupdate,name='uupdate'),
    path('uupdate/uupdates/<int:id>',views.uupdates,name='uupdates'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
