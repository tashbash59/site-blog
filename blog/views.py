from django.shortcuts import render

def Post_list(request):
	return render(request, 'blog/Post_list.html',{})