"""config URL Configuration

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
from django.urls import path, include
import board.views
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user.views.login),
    
    path('board/list', board.views.list, name='board_list'),
    path('board/popup', board.views.popup, name='board_popup'),
    
    path('user/signup', user.views.signup),
    path('user/login', user.views.login, name='user_login'),
    path('user/logout', user.views.logout, name='user_logout'),
    path('user/changepw', user.views.changepw, name='user_changepw'),
]
"""     path('board/create', board.views.create),
    path('board/read/<int:bid>', board.views.read),
    path('board/delete/<int:bid>', board.views.delete),
    path('board/update/<int:bid>', board.views.update), """