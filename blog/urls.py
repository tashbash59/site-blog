from django.urls import path
from . import views

urlpatterns = [
	path('', views.Post_list, name='Post_list')
]