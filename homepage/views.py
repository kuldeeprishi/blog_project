from blog.models import Post, Comment
from news.models import News
from homepage.models import Subscriber
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.validators import validate_email
from django.views.decorators.csrf import csrf_exempt

def homepage(request):
    posts = Post.published_objects.all()[:4]
    news = News.get_published.all()[:4]
    ci = RequestContext(request)
    return render_to_response('homepage/index.html', {'posts': posts, 
    	'news_list': news,}, ci)
@csrf_exempt
def add_subscriber(request, email=None):
	if request.method == 'POST':
		email = request.POST['email_field']
		try:
			validate_email(email)
			e = Subscriber.objects.create(email=email)
			msg = "{0} added successfully".format(email)
		except:
			msg = ""
	return HttpResponse(msg)
		