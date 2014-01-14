from blog.models import Post, Comment
from news.models import News
from django.shortcuts import render_to_response

def homepage(request):
	posts = Post.published_objects.filter(featured=True)[:4]
	popular_posts = Post.published_objects.all()[:5]
	comments = Comment.objects.all()[:5]
	queryset = News.get_published.all()[:4]
	return render_to_response('homepage/index.html', {'posts': posts, 'popular_posts': popular_posts, 
						'comments': comments, 'news_list': queryset})
