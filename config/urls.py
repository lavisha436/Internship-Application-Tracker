"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from applications.views import add_application, application_list, delete_application, edit_application, home, logout_user, register_user , login_user

urlpatterns = [
    path("admin/", admin.site.urls),
    path("add-application/", add_application, name="add_application"),
    path("register/", register_user, name="register_user"),
    path("", home, name="home"),
    path("login/", login_user, name="login_user"),
    path("logout/", logout_user, name="logout_user"),
    path("applications/", application_list, name="application_list"),
    path("delete/<int:id>/", delete_application, name="delete_application"),
    path("edit/<int:id>/", edit_application, name="edit_application"),
]
