from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	return redirect('dashboard')

def dashboard(request):
	return render(request, "clickable.html")

def login(request):
	return render(request, "login_page.html")

def addalbum(request):
	return render(request, "album_add.html")

def addpicture(request):
	return render(request, "picture_add.html")
