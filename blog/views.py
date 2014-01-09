# Create your views here.
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Post
from .models import Comment
from django import  forms

class comment_form(forms.Form):
    """"""
    comment = forms.CharField(widget=forms.TextInput())



def post_view(request):
    """view to collect post"""
    template_name = "post.html"
    ci = RequestContext(request)
    posts=Post.objects.all()
    return render_to_response(template_name ,{'posts':posts,}, ci)


def detail_view(request ,post_id):
    """view to get post detail and add comment"""
    template_name = "detail.html"  
    ci = RequestContext(request)
    form= comment_form()
    post=Post.objects.get(id=post_id)
    if request.method=="POST":
        form= comment_form(request.POST)
        if form.is_valid():
            comment=form.cleaned_data['comment']
            user=request.user           
            comment = Comment.objects.create(post=post,user=user,body=post)
            return render_to_response("comment.html",{'comment':comment},ci)
        else:
            return render_to_response(template_name ,{'form':form, 'post':post} , ci )
    else:
        return render_to_response(template_name ,{'form':form, 'post':post} , ci )




def add_comment(request , post_id):
    """views to store comment"""
    template_name="detail.html"
    ci = RequestContext(request)
    form = comment_form()
    if request.method=="POST":
	form= comment_form(request)
	if form.is_valid():
	    comment=form.cleaned_data['comment']
	    post = Post.objects.get(id=id)
	    user=request.user		
            comment = Comment.objects.create(post=post,user=user,body=post)
	    return HttpResponseRedirect("/detail/")
	else:
	    return render_to_response(template_name ,{'form':form} , ci )
    else:
        return render_to_response(template_name ,{'form':form} , ci )
	
