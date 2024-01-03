from django.http import HttpResponse
from .models import Password
from django.template import loader
from django.shortcuts import render, redirect


def list(request):
    password_list = Password.objects.all()
    context = {"password_list": password_list}
    return render(request, "list.html", context)
    # return render(request, "password_manager/list.html")


def add_password(request):
    if request.method == "GET":
        return render(request, "add_password.html")
    else:
        name = request.POST.get("name")
        url = request.POST.get("url")
        login = request.POST.get("login")
        password = request.POST.get("password")
        password = Password(name=name, url=url, login=login, password=password)
        print(password)
        password.save()
        return redirect("list")


def delete_password(request, id):
    password = Password.objects.get(id=id)
    password.delete()
    return redirect("list")


def update_password(request, id):
    password = Password.objects.get(id=id)
    if request.method == "GET":
        context = {"password": password}
        return render(request, "update_password.html", context)
    else:
        password.name = request.POST.get("name")
        password.url = request.POST.get("url")
        password.login = request.POST.get("login")
        password.password = request.POST.get("password")
        password.save()
        return redirect("list")
