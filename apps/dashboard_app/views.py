from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	return HttpResponse('Index route')
@login_required
def home(request):
	return render(request, 'login.html')
