from blog.models import Post
from django.shortcuts import render_to_response

def homepage(request):
	posts = Post.published_objects.all()
	return render_to_response('homepage/index.html', {'posts': posts})
