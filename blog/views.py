# Create your views here.
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Post
from .models import Comment
from django import  forms
from django.views.decorators.csrf import csrf_exempt


class comment_form(forms.Form):
<<<<<<< HEAD
    """"""
    comment = forms.CharField(
               widget=forms.Textarea())
=======
    """
    Comment Form
    """
    comment = forms.CharField(widget=forms.TextInput())

>>>>>>> 6efd77ee927a3e40beb6c654d3ec66d83558f37a


def post_view(request):
    """view to display all post"""
    template_name = "posts.html"
    ci = RequestContext(request)
    posts=Post.objects.all()
    return render_to_response(template_name ,{'posts':posts,}, ci)


<<<<<<< HEAD
@csrf_exempt
=======
>>>>>>> 6efd77ee927a3e40beb6c654d3ec66d83558f37a
def detail_view(request ,post_id):
    """view to get post detail and add comment"""
    template_name = "detail.html"  
    ci = RequestContext(request)
    form= comment_form()
    post=Post.objects.get(id=post_id)
    if request.is_ajax():
    	if request.method=="POST":
		comment=request.POST.get("comment")
        	user=request.user          
        	data = Comment.objects.create(post=post,user=user,body=comment)
        	return render_to_response("comment.html",{'comment':data},ci)
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



def get_blog_by_tag(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response('blog/search_result.html', {'object_list':posts, 'tag': tag})
	
