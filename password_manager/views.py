from django.http import HttpResponse
from .models import Password
from django.template import loader
from django.shortcuts import render

def list(request):
    password_list = Password.objects.all()
    context = {"password_list": password_list}
    return render(request, "list.html", context)
    # return render(request, "password_manager/list.html")