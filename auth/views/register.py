from auth.forms import RegistrationForm
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User
def registration_view(request):
    form=RegistrationForm()
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            cpassword=form.cleaned_data['cpassword']
            firstname=form.cleaned_data['first_name']
            lastname=form.cleaned_data['last_name']
            user=User.objects.create_user(username=name,email=email,password=password)
            user.first_name = firstname
            user.lastname = lastname
            return HttpResponse("from has been submit")
        else:
            return render_to_response('index.html',{'form':form},context_instance=RequestContext(request))
    else:
        return render_to_response('index.html',{'form':form},context_instance=RequestContext(request))
