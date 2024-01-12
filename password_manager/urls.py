"""
URL configuration for password_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import export_passwords_csv
from .views import import_passwords_csv

urlpatterns = [
    path("admin/", admin.site.urls),

    # Vue login
    path("", views.login_view, name="login"),
    # Vue login_user
    path("login_user/", views.login_user, name="login_user"),
    # Vue logout
    path("logout/", views.logout_view, name="logout"),
    # Vue liste des mots de passe
    path("list/", views.list, name="list"),
    # Vue ajout d'un mot de passe
    path("add_password/", views.add_password, name="add_password"),
    path("delete_password/<int:id>", views.delete_password, name="delete_password"),
    path("update_password/<int:id>", views.update_password, name="update_password"),
    path('export/csv/', export_passwords_csv, name='export_passwords_csv'),
    path('import/csv/', import_passwords_csv, name='import_passwords_csv'),
]
