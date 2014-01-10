# Create your views here.
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from .models import Post
from .models import Comment
from django import  forms
from django.views.decorators.csrf import csrf_exempt


class comment_form(forms.Form):
    comment = forms.CharField(
               widget=forms.Textarea())


def post_view(request):
    """view to display all post"""
    template_name = "posts.html"
    ci = RequestContext(request)
    posts=Post.objects.all()
    return render_to_response(template_name ,{'posts':posts,}, ci)


@csrf_exempt
def detail_view(request ,year, month, day, slug):
    """ view to get post detail and add comment """
    template_name = "blog/post_detail.html"  
    ci = RequestContext(request)
    form= comment_form()
    post=Post.objects.get(slug=slug)
    return render_to_response(template_name ,{'form':form, 'post':post} , ci )


def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = comment_form(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            user = request.user
            c = Comment.objects.create(post=post, user=user, body=comment)
            year = post.pub_date.strftime("%Y")
            month = post.pub_date.strftime("%b").lower()
            day = post.pub_date.strftime("%d")
            slug = post.slug
            return HttpResponseRedirect('/blog/{0}/{1}/{2}/{3}'.format(year,month,day,slug))



def get_blog_by_tag(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response('blog/search_result.html', {'object_list':posts, 'tag': tag})
	
"""
    ci = RequestContext(request)
    form= comment_form()
    post=Post.objects.get(slug=slug)
    if request.is_ajax():
        if request.method=="POST":
        comment=request.POST.get("comment")
            user=request.user          
            data = Comment.objects.create(post=post,user=user,body=comment)
            return render_to_response("blog/comment.html",{'comment':data},ci)
        else:
            return render_to_response(template_name ,{'form':form, 'post':post} , ci )
    else:
    if request.method=="POST":
        form = comment_form(request.POST)
        if form.is_valid():
                    comment=form.cleaned_data['comment']
                    user=request.user 
                    data = Comment.objects.create(post=post,user=user,body=comment)
                    return HttpResponseRedirect('/blog/detail/'+str(post.id)+'/')
        else:
                return render_to_response(template_name ,{'form':form, 'post':post} , ci )
        else:
                return render_to_response(template_name ,{'form':form, 'post':post} , ci )
                """