from blog.models import Post, Comment
from django.shortcuts import render_to_response

def homepage(request):
	posts = Post.published_objects.filter(featured=True)[:4]
	popular_posts = Post.published_objects.all()[:5]
	comments = Comment.objects.all()[:5]
	return render_to_response('homepage/index.html', {'posts': posts, 'popular_posts': popular_posts, 'comments': comments})
