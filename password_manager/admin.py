#Ce bout de code permet d'ajouter les tables au panneau d'administration de Django

from django.contrib import admin

from .models import Password

admin.site.register(Password)