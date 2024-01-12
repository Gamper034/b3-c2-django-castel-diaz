from django.http import HttpResponse
from .models import Password
from django.template import loader
from django.shortcuts import render, redirect
import csv
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        return redirect('list')
    else:
        return render(request, 'registration/login.html')

def login_user(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None:
        login(request, user)
        return redirect("list")
    else:
        return redirect("login")

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def list(request):
    password_list = Password.objects.all()
    context = {"password_list": password_list}
    return render(request, "list.html", context)
    # return render(request, "password_manager/list.html")

@login_required
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

@login_required
def delete_password(request, id):
    password = Password.objects.get(id=id)
    password.delete()
    return redirect("list")

@login_required
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

@login_required
def export_passwords_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="passwords.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Login', 'URL', 'Password'])

    passwords = Password.objects.all().values_list('name', 'login', 'url', 'password')
    for password in passwords:
        writer.writerow(password)

    return response

@login_required
def import_passwords_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        for row in reader:
            password = Password(name=row['Name'], url=row['URL'], login=row['Login'], password=row['Password'])
            password.save()

        return redirect('list')
    else:
        return HttpResponse('Only POST method is allowed')
