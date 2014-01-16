from blog.models import Post, Comment
from news.models import News
from django.shortcuts import render_to_response
from django.template import RequestContext


def homepage(request):
    posts = Post.published_objects.all()[:4]
    popular_posts = Post.published_objects.order_by('-no_views')[:5]
    recent_comments = Comment.objects.all()[:4]
    news = News.get_published.all()[:4]
    ci = RequestContext(request)
    return render_to_response('homepage/index.html', {'posts': posts, 'popular_posts': popular_posts, 
                        'recent_comments': recent_comments, 'news_list': news}, ci)
