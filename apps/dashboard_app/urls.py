from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('login', views.login, name='login'),
	path('dashboard', views.dashboard, name='dashboard'),
	path('album/add', views.addalbum, name='addalbum'),
	path('picture/add', views.addpicture, name='addpicture'),
]
