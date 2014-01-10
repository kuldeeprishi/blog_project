# Create your views here.
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from .models import Post
from .models import Comment
from django import  forms
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


class comment_form(forms.Form):
    comment = forms.CharField(
               widget=forms.Textarea())


def post_view(request):
    """view to display all post"""
    template_name = "posts.html"
    ci = RequestContext(request)
    posts=Post.objects.all()
    return render_to_response(template_name ,{'posts':posts,}, ci)



def detail_view(request ,year, month, day, slug):
    """ view to get post detail and add comment """
    template_name = "blog/post_detail.html"  
    ci = RequestContext(request)
    form= comment_form()
    post=Post.objects.get(slug=slug)
    msg = ''
    user = request.user
    if not user.is_active:
        msg = "Kindly Login/Signup to Comment"
    return render_to_response(template_name ,{'form':form, 'post':post, 'login_required_msg':msg} , ci )



@csrf_exempt
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    template_name = "blog/post_detail.html"
    year = post.pub_date.strftime("%Y")
    month = post.pub_date.strftime("%b").lower()
    day = post.pub_date.strftime("%d")
    slug = post.slug
    form = comment_form()
    ci = RequestContext(request)
    user = request.user
    if request.is_ajax():
        if  user.is_active:
            if request.method=="POST":
                comment=request.POST.get("comment",'')
                if comment != '':
                    c = Comment.objects.create(post=post,user=user,body=comment)
                    args = {'comment': c,}
                else:
                    args = {'error': 'Comment cannot be blank'}
                return render_to_response("blog/comment.html", args, ci)
        else:
            return HttpResponse()
    else: # Save Comment and redirect
        if user.is_active:  
            if request.method == 'POST':
                form = comment_form(request.POST)
                if form.is_valid():
                    comment = form.cleaned_data['comment']
                    c = Comment.objects.create(post=post, user=user, body=comment)
                    return HttpResponseRedirect('/blog/{0}/{1}/{2}/{3}'.format(year,month,day,slug))
                else:
                    return render_to_response(template_name ,{'form':form, 'post':post} , ci )
        else:
            msg = "Kindly Login/Signup to Comment"
            return render_to_response(template_name, {'form':form, 'post':post,'login_required_msg':msg} , ci )




def get_blog_by_tag(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response('blog/search_result.html', {'object_list':posts, 'tag': tag})
	